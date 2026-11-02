"""Compara dois modelos nulos para o teste de significância (Seção 5.1.4):
(a) permutação i.i.d. da sequência comparada (alternativa descartada no texto);
(b) sopranos de outros corais, sem relação com a consulta (preservam o estilo).
Forma Id apenas, k=4, máscara de baixa complexidade, mesmos pesos ilustrativos do Quadro 2."""
import random, math, sys
from music21 import corpus
import quadro2 as q

K = 4

def low_complex(w):
    return len(set(w)) == 1 and abs(w[0]) <= 1

def busca_max(S, T):
    idx = {}
    for i in range(len(S) - K + 1):
        w = tuple(x[0] for x in S[i:i+K])
        if not low_complex(w):
            idx.setdefault(w, []).append(i)
    best = 0.0
    for j in range(len(T) - K + 1):
        w = tuple(x[0] for x in T[j:j+K])
        for i in idx.get(w, []):
            seed = sum(q.s(S[i+t], T[j+t]) for t in range(K))
            hr = q.xdrop(S[i+K:], T[j+K:])[0]
            hl = q.xdrop(S[:i][::-1], T[:j][::-1])[0]
            best = max(best, seed + hr + hl)
    return best

def soprano_rep(path):
    try:
        sc = corpus.parse(path)
        if len(sc.parts) != 4:
            return None
        ns = [n for n in sc.parts[0].stripTies().recurse().notes if n.isNote]
        return q.rep(ns) if len(ns) > 10 else None
    except Exception:
        return None

if __name__ == '__main__':
    random.seed(1)
    SA = q.rep(q.voz('244.15'))
    SB = q.rep(q.voz('244.62'))
    print('escore real 244.15 x 244.62:', round(busca_max(SA, SB), 2))
    # (a) iid
    a = []
    for _ in range(300):
        T = SB[:]; random.shuffle(T); a.append(busca_max(SA, T))
    # (b) outros corais (exclui a família do coral da Paixão pelo início do soprano)
    paths = [p for p in corpus.getComposer('bach') if str(p).endswith(('.mxl', '.xml', '.musicxml'))]
    random.shuffle(paths)
    head = tuple(x[0] for x in SA[:6])
    b = []
    for p in paths:
        T = soprano_rep(p)
        if T is None or tuple(x[0] for x in T[:6]) == head:
            continue
        b.append(busca_max(SA, T))
        if len(b) >= 300:
            break
    for nome, v in (('iid', a), ('outros corais', b)):
        v = sorted(v)
        pct = lambda f: v[min(len(v)-1, int(f*len(v)))]
        print(f'{nome:14s} n={len(v)} mediana={pct(.5):.2f} p95={pct(.95):.2f} p99={pct(.99):.2f} max={v[-1]:.2f}')
