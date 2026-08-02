"""
test_real_piece.py — Validação com material real (corpus embutido do music21)

Usa a linha de soprano do coral de Bach BWV 66.6 como "versão A". A "versão B"
é construída aplicando uma transformação conhecida a um trecho real da peça,
mantendo o restante do material real como contexto ao redor — testando se o
algoritmo encontra o motivo transformado em meio a material musical genuíno,
não apenas contra ruído sintético.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from motif_align.core import extract_notes, interval_sequence, align_motifs, TRANSFORMATIONS


def carregar_intervalos_soprano():
    from music21 import corpus

    peca = corpus.parse("bach/bwv66.6")
    soprano = peca.parts[0]  # linha de soprano
    notas = extract_notes(soprano)
    assert len(notas) > 15, "peça carregada parece curta demais — checar corpus"
    return interval_sequence(notas)


def test_carrega_corpus_real():
    intervalos = carregar_intervalos_soprano()
    assert len(intervalos) > 10


def test_encontra_trecho_identico_dentro_da_propria_peca():
    """Versão B = a própria peça (transposição trivial / identidade).
    Deve encontrar alinhamento perfeito cobrindo praticamente toda a peça."""
    intervalos = carregar_intervalos_soprano()
    alinhamentos = align_motifs(intervalos, list(intervalos), min_len=5, max_len=6, seed_threshold=0.8)

    assert len(alinhamentos) >= 1
    cobertura = sum(a.end_a - a.start_a for a in alinhamentos)
    assert cobertura / len(intervalos) > 0.5, "deveria cobrir boa parte da peça (é a própria peça)"


def test_encontra_transformacao_conhecida_em_trecho_real():
    """Pega um trecho real de ~6 notas do meio da peça, aplica inversão, e
    embute de volta numa 'versão B' junto com o resto do material real
    (deslocado). O alinhamento deve achar essa correspondência e classificar
    corretamente como inversão."""
    intervalos = carregar_intervalos_soprano()

    meio = len(intervalos) // 2
    trecho_real = intervalos[meio:meio + 6]
    trecho_invertido = TRANSFORMATIONS["inversao"](trecho_real)

    versao_a = intervalos
    versao_b = intervalos[:meio] + trecho_invertido + intervalos[meio + 6:]

    alinhamentos = align_motifs(versao_a, versao_b, min_len=4, max_len=6, seed_threshold=0.75)

    candidatos_na_regiao = [
        a for a in alinhamentos
        if a.start_a <= meio < a.end_a or a.start_a <= meio + 6 <= a.end_a
    ]
    assert len(candidatos_na_regiao) >= 1, "deveria encontrar alinhamento cobrindo a região alterada"
    assert any(a.transformation == "inversao" for a in candidatos_na_regiao)


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__, "-v"]))
