"""
Testes de sementes.py (Seção 5.1.2). Tamanho de semente k = 4, como no
Quadro 2 do texto.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from motif_align.sementes import baixa_complexidade, buscar_hits, construir_indice

K = 4


# --- Passo 8: máscara ----------------------------------------------------------

def test_mascara_notas_repetidas_e_escalas():
    assert baixa_complexidade((0, 0, 0, 0))
    assert baixa_complexidade((1, 1, 1, 1))
    assert baixa_complexidade((-1, -1, -1, -1))


def test_nao_mascara_o_que_tem_desenho():
    assert not baixa_complexidade((1, 1, 2, 1))
    assert not baixa_complexidade((2, 2, 2, 2))  # arpejo, não escala
    assert not baixa_complexidade((1, -1, 1, -1))
    assert not baixa_complexidade((3, -1, -1, -1))  # semente do Quadro 2


# --- Passo 9: índice -----------------------------------------------------------

def test_indice_tem_as_tres_formas():
    I = construir_indice([3, -1, 2, -2], K)
    assert I[(3, -1, 2, -2)] == [(0, "Id")]
    assert I[(-3, 1, -2, 2)] == [(0, "Inv")]
    assert I[(2, -2, 1, -3)] == [(0, "Ret")]
    assert len(I) == 3


def test_indice_pula_baixa_complexidade():
    # Janelas: (1,1,1,1) mascarada, (1,1,1,3) e (1,1,3,-2) indexadas.
    I = construir_indice([1, 1, 1, 1, 3, -2], K)
    assert (1, 1, 1, 1) not in I
    assert (-1, -1, -1, -1) not in I  # nem as formas dela
    assert I[(1, 1, 1, 3)] == [(1, "Id")]
    assert I[(1, 1, 3, -2)] == [(2, "Id")]


def test_mesma_semente_em_dois_lugares():
    I = construir_indice([3, -1, 2, -2, 0, 3, -1, 2, -2], K)
    assert [p for p, f in I[(3, -1, 2, -2)] if f == "Id"] == [0, 5]


# --- Passo 10: busca -----------------------------------------------------------

def test_hit_identico():
    I = construir_indice([5, 3, -1, 2, -2, 5], K)
    assert buscar_hits(I, [0, 0, 3, -1, 2, -2], K) == [(1, 2, "Id")]


def test_hit_invertido_e_retrogradado():
    consulta = [3, -1, 2, -2]
    I = construir_indice(consulta, K)
    b = [0, 9, -3, 1, -2, 2, 9, 2, -2, 1, -3]
    #          ^ inversão em j=2      ^ retrógrado em j=7
    assert buscar_hits(I, b, K) == [(0, 2, "Inv"), (0, 7, "Ret")]


def test_sem_hits():
    I = construir_indice([3, -1, 2, -2], K)
    assert buscar_hits(I, [1, 2, 3, 4, 5, 6], K) == []


def test_sopranos_do_quadro_2():
    # Semente w1 = (3, -1, -1, -1) do 244.15 tem hit na posição 0 do 244.62.
    da = [3, -1, -1, -1, -1, 1, 4, 1, 0, -1]
    db = [3, -1, -1, -1, -1, 1, 4, 1, -1, 1]
    hits = buscar_hits(construir_indice(da, K), db, K)
    assert (0, 0, "Id") in hits
