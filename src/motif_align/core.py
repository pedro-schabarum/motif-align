"""
core.py — Alinhamento motívico automático entre versões de uma composição simbólica

Recebe duas versões de uma peça (MusicXML, via music21) e identifica trechos
correspondentes, determinando se um motivo foi transposto, invertido, retrogradado,
retrogradado-invertido ou fragmentado entre as versões — distinguindo relações
motívicas genuínas de coincidências espúrias de intervalo.

Abordagem:
  1. Representação por intervalo cromático (invariante a transposição por natureza).
  2. Geração de candidatos por janela deslizante.
  3. Alinhamento por semente-e-extensão (seed-and-extend, inspirado no BLAST):
     acha uma âncora curta e confiável, depois estende nota por nota em cada
     direção enquanto a transformação continuar batendo, parando por critério
     X-drop (queda de score maior que um limiar em relação ao melhor já visto).

Escopo desta versão: peças/linhas monofônicas (uma voz por vez).
"""

from dataclasses import dataclass
from typing import List, Tuple, Dict, Callable, Optional


# ---------------------------------------------------------------------------
# Representação
# ---------------------------------------------------------------------------

def extract_notes(part) -> list:
    """Extrai a sequência de notas de uma parte monofônica do music21
    (ignora pausas e acordes — fora do escopo desta versão)."""
    return [n for n in part.flatten().notes if n.isNote]


def interval_sequence(notes: list) -> List[int]:
    """Sequência de intervalos cromáticos (semitons) entre notas consecutivas.
    É invariante a transposição por construção: duas execuções da mesma melodia
    em tons diferentes geram a mesma sequência de intervalos."""
    return [notes[i + 1].pitch.midi - notes[i].pitch.midi for i in range(len(notes) - 1)]


# ---------------------------------------------------------------------------
# Transformações temáticas clássicas
#
# Derivação a partir da sequência de notas n0..nk (intervalos i1..ik):
#   inversão               -> nega cada intervalo, mantém a ordem
#   retrogradação          -> nega e inverte a ordem
#   retrogradação-inversão -> inverte a ordem, sem negar
#   transposição           -> não muda a sequência de intervalos (invariante)
# ---------------------------------------------------------------------------

def transposicao(intervals: List[int]) -> List[int]:
    return list(intervals)


def inversao(intervals: List[int]) -> List[int]:
    return [-i for i in intervals]


def retrogradacao(intervals: List[int]) -> List[int]:
    return [-i for i in reversed(intervals)]


def retrogradacao_inversao(intervals: List[int]) -> List[int]:
    return list(reversed(intervals))


TRANSFORMATIONS: Dict[str, Callable[[List[int]], List[int]]] = {
    "transposicao": transposicao,
    "inversao": inversao,
    "retrogradacao": retrogradacao,
    "retrogradacao_inversao": retrogradacao_inversao,
}


# ---------------------------------------------------------------------------
# Similaridade (distância de edição)
# ---------------------------------------------------------------------------

def edit_distance(seq_a: List[int], seq_b: List[int]) -> int:
    """Distância de Levenshtein entre duas sequências de intervalos."""
    n, m = len(seq_a), len(seq_b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if seq_a[i - 1] == seq_b[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost,
            )
    return dp[n][m]


def similarity(seq_a: List[int], seq_b: List[int]) -> float:
    """Similaridade normalizada em [0, 1]. 1.0 = idêntico, 0.0 = totalmente distinto."""
    if not seq_a and not seq_b:
        return 1.0
    max_len = max(len(seq_a), len(seq_b), 1)
    return 1.0 - (edit_distance(seq_a, seq_b) / max_len)


def best_transformation_match(seq_a: List[int], seq_b: List[int]) -> Tuple[str, float]:
    """Testa seq_a contra as 4 transformações clássicas e compara com seq_b,
    retornando a transformação de maior similaridade."""
    best_name, best_score = "nenhuma", -1.0
    for name, transform_fn in TRANSFORMATIONS.items():
        score = similarity(transform_fn(seq_a), seq_b)
        if score >= best_score:
            best_name, best_score = name, score
    return best_name, best_score


# ---------------------------------------------------------------------------
# Geração de candidatos (janela deslizante)
# ---------------------------------------------------------------------------

@dataclass
class Candidate:
    start: int
    length: int
    intervals: List[int]


def sliding_windows(intervals: List[int], min_len: int = 4, max_len: int = 7) -> List[Candidate]:
    """Gera todas as subsequências de tamanho entre min_len e max_len (em número
    de intervalos). min_len/max_len calibram o quão curto pode ser um motivo
    considerado — parâmetro que se mostrou metodologicamente relevante nos
    testes preliminares (afeta diretamente a taxa de falsos positivos)."""
    candidates = []
    n = len(intervals)
    for length in range(min_len, max_len + 1):
        for start in range(0, n - length + 1):
            candidates.append(Candidate(start, length, intervals[start:start + length]))
    return candidates


# ---------------------------------------------------------------------------
# Semente-e-extensão (seed-and-extend, inspirado no BLAST)
# ---------------------------------------------------------------------------

@dataclass
class Alignment:
    start_a: int
    end_a: int
    start_b: int
    end_b: int
    transformation: str
    score: float
    seed_score: float


def find_seeds(cand_a: Candidate, intervals_b: List[int], threshold: float) -> List[tuple]:
    """Acha âncoras: janelas em B que batem bem com a candidata de A sob
    alguma das transformações clássicas. Curtas e exigentes por construção
    (só avança se score >= threshold), pra manter a etapa de busca barata."""
    seeds = []
    n = len(intervals_b)
    length = cand_a.length
    for start_b in range(0, n - length + 1):
        window_b = intervals_b[start_b:start_b + length]
        name, score = best_transformation_match(cand_a.intervals, window_b)
        if score >= threshold:
            seeds.append((start_b, start_b + length, name, score))
    return seeds


def extend_seed(
    intervals_a: List[int],
    intervals_b: List[int],
    start_a: int, end_a: int,
    start_b: int, end_b: int,
    transformation: str,
    x_drop: float = 0.3,
) -> Alignment:
    """Estende a âncora nota por nota em cada direção enquanto a transformação
    continuar batendo, parando quando o score cair mais que x_drop abaixo do
    melhor score já visto (critério X-drop, como no BLAST). Corrige a limitação
    encontrada nos testes preliminares: a semente acha a região certa, mas não
    necessariamente a fronteira exata do motivo."""
    transform_fn = TRANSFORMATIONS[transformation]

    def score_of(sa, ea, sb, eb):
        return similarity(transform_fn(intervals_a[sa:ea]), intervals_b[sb:eb])

    sa, ea, sb, eb = start_a, end_a, start_b, end_b
    best_score = score_of(sa, ea, sb, eb)
    best_bounds = (sa, ea, sb, eb)

    # extensão à direita: avança enquanto não cair mais que x_drop abaixo do
    # pico, mas o alinhamento final é RECUADO até o pico (não até onde parou
    # de avançar) — senão o score reportado fica desatualizado assim que a
    # extensão ultrapassa a região que realmente corresponde.
    cur_ea, cur_eb = ea, eb
    while cur_ea < len(intervals_a) and cur_eb < len(intervals_b):
        cur_ea, cur_eb = cur_ea + 1, cur_eb + 1
        score = score_of(sa, cur_ea, sb, cur_eb)
        if score < best_score - x_drop:
            break
        if score >= best_score:
            best_score = score
            best_bounds = (sa, cur_ea, sb, cur_eb)

    sa, ea, sb, eb = best_bounds

    # extensão à esquerda, mesma lógica de recuo até o pico
    cur_sa, cur_sb = sa, sb
    while cur_sa > 0 and cur_sb > 0:
        cur_sa, cur_sb = cur_sa - 1, cur_sb - 1
        score = score_of(cur_sa, ea, cur_sb, eb)
        if score < best_score - x_drop:
            break
        if score >= best_score:
            best_score = score
            best_bounds = (cur_sa, ea, cur_sb, eb)

    sa, ea, sb, eb = best_bounds
    return Alignment(sa, ea, sb, eb, transformation, best_score, 0.0)


def align_motifs(
    intervals_a: List[int],
    intervals_b: List[int],
    min_len: int = 4,
    max_len: int = 7,
    seed_threshold: float = 0.7,
    x_drop: float = 0.3,
) -> List[Alignment]:
    """Pipeline completo: gera candidatos em A, acha sementes em B, estende
    cada semente e remove sobreposições com estratégia gulosa (maior score
    primeiro). Retorna os alinhamentos finais ordenados pela posição em A."""
    candidates = sliding_windows(intervals_a, min_len, max_len)

    raw: List[Alignment] = []
    for cand in candidates:
        for start_b, end_b, transformation, seed_score in find_seeds(cand, intervals_b, seed_threshold):
            aln = extend_seed(
                intervals_a, intervals_b,
                cand.start, cand.start + cand.length,
                start_b, end_b,
                transformation, x_drop,
            )
            aln.seed_score = seed_score
            raw.append(aln)

    raw.sort(key=lambda a: a.score, reverse=True)
    used_a, used_b = set(), set()
    final: List[Alignment] = []
    for aln in raw:
        range_a = set(range(aln.start_a, aln.end_a))
        range_b = set(range(aln.start_b, aln.end_b))
        if range_a & used_a or range_b & used_b:
            continue
        used_a |= range_a
        used_b |= range_b
        final.append(aln)

    return sorted(final, key=lambda a: a.start_a)
