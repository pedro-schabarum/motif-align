"""
frequencias_intervalos.py — Frequência dos intervalos diatônicos no corpus.

Reproduz os números citados no TCC (Seção 5.1.3) sobre por que a pontuação
uniforme dos pesos ilustrativos (alpha = 2, beta = 1, gamma = 1) não serve:

  1. a distribuição dos intervalos diatônicos (delta) nas vozes dos corais;
  2. a probabilidade de dois intervalos tirados ao acaso de corais diferentes
     coincidirem, sum_d f(d)^2;
  3. o escore esperado da parte de alturas da Equação 7 para esse par
     aleatório, com e sem o desempate cromático gamma;
  4. a informação, em bits, de acertar cada intervalo, -log2 f(d).

A estimativa supõe independência entre os dois intervalos sorteados, o que é
o modelo de fundo usado na teoria de Karlin e Altschul (1990).

Uso:
    python scripts/frequencias_intervalos.py            # só os sopranos
    python scripts/frequencias_intervalos.py --vozes    # as quatro vozes
"""

import argparse
import math
from collections import Counter

from music21 import __version__ as versao_music21
from music21 import corpus

ALFA, BETA, GAMA = 2, 1, 1


def intervalos(parte):
    notas = [x for x in parte.recurse().notes if x.isNote]
    return [(b.pitch.diatonicNoteNum - a.pitch.diatonicNoteNum,
             b.pitch.midi - a.pitch.midi) for a, b in zip(notas, notas[1:])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vozes", action="store_true",
                    help="usa as quatro vozes, e não só o soprano")
    args = ap.parse_args()

    delta, par = Counter(), Counter()
    n_corais = 0
    for caminho in corpus.getComposer("bach"):
        if caminho.suffix not in (".mxl", ".xml", ".musicxml"):
            continue
        partitura = corpus.parse(caminho)
        if len(partitura.parts) != 4:
            continue
        n_corais += 1
        partes = partitura.parts if args.vozes else partitura.parts[:1]
        for parte in partes:
            for d, c in intervalos(parte):
                delta[d] += 1
                par[(d, c)] += 1

    total = sum(delta.values())
    f = {d: n / total for d, n in delta.items()}
    p_igual = sum(v * v for v in f.values())
    p_igual_crom = sum((n / total) ** 2 for n in par.values())
    e_sem_gama = ALFA * p_igual - BETA * (1 - p_igual)
    e_com_gama = e_sem_gama + GAMA * p_igual_crom

    print(f"music21 {versao_music21}; corais a quatro vozes: {n_corais}; "
          f"{'quatro vozes' if args.vozes else 'sopranos'}; "
          f"{total} intervalos")
    print(f"|delta| <= 1:            {sum(f.get(d, 0) for d in (-1, 0, 1)):.3f}")
    print(f"delta = +-1:             {f.get(-1, 0) + f.get(1, 0):.3f}")
    print(f"P(delta igual):          {p_igual:.3f}")
    print(f"P(delta e c iguais):     {p_igual_crom:.3f}")
    print(f"E[s] alturas, sem gamma: {e_sem_gama:+.3f}")
    print(f"E[s] alturas, com gamma: {e_com_gama:+.3f}")
    print("delta  freq   bits")
    for d in sorted(f):
        print(f"{d:+4d}  {f[d]:.3f}  {-math.log2(f[d]):5.1f}")


if __name__ == "__main__":
    main()
