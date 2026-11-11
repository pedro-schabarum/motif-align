# motif-align

Identificação de correspondências motívicas entre versões simbólicas de obras
musicais, com um método de alinhamento de sequências inspirado no BLAST
(*seed-and-extend*), aplicado aos corais a quatro vozes de J. S. Bach.

> Repositório do TCC em Ciência da Computação (Unochapecó, 2026).
> **Status:** o TCC I (fundamentação, método e planejamento da avaliação) foi
> concluído; a implementação do método e a avaliação ficam para o TCC II.
> O texto em `docs/tcc/` é a referência do método. Veja a seção
> [Estado do código](#estado-do-código).

## O problema

Ferramentas de diff de partitura, como o
[musicdiff](https://github.com/fosfrancesco/musicdiff) (Foscarin et al., 2019),
comparam duas versões de uma peça no nível do **símbolo** e apontam inserções,
remoções e substituições de notas. Os métodos de descoberta de padrões, como a
família SIATEC e o alinhamento local de Zhu et al. (2026), procuram motivos
repetidos **dentro de uma mesma obra**.

Este trabalho trata de outro problema: alinhar **duas versões** de uma
composição no nível **motívico**. O objetivo é produzir um mapeamento
segmentado das correspondências entre elas, rotulado pelo tipo de
transformação, que tolere transposição, variação rítmica e inserção ou
remoção de notas (e, como generalidade do método, inversão e retrogradação).

## Método (resumo do Capítulo 5 do TCC)

1. **Representação simbólica.** Cada voz vira uma sequência de triplas
   (δ, c, r): intervalo **diatônico**, intervalo cromático em semitons e
   proporção rítmica entre eventos consecutivos. A representação por
   intervalos é invariante à transposição por construção.
2. **Sementes.** Sementes de tamanho k passam por um filtro de baixa
   complexidade e são indexadas nas quatro formas: original, inversão,
   retrogradação e retrogradação da inversão.
3. **Busca e extensão com *gaps*.** A partir de cada coincidência com uma
   semente, o alinhamento é estendido nas duas direções, com penalidade de
   *gap* linear e parada por X-drop (como no Gapped BLAST). A pontuação de
   substituição φ entre intervalos diatônicos é do tipo *log-odds*,
   estimada no corpus, à maneira das matrizes BLOSUM.
4. **Filtragem.** Alinhamentos da mesma forma que se sobrepõem são reduzidos
   a um. Os que restam precisam atingir um comprimento mínimo e passar num
   teste de significância empírica por permutação, com modelo nulo separado
   por forma.
5. **Rotulagem.** Cada correspondência é segmentada e rotulada pelo tipo de
   transformação, com base nas alturas absolutas dos eventos alinhados.

O método compara as 16 combinações de vozes entre as duas versões.

## Avaliação planejada (TCC II)

- **Corpus:** corais a quatro vozes de Bach distribuídos com o
  [music21](https://web.mit.edu/music21/), em MusicXML.
- **Três conjuntos de teste:** pares sintéticos com gabarito completo;
  harmonizações diferentes de uma mesma melodia, com gabarito parcial pelo
  soprano (ex.: o coral da Paixão, BWV 244); e pares de fontes de uma mesma
  harmonização no corpus (ex.: as versões de Weimar e de Leipzig do BWV 18.5).
- **Critérios fixados a priori:** regra de acerto por sobreposição e
  calibração dos parâmetros num subconjunto do corpus separado do usado na
  avaliação.
- **Referências de comparação:** o alinhamento exato de Smith-Waterman e uma
  referência simples de transposição global.

## Estado do código

- `scripts/` reúne os scripts que reproduzem os números citados no texto do
  TCC. Cada script indica no cabeçalho a seção ou o quadro que reproduz:

  | Script | O que reproduz |
  |---|---|
  | `frequencias_intervalos.py`, `intervalos_por_voz.py` | Frequências de intervalos diatônicos no corpus (Seção 5.1.3) |
  | `quadro2.py`, `melhor_alinhamento.py` | Quadro 2 e alinhamentos do par BWV 244.15 × BWV 244.62 (Seção 5.1.4) |
  | `nulo.py`, `ae.py` | Comparação de modelos nulos para o teste de significância (Seção 5.1.4) |
  | `levantamento_corpus.py` | Contagens do corpus (Seções 5.6.1 e 5.6.2) |
  | `pares_fontes.py` | Pares de fontes de uma mesma harmonização (Seção 5.6.2, Quadro 7) |
  | `comparar_bwv18_5.py` | Diferenças entre as versões de Weimar e de Leipzig do BWV 18.5 (Seção 5.6.2) |

- `src/motif_align/core.py`, `tests/` e `scripts/comparar_versoes.py` são um
  **protótipo exploratório anterior ao desenho do TCC I**. Ele ainda usa
  intervalos cromáticos, janela deslizante e seleção gulosa, e **não
  implementa o método descrito no texto**. A implementação do método é o
  objetivo *f* do TCC, previsto para o TCC II.

## Rodando

```bash
pip install -r requirements.txt

# scripts que reproduzem os números do TCC
python scripts/levantamento_corpus.py
python scripts/quadro2.py

# testes do protótipo exploratório
pytest tests/ -v
```

## Texto do TCC

- `docs/tcc/TCC-I.docx`: versão atual do texto (formato de entrega). O
  histórico de versões fica no git.
- `docs/tcc/TCC-I.md`: exportação em Markdown, só para acompanhar no diff o
  que mudou entre versões. Regenerar com `bash scripts/exportar_texto.sh`
  antes de cada commit do .docx.
