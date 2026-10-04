"""
sementes.py — Sementes, máscara de baixa complexidade e índice (Seção 5.1.2).

A semente usa só a componente delta (intervalo diatônico) da representação.
Rode `pytest tests/test_sementes.py`.

O índice é um dicionário que leva cada semente (uma tupla de k deltas) à
lista de lugares onde ela aparece na versão de consulta, como pares
(posicao, forma). A forma diz sob qual transformação a semente foi indexada:
  "Id"   a própria semente
  "Inv"  a semente invertida (sinais trocados)
  "Ret"  a semente retrogradada (ordem invertida e sinais trocados)

Assim, ao varrer a outra versão, basta olhar cada janela de k deltas no
dicionário (custo esperado constante) para saber se há um hit e de que tipo.
"""

from typing import Dict, List, Sequence, Tuple

Semente = Tuple[int, ...]
Indice = Dict[Semente, List[Tuple[int, str]]]


def baixa_complexidade(semente: Semente) -> bool:
    """Critério inicial do texto: todos os passos iguais e |delta| <= 1.

    Mascara notas repetidas (0, 0, 0, 0) e fragmentos de escala numa única
    direção (1, 1, 1, 1) ou (-1, -1, -1, -1). Não mascara (1, 1, 2, 1) nem
    (2, 2, 2, 2).
    """
    raise NotImplementedError


def construir_indice(deltas: Sequence[int], k: int) -> Indice:
    """Indexa todas as janelas de tamanho k de `deltas`, cada uma nas três
    formas, pulando as de baixa complexidade.

    A posição registrada é sempre o início da janela na sequência original,
    mesmo para as formas Inv e Ret.
    """
    raise NotImplementedError


def buscar_hits(indice: Indice, deltas_b: Sequence[int], k: int) -> List[Tuple[int, int, str]]:
    """Varre as janelas de tamanho k de `deltas_b` e devolve todos os hits
    como (i, j, forma): i é a posição na versão de consulta (do índice),
    j a posição em b. Ordem: por j crescente; dentro do mesmo j, na ordem
    em que aparecem na lista do índice.
    """
    raise NotImplementedError
