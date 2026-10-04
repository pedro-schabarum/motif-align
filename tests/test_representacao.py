"""
Testes de representacao.py. Os dois últimos usam os sopranos de BWV 244.15 e
BWV 244.62 do corpus do music21, o mesmo par do Quadro 2 do texto.
"""

import sys
from fractions import Fraction
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from motif_align.representacao import (
    Evento,
    extrair_eventos,
    intervalo_transposicao,
    inversao,
    representar,
    retrogradacao,
)


def ev(nome, midi, grau, dur):
    return Evento(nome, midi, grau, Fraction(dur), 1, Fraction(0))


# dó4 (semínima), ré4 (semínima), mi4 (mínima), sol4 (semínima)
DO_RE_MI_SOL = [
    ev("C4", 60, 29, 1),
    ev("D4", 62, 30, 1),
    ev("E4", 64, 31, 2),
    ev("G4", 67, 33, 1),
]


# --- Passo 5: representação ---------------------------------------------------

def test_representar_do_re_mi_sol():
    v = representar(DO_RE_MI_SOL)
    assert v.elementos == [
        (1, 2, Fraction(1)),
        (1, 2, Fraction(2)),
        (2, 3, Fraction(1, 2)),
    ]
    assert v.ancora.nome == "C4"
    assert len(v.eventos) == 4


def test_transposicao_nao_muda_os_intervalos():
    # A mesma melodia uma segunda maior acima (ré-mi-fá#-lá).
    transposta = [
        ev("D4", 62, 30, 1),
        ev("E4", 64, 31, 1),
        ev("F#4", 66, 32, 2),
        ev("A4", 69, 34, 1),
    ]
    a, b = representar(DO_RE_MI_SOL), representar(transposta)
    assert a.elementos == b.elementos
    assert intervalo_transposicao(a, b) == 2


# --- Passo 6: inversão e retrogradação -----------------------------------------

def test_inversao_troca_o_sinal_de_delta_e_mantem_r():
    S = representar(DO_RE_MI_SOL).elementos
    inv = inversao(S)
    # Só delta e r: o que fazer com c ainda é decisão em aberto (ver docstring).
    assert [(d, r) for d, _, r in inv] == [(-1, 1), (-1, 2), (-2, Fraction(1, 2))]


def test_retrogradacao_exemplo_do_texto():
    S = representar(DO_RE_MI_SOL).elementos
    ret = retrogradacao(S)
    assert [d for d, _, _ in ret] == [-2, -1, -1]  # e não (2, 1, 1)
    assert [c for _, c, _ in ret] == [-3, -2, -2]
    # Durações 1, 1, 2, 1 lidas de trás para a frente: 1, 2, 1, 1.
    assert [r for _, _, r in ret] == [Fraction(2), Fraction(1, 2), Fraction(1)]


def test_retrogradacao_bate_com_a_melodia_tocada_de_tras_para_frente():
    # A prova de verdade: representar a melodia invertida no tempo tem que dar
    # o mesmo que aplicar retrogradacao() à representação original.
    S = representar(DO_RE_MI_SOL).elementos
    assert retrogradacao(S) == representar(list(reversed(DO_RE_MI_SOL))).elementos


def test_aplicar_duas_vezes_volta_ao_original():
    S = representar(DO_RE_MI_SOL).elementos
    assert retrogradacao(retrogradacao(S)) == S
    assert inversao(inversao(S)) == S


# --- Passo 7: dados reais -------------------------------------------------------

@pytest.fixture(scope="module")
def sopranos():
    corpus = pytest.importorskip("music21.corpus")
    a = representar(extrair_eventos(corpus.parse("bach/bwv244.15").parts[0]))
    b = representar(extrair_eventos(corpus.parse("bach/bwv244.62").parts[0]))
    return a, b


def test_sopranos_do_quadro_2(sopranos):
    a, b = sopranos
    inicio = [3, -1, -1, -1, -1, 1, 4, 1]
    assert [d for d, _, _ in a.elementos[:8]] == inicio
    assert [d for d, _, _ in b.elementos[:8]] == inicio
    assert a.ancora.nome == "F#4" and b.ancora.nome == "E4"
    assert intervalo_transposicao(a, b) == -2
    # Na 9ª posição o 244.15 repete a nota (delta 0) e o 244.62 desce.
    assert a.elementos[8][0] == 0 and b.elementos[8][0] == -1


def test_smith_waterman_alinha_os_dois_sopranos_inteiros(sopranos):
    # O "gabarito parcial" da Seção 6.3: um soprano corresponde ao outro do
    # início ao fim. Este teste junta o passo 3 com o passo 5.
    from motif_align.alinhamento import smith_waterman, traceback_local

    a, b = sopranos
    da = [d for d, _, _ in a.elementos]
    db = [d for d, _, _ in b.elementos]
    s = lambda x, y: 2 if x == y else -1
    H, _, celula = smith_waterman(da, db, s, 2)
    assert traceback_local(da, db, s, 2, H, celula) == (0, len(da), 0, len(db))
