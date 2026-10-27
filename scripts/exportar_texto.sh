#!/usr/bin/env bash
# exportar_texto.sh — gera docs/tcc/TCC-I.md a partir de docs/tcc/TCC-I.docx
#
# Uso: bash scripts/exportar_texto.sh
# Requer pandoc. Rodar sempre antes de commitar uma nova versão do .docx,
# para que o diff do Markdown mostre o que mudou no texto.
set -euo pipefail
cd "$(dirname "$0")/.."
pandoc docs/tcc/TCC-I.docx -t gfm --wrap=none --track-changes=accept -o docs/tcc/TCC-I.md
echo "docs/tcc/TCC-I.md atualizado"
