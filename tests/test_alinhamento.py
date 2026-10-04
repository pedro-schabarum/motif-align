"""
Testes de alinhamento.py. Os números vêm da Figura 2 e da Seção 3.2 do texto:
A = ACGT, B = AGT, acerto +1, erro -1, espaço g = 2.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from motif_align.alinhamento import (
    needleman_wunsch,
    smith_waterman,
    traceback_global,
    traceback_local,
)


def s(x, y):
    return 1 if x == y else -1


G = 2

# Figura 2 transposta (aqui ACGT fica nas linhas, AGT nas colunas).
MATRIZ_FIGURA_2 = [
    [0, -2, -4, -6],
    [-2, 1, -1, -3],
    [-4, -1, 0, -2],
    [-6, -3, 0, -1],
    [-8, -5, -2, 1],
]


# --- Passo 1: Needleman-Wunsch ------------------------------------------------

def test_nw_bordas():
    F = needleman_wunsch("ACGT", "AGT", s, G)
    assert [linha[0] for linha in F] == [0, -2, -4, -6, -8]
    assert F[0] == [0, -2, -4, -6]


def test_nw_matriz_da_figura_2():
    assert needleman_wunsch("ACGT", "AGT", s, G) == MATRIZ_FIGURA_2


def test_nw_celula_destacada_no_texto():
    # Célula G x G: diagonal -1 + 1 = 0; de cima/esquerda dão -5 e -2. Vence 0.
    F = needleman_wunsch("ACGT", "AGT", s, G)
    assert F[3][2] == 0


def test_nw_pontuacao_final_e_1():
    assert needleman_wunsch("ACGT", "AGT", s, G)[-1][-1] == 1


def test_nw_sequencias_iguais_pontuam_o_comprimento():
    assert needleman_wunsch("BACH", "BACH", s, G)[-1][-1] == 4


# --- Passo 2: traceback global -------------------------------------------------

def test_traceback_da_figura_2():
    F = needleman_wunsch("ACGT", "AGT", s, G)
    assert traceback_global("ACGT", "AGT", s, G, F) == [
        ("A", "A"),
        ("C", None),
        ("G", "G"),
        ("T", "T"),
    ]


def test_traceback_reproduz_a_pontuacao():
    # Somando os pares do alinhamento, tem que dar F[-1][-1].
    a, b = "GATTACA", "GCATGCA"
    F = needleman_wunsch(a, b, s, G)
    pares = traceback_global(a, b, s, G, F)
    total = sum(-G if x is None or y is None else s(x, y) for x, y in pares)
    assert total == F[-1][-1]
    assert "".join(x for x, _ in pares if x is not None) == a
    assert "".join(y for _, y in pares if y is not None) == b


# --- Passo 3: Smith-Waterman ---------------------------------------------------

def test_sw_nunca_negativo():
    H, _, _ = smith_waterman("TTACGTAA", "GGAGTCC", s, G)
    assert all(v >= 0 for linha in H for v in linha)


def test_sw_bordas_zeradas():
    H, _, _ = smith_waterman("ACGT", "AGT", s, G)
    assert H[0] == [0, 0, 0, 0]
    assert [linha[0] for linha in H] == [0, 0, 0, 0, 0]


def test_sw_acha_o_trecho_comum():
    H, melhor, celula = smith_waterman("XXACGTYY", "ZZACGTWW", s, G)
    assert melhor == 4
    assert celula == (6, 6)


def test_sw_supera_nw_quando_so_um_trecho_corresponde():
    a, b = "XXACGTYY", "ZZACGTWW"
    _, melhor_local, _ = smith_waterman(a, b, s, G)
    assert melhor_local > needleman_wunsch(a, b, s, G)[-1][-1]


# --- Passo 4: traceback local --------------------------------------------------

def test_traceback_local_devolve_o_trecho():
    a, b = "XXACGTYY", "ZZACGTWW"
    H, _, celula = smith_waterman(a, b, s, G)
    ia, fa, ib, fb = traceback_local(a, b, s, G, H, celula)
    assert a[ia:fa] == "ACGT"
    assert b[ib:fb] == "ACGT"


def test_traceback_local_com_espaco():
    # "ACGGT" contra "ACGT": um G a mais, absorvido por um espaço.
    a, b = "XXACGGTYY", "ZZACGTWW"
    s2 = lambda x, y: 2 if x == y else -1
    H, _, celula = smith_waterman(a, b, s2, 1)
    ia, fa, ib, fb = traceback_local(a, b, s2, 1, H, celula)
    assert a[ia:fa] == "ACGGT"
    assert b[ib:fb] == "ACGT"


def test_funciona_com_listas_de_intervalos():
    # As funções não podem depender de strings.
    a = [3, -1, -1, 0, 4]
    b = [3, -1, -1, 4]
    s2 = lambda x, y: 2 if x == y else -1
    H, melhor, celula = smith_waterman(a, b, s2, 1)
    assert melhor == 7  # 3 acertos (6) - espaço (1) + 1 acerto (2)
    assert traceback_local(a, b, s2, 1, H, celula) == (0, 5, 0, 4)
