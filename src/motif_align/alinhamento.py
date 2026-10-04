"""
alinhamento.py — Needleman-Wunsch e Smith-Waterman (Capítulo 3 do TCC).

Exercício: implemente as quatro funções marcadas com NotImplementedError,
nesta ordem, rodando `pytest tests/test_alinhamento.py` a cada passo.

As funções são genéricas: `a` e `b` podem ser strings ("ACGT"), listas de
inteiros (intervalos) ou qualquer sequência; quem decide o que é acerto ou
erro é a função de pontuação `s`.

Convenções usadas nos testes:
  - a matriz tem len(a)+1 linhas e len(b)+1 colunas;
    a linha i corresponde a a[i-1], a coluna j a b[j-1];
  - g é a penalidade por espaço (positiva) e é SUBTRAÍDA;
  - no traceback, em caso de empate, prefira: diagonal, depois cima
    (espaço em b), depois esquerda (espaço em a).

Atenção: a Figura 2 do texto desenha A nas colunas e B nas linhas.
Aqui é o contrário (a nas linhas), então a matriz do teste é a da figura
transposta.
"""

from typing import Callable, List, Optional, Sequence, Tuple, TypeVar

T = TypeVar("T")
Pontuacao = Callable[[T, T], float]
Matriz = List[List[float]]
Par = Tuple[Optional[T], Optional[T]]


def needleman_wunsch(a: Sequence[T], b: Sequence[T], s: Pontuacao, g: float) -> Matriz:
    """Alinhamento global (Equação 1).

    F[i][0] = -i*g, F[0][j] = -j*g e, para i, j >= 1:
        F[i][j] = max(F[i-1][j-1] + s(a[i-1], b[j-1]),
                      F[i-1][j]   - g,
                      F[i][j-1]   - g)

    Retorna a matriz F inteira. A pontuação do alinhamento ótimo é F[-1][-1].
    """
    raise NotImplementedError


def traceback_global(
    a: Sequence[T], b: Sequence[T], s: Pontuacao, g: float, F: Matriz
) -> List[Par]:
    """Reconstrói o alinhamento ótimo a partir de F, do canto inferior
    direito até F[0][0].

    Retorna a lista de pares na ordem das sequências (do início ao fim):
      (a[i], b[j])  par de elementos (passo diagonal)
      (a[i], None)  espaço em b      (passo para cima)
      (None, b[j])  espaço em a      (passo para a esquerda)

    Dica: em cada célula, descubra qual das três vizinhas gerou o valor,
    refazendo a conta da Equação 1.
    """
    raise NotImplementedError


def smith_waterman(
    a: Sequence[T], b: Sequence[T], s: Pontuacao, g: float
) -> Tuple[Matriz, float, Tuple[int, int]]:
    """Alinhamento local (Equação 2).

    Igual a Needleman-Wunsch, com duas diferenças:
      - primeira linha e primeira coluna são zero;
      - cada célula tem piso zero: H[i][j] = max(0, ...).

    Retorna (H, maior_escore, (i, j)), em que (i, j) é a célula do maior
    escore. Se houver empate, fique com a primeira encontrada percorrendo
    linha por linha, da esquerda para a direita (use > e não >=).
    """
    raise NotImplementedError


def traceback_local(
    a: Sequence[T],
    b: Sequence[T],
    s: Pontuacao,
    g: float,
    H: Matriz,
    celula: Tuple[int, int],
) -> Tuple[int, int, int, int]:
    """Volta da célula de maior escore até encontrar uma célula com zero.

    Retorna (ini_a, fim_a, ini_b, fim_b) como índices de fatia do Python:
    o trecho alinhado é a[ini_a:fim_a] e b[ini_b:fim_b] (fim exclusivo).
    Use a mesma regra de empate de traceback_global.
    """
    raise NotImplementedError
