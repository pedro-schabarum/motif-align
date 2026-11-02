"""pares_fontes.py — Pares de fontes de uma mesma harmonização no corpus (TCC, Seção 5.6.2).

Procura, entre os corais a quatro vozes em MusicXML do music21, pares de arquivos que
codificam a mesma harmonização: as quatro vozes coincidem em pelo menos LIMIAR da
sequência de intervalos diatônicos (razão de similaridade do difflib, biblioteca padrão).

Para cada par, informa:
  - a transposição entre as duas versões, em semitons (diferença entre as primeiras
    notas do soprano);
  - o número de trechos divergentes em cada voz (S, A, T, B), depois de remover a
    transposição: trechos maximais em que as sequências de (altura, duração) diferem.

Uso:
    python scripts/pares_fontes.py
"""

import difflib

from music21 import __version__ as versao_music21
from music21 import corpus

LIMIAR = 0.9


def vozes(caminho):
    sc = corpus.parse(caminho)
    if len(sc.parts) != 4:
        return None
    return [[n for n in p.stripTies().recurse().notes if n.isNote] for p in sc.parts]


def intervalos(notas):
    g = [n.pitch.diatonicNoteNum for n in notas]
    return [b - a for a, b in zip(g, g[1:])]


def razao(a, b):
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()


def main():
    print('music21', versao_music21)
    corais = []
    for caminho in corpus.getComposer('bach'):
        if not str(caminho).endswith(('.mxl', '.xml', '.musicxml')):
            continue
        try:
            v = vozes(caminho)
        except Exception:
            continue
        if v:
            corais.append((str(caminho).split('/')[-1], v, [intervalos(x) for x in v]))
    print('corais a quatro vozes:', len(corais))
    pares = 0
    for i in range(len(corais)):
        for j in range(i + 1, len(corais)):
            na, va, ia = corais[i]
            nb, vb, ib = corais[j]
            if min(razao(x, y) for x, y in zip(ia, ib)) < LIMIAR:
                continue
            pares += 1
            t = vb[0][0].pitch.midi - va[0][0].pitch.midi
            difs = []
            for x, y in zip(va, vb):
                sa = [(n.pitch.midi, n.quarterLength) for n in x]
                sb = [(n.pitch.midi - t, n.quarterLength) for n in y]
                ops = difflib.SequenceMatcher(None, sa, sb, autojunk=False).get_opcodes()
                difs.append(sum(1 for o in ops if o[0] != 'equal'))
            print(f'{na:16s} x {nb:16s} transposição {t:+d} st  trechos divergentes S,A,T,B = {difs}')
    print('pares de fontes:', pares)


if __name__ == '__main__':
    main()
