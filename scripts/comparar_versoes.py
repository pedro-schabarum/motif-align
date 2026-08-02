#!/usr/bin/env python3
"""
comparar_versoes.py — CLI para alinhar motivicamente duas versões de uma peça

Uso:
    python scripts/comparar_versoes.py versao_a.musicxml versao_b.musicxml [--parte 0]

Imprime os alinhamentos encontrados: posição em cada versão, tipo de
transformação e score de similaridade.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from motif_align.core import extract_notes, interval_sequence, align_motifs


def carregar_intervalos(caminho: str, indice_parte: int):
    from music21 import converter

    peca = converter.parse(caminho)
    parte = peca.parts[indice_parte] if peca.parts else peca
    notas = extract_notes(parte)
    return interval_sequence(notas), len(notas)


def main():
    parser = argparse.ArgumentParser(description="Alinha motivicamente duas versões de uma peça (MusicXML).")
    parser.add_argument("versao_a", help="Caminho do arquivo MusicXML da versão A")
    parser.add_argument("versao_b", help="Caminho do arquivo MusicXML da versão B")
    parser.add_argument("--parte", type=int, default=0, help="Índice da parte/voz a comparar (padrão: 0)")
    parser.add_argument("--min-len", type=int, default=4)
    parser.add_argument("--max-len", type=int, default=7)
    parser.add_argument("--seed-threshold", type=float, default=0.7)
    args = parser.parse_args()

    intervalos_a, n_notas_a = carregar_intervalos(args.versao_a, args.parte)
    intervalos_b, n_notas_b = carregar_intervalos(args.versao_b, args.parte)

    print(f"Versão A: {n_notas_a} notas ({len(intervalos_a)} intervalos)")
    print(f"Versão B: {n_notas_b} notas ({len(intervalos_b)} intervalos)")
    print()

    alinhamentos = align_motifs(
        intervalos_a, intervalos_b,
        min_len=args.min_len, max_len=args.max_len,
        seed_threshold=args.seed_threshold,
    )

    if not alinhamentos:
        print("Nenhum alinhamento encontrado acima do limiar.")
        return

    print(f"{len(alinhamentos)} alinhamento(s) encontrado(s):\n")
    for i, aln in enumerate(alinhamentos, 1):
        print(
            f"[{i}] A[{aln.start_a}:{aln.end_a}] <-> B[{aln.start_b}:{aln.end_b}]  "
            f"transformação={aln.transformation}  score={aln.score:.2f}"
        )


if __name__ == "__main__":
    main()
