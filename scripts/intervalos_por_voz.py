"""
intervalos_por_voz.py — Distribuição dos intervalos diatônicos por voz.

Reproduz os números citados no TCC (Seção 5.1.3) sobre a diferença entre as
vozes: a proporção de passos de um grau, de intervalos de no máximo um grau e
de saltos de terça ou mais em soprano, contralto, tenor e baixo dos corais a
quatro vozes de Bach distribuídos com o music21.

Uso:
    python scripts/intervalos_por_voz.py
"""

from collections import Counter

from music21 import __version__ as versao_music21
from music21 import corpus

VOZES = ["soprano", "contralto", "tenor", "baixo"]


def main():
    cont = [Counter() for _ in VOZES]
    n_corais = 0
    for caminho in corpus.getComposer("bach"):
        if caminho.suffix not in (".mxl", ".xml", ".musicxml"):
            continue
        partitura = corpus.parse(caminho)
        if len(partitura.parts) != 4:
            continue
        n_corais += 1
        for v, parte in enumerate(partitura.parts):
            notas = [x for x in parte.recurse().notes if x.isNote]
            for a, b in zip(notas, notas[1:]):
                cont[v][b.pitch.diatonicNoteNum - a.pitch.diatonicNoteNum] += 1

    print(f"music21 {versao_music21}: {n_corais} corais a quatro vozes")
    for nome, c in zip(VOZES, cont):
        total = sum(c.values())
        passo = sum(k for d, k in c.items() if abs(d) == 1) / total
        ate1 = sum(k for d, k in c.items() if abs(d) <= 1) / total
        salto = sum(k for d, k in c.items() if abs(d) >= 2) / total
        print(f"{nome:10s} {total:6d} intervalos | passos {passo:.1%} | "
              f"até um grau {ate1:.1%} | terça ou mais {salto:.1%}")


if __name__ == "__main__":
    main()
