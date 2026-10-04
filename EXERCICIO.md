# Exercício: implementar o método do TCC passo a passo

Três módulos novos em `src/motif_align/`, com as funções definidas e os corpos
vazios (`NotImplementedError`). Os testes em `tests/` dizem exatamente o que
cada função tem que devolver. O trabalho é escrever os corpos até os testes
passarem, sem biblioteca de alinhamento.

```bash
pip install -r requirements.txt
pytest tests/test_alinhamento.py -x    # -x para parar no primeiro erro
```

## Ordem

| Passo | Função | Arquivo | No texto |
|---|---|---|---|
| 1 | `needleman_wunsch` | `alinhamento.py` | Eq. 1, Figura 2 |
| 2 | `traceback_global` | `alinhamento.py` | Seção 3.2 |
| 3 | `smith_waterman` | `alinhamento.py` | Eq. 2 |
| 4 | `traceback_local` | `alinhamento.py` | Seção 3.3 |
| 5 | `representar`, `intervalo_transposicao` | `representacao.py` | Eq. 4 |
| 6 | `inversao`, `retrogradacao` | `representacao.py` | Eq. 5 e 6 |
| 7 | (nada novo: testes com os sopranos reais) | `test_representacao.py` | Quadro 2, Seção 6.3 |
| 8 | `baixa_complexidade` | `sementes.py` | Seção 5.1.2 |
| 9 | `construir_indice` | `sementes.py` | Seção 5.1.2 |
| 10 | `buscar_hits` | `sementes.py` | Quadro 3, função Busca |

Os passos 1 a 4 são a base: se você conseguir explicar o que muda do 1 para o 3
(duas linhas de código), já responde metade das perguntas sobre o Capítulo 3.
O passo 7 junta tudo e mostra o Smith-Waterman alinhando os dois sopranos do
coral da Paixão de ponta a ponta, que é o gabarito parcial da Seção 6.3.

Depois disso vêm a extensão com *gaps* e X-drop (Eq. 3 e 7) e o teste de
permutação (Eq. 8), que ficam para a próxima rodada.

## O que já existe no repositório e não bate com o texto

O `core.py` é a prova de conceito anterior e segue um desenho diferente do que
está no TCC. Os testes dele passam, mas ele não implementa o
método descrito:

- usa intervalos cromáticos, e o texto adotou diatônicos;
- não tem índice de sementes: compara cada janela de A com todas as janelas de
  B por distância de edição, o que é força bruta e não *seed-and-extend*;
- estende sem *gaps*, e o texto adotou o *gapped BLAST*;
- trata o retrógrado da inversão como uma quarta transformação, que o texto não
  menciona;
- não tem significância (Eq. 8) nem comprimento mínimo.

Ele fica como está até os módulos novos cobrirem o pipeline. Se a banca abrir o
repositório, o código novo é o que corresponde ao texto.
