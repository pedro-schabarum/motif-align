import random, sys
from collections import defaultdict
import quadro2 as q, nulo

def ae_shuffle(S, rng):
    """Embaralha triplas preservando a contagem de pares consecutivos de δ (Altschul-Erickson, via trilha euleriana)."""
    # vértices = δ; aresta k: δ_k -> δ_{k+1}, rotulada com S[k+1]
    d = [x[0] for x in S]
    edges = defaultdict(list)
    for k in range(len(S)-1):
        edges[d[k]].append(S[k+1])
    last = d[-1]
    # árvore de última saída (Wilson/AE): para cada vértice != last, escolhe aleatoriamente a última aresta
    while True:
        lastedge = {}
        for v, es in edges.items():
            if v != last and es:
                lastedge[v] = rng.randrange(len(es))
        # verifica que as últimas arestas levam a 'last'
        ok = True
        for v in lastedge:
            seen=set(); u=v
            while u != last:
                if u in seen: ok=False; break
                seen.add(u); u = edges[u][lastedge[u]][0]
            if not ok: break
        if ok: break
    order = {}
    for v, es in edges.items():
        idx = list(range(len(es)))
        if v in lastedge:
            idx.remove(lastedge[v]); rng.shuffle(idx); idx.append(lastedge[v])
        else:
            rng.shuffle(idx)
        order[v] = [es[i] for i in idx]
    out = [S[0]]; u = d[0]
    while order.get(u):
        x = order[u].pop(0); out.append(x); u = x[0]
    assert len(out) == len(S)
    return out

rng = random.Random(2)
SA = q.rep(q.voz('244.15')); SB = q.rep(q.voz('244.62'))
v = sorted(nulo.busca_max(SA, ae_shuffle(SB, rng)) for _ in range(300))
p = lambda f: v[min(len(v)-1,int(f*len(v)))]
print(f'AE             n=300 mediana={p(.5):.2f} p95={p(.95):.2f} p99={p(.99):.2f} max={v[-1]:.2f}')
