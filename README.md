# motif-align

Alinhamento motívico automático entre versões de uma composição musical simbólica.

> TCC I — Ciência da Computação. Status atual: **prova de conceito preliminar**
> (não é validação experimental completa — isso fica pro TCC II).

## O problema

Ferramentas de diff de partitura já existem e funcionam bem no nível da
**notação** — [musicdiff/Foscarin et al.](https://github.com/fosfrancesco/musicdiff)
apontam "essa nota mudou" entre duas versões de uma peça em MusicXML.

Não há, no levantamento feito até agora, uma ferramenta que compare duas
versões no nível **motívico/semântico**: apontar que um motivo específico foi
*transposto*, *invertido*, *retrogradado* (ou retrogradado-invertido) entre
as versões — distinguindo essa relação genuína de uma coincidência espúria de
intervalo.

## Abordagem

1. **Representação por intervalo cromático** — invariante a transposição por
   construção (duas execuções da mesma melodia em tons diferentes geram a
   mesma sequência de intervalos).
2. **Geração de candidatos por janela deslizante** sobre a versão A.
3. **Alinhamento por semente-e-extensão** (*seed-and-extend*, inspirado no
   [BLAST](https://blast.ncbi.nlm.nih.gov/)): acha uma âncora curta e
   confiável contra a versão B, depois estende nota por nota em cada direção
   enquanto a transformação continuar batendo, parando por critério X-drop
   (recuando até o pico de score, não até onde a extensão parou).
4. **Seleção gulosa** dos alinhamentos de maior score, removendo sobreposições.

Reaproveita a base técnica do TCC I anterior (representação por
intervalo/contorno, janela deslizante, [music21](https://web.mit.edu/music21/)).

## Objetivo de pesquisa

- **Principal:** distinguir correspondências motívicas genuínas de
  coincidências espúrias de intervalo entre duas versões de uma peça, com
  precisão/recall mensuráveis.
- **Secundário (descritivo):** dado um alinhamento já validado, classificar
  o tipo de transformação sofrida (transposição, inversão, retrogradação,
  retrogradação-inversão).

Separar esses dois objetivos foi uma correção importante de escopo — a
versão anterior do projeto misturava os dois num só problema de pesquisa.

## Estrutura

```
src/motif_align/core.py     # representação, transformações, seed-and-extend
tests/test_synthetic.py     # dados sintéticos, transformação conhecida
tests/test_real_piece.py    # corpus real (coral de Bach, BWV 66.6, via music21)
scripts/comparar_versoes.py # CLI: compara duas versões em MusicXML
```

## Rodando

```bash
pip install -r requirements.txt
pytest tests/ -v

python scripts/comparar_versoes.py versao_a.musicxml versao_b.musicxml
```

## O que já foi testado

- **Dados sintéticos:** motivo-base com transformação conhecida embutido em
  ruído — confirma que cada transformação clássica é reconhecida
  corretamente, que a extensão amplia a fronteira além da semente mínima, e
  que ruído puro não gera alinhamentos de alta confiança (controle de falso
  positivo).
- **Material real:** linha de soprano do coral de Bach BWV 66.6 (corpus
  embutido do music21) — confirma que a ideia se sustenta com material real,
  não só sintético, incluindo o caso de uma transformação conhecida
  (inversão) embutida em meio ao material original.
- **Dois bugs reais encontrados e corrigidos durante a reconstrução/teste,
  documentados aqui como parte do processo, não escondidos:**
  1. Definição matemática invertida de retrogradação vs.
     retrogradação-inversão (corrigida a partir da derivação formal a partir
     da sequência de notas — ver comentários em `core.py`).
  2. Score desatualizado no *seed-and-extend*: a extensão avançava até o
     limite do X-drop mas reportava o score de antes da extensão passar da
     região realmente correspondente, em vez de recuar até o pico real.

## Limitações conhecidas / próximos passos (TCC II)

- **Escopo monofônico** — uma voz por vez; não trata polifonia/acordes.
- **Sensibilidade ao tamanho da janela (`min_len`/`max_len`):** o tamanho
  mínimo de janela considerado — parâmetro que parece bobo à primeira vista —
  afeta diretamente quais alinhamentos "vencem" na seleção gulosa quando há
  empates de score (ex.: dois trechos idênticos podem gerar tanto um
  alinhamento grande cobrindo quase toda a peça quanto vários alinhamentos
  pequenos, dependendo da ordem de geração dos candidatos). Isso já apareceu
  nos testes com dados sintéticos e com material real — é decisão
  metodológica central, não só um parâmetro de ajuste fino, e precisa de
  tratamento formal na validação completa.
- **Sem métricas formais de precisão/recall ainda** — os testes atuais
  verificam comportamento esperado (achado correto, tipo correto, sem falso
  positivo óbvio), mas não uma validação estatística sobre corpus rotulado.
  Isso é o objetivo central do TCC II.
- **Baseline não comparado ainda** — falta comparação sistemática contra
  diff de notação pura (musicdiff) pra provar o ganho real do nível motívico.

## Contexto acadêmico

TCC I anterior reprovado por: fundamentação teórica rasa, trabalhos
relacionados fracos, corpus enviesado (autoral), avaliação sem critério
objetivo, contribuição computacional trivial. Este projeto reaproveita a
base técnica válida do trabalho anterior, mas resolve um problema diferente
e mais bem delimitado — com o cuidado explícito de não repetir os mesmos
erros de escopo e avaliação.
