"""
test_synthetic.py — Validação com dados sintéticos (transformação conhecida)

Gera um motivo-base e suas transformações clássicas, embutidas em contexto de
"ruído" (intervalos aleatórios), e verifica se o algoritmo:
  (a) encontra o motivo transformado com alta similaridade;
  (b) identifica corretamente o tipo de transformação;
  (c) NÃO reporta correspondência forte entre trechos sem relação real
      (controle de falso positivo).
"""

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from motif_align.core import (
    TRANSFORMATIONS,
    align_motifs,
    best_transformation_match,
)

random.seed(42)

MOTIF = [2, 2, 1, -2, -1]  # motivo-base sintético (5 intervalos)


def ruido(n: int) -> list:
    return [random.choice([-4, -3, -2, -1, 1, 2, 3, 4]) for _ in range(n)]


def test_transformacoes_sao_reconhecidas_isoladamente():
    """Cada transformação clássica aplicada ao motivo-base deve ser
    identificada corretamente contra o motivo original."""
    for nome_esperado, transform_fn in TRANSFORMATIONS.items():
        transformado = transform_fn(MOTIF)
        nome_encontrado, score = best_transformation_match(MOTIF, transformado)
        assert nome_encontrado == nome_esperado, (
            f"esperado {nome_esperado}, encontrado {nome_encontrado}"
        )
        assert score == 1.0, f"transformação exata deveria ter score 1.0, teve {score}"


def test_encontra_motivo_transposto_em_contexto_com_ruido():
    """O motivo (via 'transposição', i.e. mesma sequência de intervalos)
    embutido em ruído deve ser encontrado pelo pipeline completo."""
    versao_a = ruido(8) + MOTIF + ruido(8)
    versao_b = ruido(6) + MOTIF + ruido(10)  # mesmo motivo, outro contexto/posição

    alinhamentos = align_motifs(versao_a, versao_b, min_len=4, max_len=5, seed_threshold=0.7)

    assert len(alinhamentos) >= 1, "deveria encontrar pelo menos um alinhamento"
    melhor = max(alinhamentos, key=lambda a: a.score)
    assert melhor.score >= 0.8
    assert melhor.transformation == "transposicao"


def test_encontra_motivo_invertido_em_contexto_com_ruido():
    versao_a = ruido(8) + MOTIF + ruido(8)
    versao_b = ruido(6) + [-i for i in MOTIF] + ruido(10)

    alinhamentos = align_motifs(versao_a, versao_b, min_len=4, max_len=5, seed_threshold=0.7)

    assert len(alinhamentos) >= 1
    melhor = max(alinhamentos, key=lambda a: a.score)
    assert melhor.transformation == "inversao"


def test_extensao_encontra_fronteira_maior_que_a_semente():
    """Regressão do bug encontrado nos testes preliminares: a extensão devia
    aumentar a região correspondente além da semente mínima, não só reportar
    o tamanho da janela original."""
    motivo_longo = MOTIF + [1, 1, -3, 2]  # motivo maior que min_len
    versao_a = ruido(5) + motivo_longo + ruido(5)
    versao_b = ruido(3) + motivo_longo + ruido(7)

    alinhamentos = align_motifs(versao_a, versao_b, min_len=4, max_len=5, seed_threshold=0.7)
    melhor = max(alinhamentos, key=lambda a: a.score)

    tamanho_encontrado = melhor.end_a - melhor.start_a
    assert tamanho_encontrado > 5, (
        f"extensão deveria superar a janela mínima de busca, achou {tamanho_encontrado}"
    )


def test_nao_reporta_correspondencia_forte_entre_ruido_puro():
    """Controle de falso positivo: dois trechos de ruído aleatório não
    relacionado não devem gerar alinhamento de alta confiança."""
    versao_a = ruido(30)
    versao_b = ruido(30)

    alinhamentos = align_motifs(versao_a, versao_b, min_len=5, max_len=7, seed_threshold=0.85)

    scores_altos = [a for a in alinhamentos if a.score >= 0.9]
    assert len(scores_altos) == 0, (
        "ruído puro não deveria gerar alinhamentos de score >= 0.9"
    )


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__, "-v"]))
