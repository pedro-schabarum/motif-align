"""melhor_alinhamento.py — Alinhamentos do par BWV 244.15 x BWV 244.62 (sopranos), na ordem do Quadro 3.

Reproduz os números citados no Quadro 2 e na Seção 5.1.4 do TCC:

  - a extensão a partir da primeira semente (hit na posição 1 das duas versões) para
    no escore 31,6, cobrindo 17 e 15 notas, porque o X-drop (X = 5) a interrompe no
    trecho em que as melodias divergem;
  - o hit na posição 14 de BWV 244.15 e 16 de BWV 244.62, estendido nas duas direções,
    cobre as duas melodias inteiras (42 e 45 notas), com escore 95,0;
  - os demais alinhamentos encontrados no par têm escore de até 17,0.

Segue a função Busca do Quadro 3: os hits são percorridos na ordem da versão comparada,
e um hit contido num alinhamento já encontrado não é estendido de novo. Forma Id apenas,
k = 4, máscara de baixa complexidade e pesos ilustrativos do Quadro 2 (quadro2.py).

Uso:
    python scripts/melhor_alinhamento.py
"""

import quadro2 as q
import nulo

K = 4


def estende(SA, SB, i, j):
    """Escore, pares de intervalos alinhados e trechos cobertos a partir do hit (i, j)."""
    hr, br, pr = q.xdrop(SA[i + K:], SB[j + K:])
    hl, bl, pl = q.xdrop(SA[:i][::-1], SB[:j][::-1])
    pares = {(i + t, j + t) for t in range(K)}
    for m, (p, r) in pr:
        if m == 'D':
            pares.add((i + K + p - 1, j + K + r - 1))
    for m, (p, r) in pl:
        if m == 'D':
            pares.add((i - p, j - r))
    escore = sum(q.s(SA[i + t], SB[j + t]) for t in range(K)) + hr + hl
    return escore, pares, (i - bl[0], i + K + br[0]), (j - bl[1], j + K + br[1])


def main():
    SA = q.rep(q.voz('244.15'))
    SB = q.rep(q.voz('244.62'))
    indice = {}
    for i in range(len(SA) - K + 1):
        w = tuple(x[0] for x in SA[i:i + K])
        if not nulo.low_complex(w):
            indice.setdefault(w, []).append(i)
    R = []
    for j in range(len(SB) - K + 1):
        w = tuple(x[0] for x in SB[j:j + K])
        for i in indice.get(w, []):
            if any((i, j) in a[1] for a in R):
                continue
            a = estende(SA, SB, i, j)
            R.append(a)
            (a0, a1), (b0, b1) = a[2], a[3]
            print(f'hit {i + 1:>2} x {j + 1:>2}: escore {a[0]:6.2f}  '
                  f'notas {a0 + 1}-{a1 + 1} de BWV 244.15 ({a1 - a0 + 1}), '
                  f'{b0 + 1}-{b1 + 1} de BWV 244.62 ({b1 - b0 + 1})')


if __name__ == '__main__':
    main()
