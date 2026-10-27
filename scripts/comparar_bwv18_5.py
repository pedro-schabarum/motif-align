#!/usr/bin/env python3
"""
comparar_bwv18_5.py — compara as duas versões do coral BWV 18.5 no corpus do music21

Uso:
    python scripts/comparar_bwv18_5.py

Os arquivos bwv18.5-w (Weimar) e bwv18.5-lz (Leipzig) registram a mesma
harmonização a um tom de distância. O script transpõe a versão de Leipzig
dois semitons abaixo e lista, voz a voz, as diferenças de altura e duração
em relação à versão de Weimar (TCC, Seção 6.3).
"""

import difflib

from music21 import corpus

TRANSPOSICAO = 2  # semitons: Leipzig (lá menor) está um tom acima de Weimar (sol menor)


def eventos(partitura, indice_voz):
    out = []
    for nota in partitura.parts[indice_voz].recurse().notes:
        altura = nota.pitches[0]
        out.append((nota.measureNumber, altura.midi, float(nota.quarterLength)))
    return out


def main():
    leipzig = corpus.parse("bach/bwv18.5-lz.mxl")
    weimar = corpus.parse("bach/bwv18.5-w.mxl")
    for i, parte in enumerate(leipzig.parts):
        a = eventos(leipzig, i)
        b = eventos(weimar, i)
        chave_a = [(m - TRANSPOSICAO, d) for _, m, d in a]
        chave_b = [(m, d) for _, m, d in b]
        sm = difflib.SequenceMatcher(None, chave_a, chave_b, autojunk=False)
        print(f"== {parte.partName}: {len(a)}/{len(b)} notas, similaridade {sm.ratio():.3f}")
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag != "equal":
                print(f"  {tag} compasso {a[i1][0]}: Leipzig {a[i1:i2]} | Weimar {b[j1:j2]}")


if __name__ == "__main__":
    main()
