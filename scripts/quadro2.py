"""Reproduz o Quadro 2 do TCC (BWV 244.15 x 244.62, sopranos) com a Eq. 7 e extensão com gaps + X-drop."""
import math, sys
from music21 import corpus

A_, B_, G_, R_ = 2, 1, 1, 1   # alfa, beta, gama, rho
GAP, X, K = 2, 5, 4

def voz(bwv, parte=0):
    s = corpus.parse(f'bach/bwv{bwv}').parts[parte].stripTies()
    ns = [n for n in s.recurse().notes if n.isNote]
    return ns

def rep(ns):
    out = []
    for a, b in zip(ns, ns[1:]):
        d = b.pitch.diatonicNoteNum - a.pitch.diatonicNoteNum
        c = b.pitch.midi - a.pitch.midi
        r = b.quarterLength / a.quarterLength
        out.append((d, c, r))
    return out

def s(x, y):
    sc = A_ if x[0] == y[0] else -B_
    if x[0] == y[0] and x[1] == y[1]:
        sc += G_
    sc -= R_ * abs(math.log2(x[2] / y[2]))
    return sc

def xdrop(Q, Z):
    """Extensão com gaps a partir de (0,0), recorrência da Eq. 1 com poda X-drop."""
    NEG = float('-inf')
    H = {(0, 0): 0.0}; back = {}
    hmax, best = 0.0, (0, 0)
    for p in range(len(Q) + 1):
        alive = False
        for q in range(len(Z) + 1):
            if (p, q) == (0, 0):
                alive = True; continue
            cands = []
            if p > 0 and q > 0 and H.get((p-1, q-1), NEG) > NEG:
                cands.append((H[(p-1, q-1)] + s(Q[p-1], Z[q-1]), 'D'))
            if p > 0 and H.get((p-1, q), NEG) > NEG:
                cands.append((H[(p-1, q)] - GAP, 'U'))   # gap em Z
            if q > 0 and H.get((p, q-1), NEG) > NEG:
                cands.append((H[(p, q-1)] - GAP, 'L'))   # gap em Q
            if not cands:
                H[(p, q)] = NEG; continue
            v, m = max(cands)
            if v < hmax - X:
                H[(p, q)] = NEG; continue
            H[(p, q)] = v; back[(p, q)] = m; alive = True
            if v > hmax:
                hmax, best = v, (p, q)
        if not alive:
            break
    # traceback
    path = []; cur = best
    while cur != (0, 0):
        m = back[cur]; path.append((m, cur))
        p, q = cur
        cur = (p-1, q-1) if m == 'D' else (p-1, q) if m == 'U' else (p, q-1)
    return hmax, best, path[::-1]

if __name__ == '__main__':
    na, nb = voz('244.15'), voz('244.62')
    SA, SB = rep(na), rep(nb)
    print('notas:', len(na), len(nb))
    print('início A:', na[0].nameWithOctave, ' B:', nb[0].nameWithOctave)
    print('δ A:', [x[0] for x in SA[:16]])
    print('δ B:', [x[0] for x in SB[:16]])
    seed = sum(s(SA[t], SB[t]) for t in range(K))
    print('escore da semente:', seed)
    h, best, path = xdrop(SA[K:], SB[K:])
    print('extensão:', h, 'até', best, '-> total', seed + h)
    ia, ib = K + best[0], K + best[1]
    print(f'intervalos alinhados: A {ia}, B {ib}  => notas A {ia+1}, B {ib+1}')
    run = seed
    for m, (p, q) in path:
        if m == 'D':
            x, y = SA[K+p-1], SB[K+q-1]; run += s(x, y)
            print(f'  D A{K+p:>2} {x} | B{K+q:>2} {y}  s={s(x,y):+.2f} acum={run:.2f}')
        else:
            run -= GAP
            print(f'  {m} gap  acum={run:.2f}')
    # diferença de altura por par alinhado (para rótulo)
