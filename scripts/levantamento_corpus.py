"""
levantamento_corpus.py — Levantamento do corpus de corais de Bach no music21.

Reproduz as contagens citadas no TCC (Seções 6.2 e 6.3):

  1. quantos arquivos do music21 são atribuídos a Bach;
  2. quantos deles, em MusicXML, são corais a quatro vozes;
  3. quantas melodias de coral aparecem harmonizadas mais de uma vez, pelo
     critério de o soprano começar pela mesma sequência de N intervalos
     diatônicos (N = 10 por padrão), e quantos arquivos essas melodias somam.

Uso:
    python scripts/levantamento_corpus.py              # critério de 10 intervalos
    python scripts/levantamento_corpus.py --n 9        # outro critério
    python scripts/levantamento_corpus.py --listar     # lista os grupos

A contagem do item 3 é conservadora: harmonizações cujo soprano difere logo
no início (por uma nota de passagem, por exemplo) não são agrupadas. É o caso
do BWV 244.62, que se afasta das demais harmonizações do coral da Paixão no
nono intervalo.
"""

import argparse
from collections import defaultdict

from music21 import __version__ as versao_music21
from music21 import corpus


def intervalos_soprano(partitura, n):
    """Primeiros n intervalos diatônicos do soprano, ou None se forem menos."""
    notas = [x for x in partitura.parts[0].recurse().notes if x.isNote]
    graus = [x.pitch.diatonicNoteNum for x in notas]
    passos = tuple(b - a for a, b in zip(graus, graus[1:]))
    return passos[:n] if len(passos) >= n else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10,
                    help="número de intervalos iniciais do soprano comparados")
    ap.add_argument("--listar", action="store_true",
                    help="lista os arquivos de cada grupo")
    args = ap.parse_args()

    caminhos = corpus.getComposer("bach")
    corais = []
    for caminho in caminhos:
        if caminho.suffix not in (".mxl", ".xml", ".musicxml"):
            continue
        partitura = corpus.parse(caminho)
        if len(partitura.parts) == 4:
            corais.append((caminho, partitura))

    grupos = defaultdict(list)
    for caminho, partitura in corais:
        chave = intervalos_soprano(partitura, args.n)
        if chave is not None:
            grupos[chave].append(caminho.stem)

    repetidas = {k: v for k, v in grupos.items() if len(v) >= 2}

    print(f"music21 {versao_music21}")
    print(f"Arquivos atribuídos a Bach:               {len(caminhos)}")
    print(f"Corais a quatro vozes em MusicXML:        {len(corais)}")
    print(f"Melodias com 2+ harmonizações (N = {args.n}): {len(repetidas)}")
    print(f"Arquivos nessas melodias:                 "
          f"{sum(len(v) for v in repetidas.values())}")

    if args.listar:
        for arquivos in sorted(repetidas.values(), key=lambda v: (-len(v), v)):
            print("  " + ", ".join(sorted(arquivos)))


if __name__ == "__main__":
    main()
