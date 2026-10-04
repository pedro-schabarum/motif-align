"""
representacao.py — Representação de cada voz (Seção 5.1.1, Equações 4 a 6).

`extrair_eventos` já está pronta: ela só lida com a API do music21, que não
é o que a banca vai perguntar. O exercício são as quatro funções seguintes.
Rode `pytest tests/test_representacao.py`.

Cada voz vira uma sequência de eventos e1..en. A representação S tem n-1
elementos; o k-ésimo é a tupla (delta, c, r):
  delta = grau(e[k+1]) - grau(e[k])        intervalo diatônico (passos na pauta)
  c     = midi(e[k+1]) - midi(e[k])        intervalo em semitons
  r     = duracao(e[k+1]) / duracao(e[k])  proporção rítmica (Fraction)

`grau` é o `diatonicNoteNum` do music21: conta linhas e espaços da pauta,
então dó4 -> ré4 dá 1, dó4 -> mi4 dá 2, e dó4 -> dó#4 dá 0. É exatamente a
"distância na pauta" que eu sugeri para definir delta no texto.
"""

from dataclasses import dataclass
from fractions import Fraction
from typing import List, Tuple

Elemento = Tuple[int, int, Fraction]  # (delta, c, r)


@dataclass(frozen=True)
class Evento:
    nome: str          # ex.: "F#4"
    midi: int          # ex.: 66
    grau: int          # diatonicNoteNum do music21
    duracao: Fraction  # em semínimas (quarterLength)
    compasso: int      # número do compasso
    posicao: Fraction  # tempo dentro do compasso, em semínimas


@dataclass
class SequenciaVoz:
    ancora: Evento          # primeira nota da voz (guarda a altura absoluta)
    elementos: List[Elemento]
    eventos: List[Evento]   # para traduzir índices em compasso/posição


def extrair_eventos(parte) -> List[Evento]:
    """Notas de uma parte do music21, na ordem, ignorando pausas e acordes.

    Notas ligadas (tie) aparecem como eventos separados; para os corais isso
    é raro e fica como refinamento para depois.
    """
    eventos = []
    # recurse() mantém cada nota dentro do seu compasso, então n.offset é a
    # posição no compasso (com flatten() seria a posição desde o início).
    for n in parte.recurse().notes:
        if not n.isNote:
            continue
        eventos.append(
            Evento(
                nome=n.nameWithOctave,
                midi=n.pitch.midi,
                grau=n.pitch.diatonicNoteNum,
                duracao=Fraction(n.quarterLength),
                compasso=n.measureNumber,
                posicao=Fraction(n.offset),
            )
        )
    return eventos


def representar(eventos: List[Evento]) -> SequenciaVoz:
    """Equação 4. Monta a SequenciaVoz a partir dos eventos.

    Com n eventos, `elementos` deve ter n-1 tuplas. Use Fraction para r,
    não float, para que 1/3 e 2/3 se comparem sem erro de arredondamento.
    """
    raise NotImplementedError


def inversao(elementos: List[Elemento]) -> List[Elemento]:
    """Equação 5: (delta, c, r) -> (-delta, -c, r).

    DECISÃO EM ABERTO: no texto, a inversão pertinente é a tonal, que
    espelha graus. Na inversão tonal, uma terça maior pode virar menor,
    então c não é simplesmente -c. Por isso os testes só conferem delta e r.
    Implemente como a Equação 5 por enquanto; quando decidirmos o que fazer
    com c, ajustamos aqui e no texto.
    """
    raise NotImplementedError


def retrogradacao(elementos: List[Elemento]) -> List[Elemento]:
    """Equação 6: percorre de trás para a frente, troca o sinal de delta e
    de c e usa o inverso de r.

    Exemplo do texto: dó-ré-mi-sol tem delta (1, 1, 2); o retrógrado,
    sol-mi-ré-dó, tem delta (-2, -1, -1).
    """
    raise NotImplementedError


def intervalo_transposicao(a: SequenciaVoz, b: SequenciaVoz) -> int:
    """Diferença em semitons entre as âncoras (b menos a).

    Para BWV 244.15 (âncora fá#4) e 244.62 (âncora mi4), dá -2.
    """
    raise NotImplementedError
