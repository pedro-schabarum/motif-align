<img src="media/image1.jpeg" style="width:5.44792in;height:1.39583in" alt="WhatsApp Image 2023-07-25 at 11" />

AATEC - Área de Agrárias, Engenharias e Tecnologias

Curso de ciência da computação

(Bacharelado)

Identificação de Correspondências Motívicas entre Versões Simbólicas de Obras Musicais:

um método de alinhamento de sequências aplicado aos corais de J. S. Bach

Pedro guilherme merisio schabarum

CHAPECÓ, novembro de 2026

AATEC - Área de Agrárias, Engenharias e Tecnologias

Curso de ciência da computação

(Bacharelado)

Identificação de Correspondências Motívicas entre Versões Simbólicas de Obras Musicais:

um método de alinhamento de sequências aplicado aos corais de J. S. Bach

Relatório Parcial do Trabalho de Conclusão de Curso submetido à Universidade Comunitária da Região de Chapecó para a disciplina de TCC I.

Pedro guilherme merisio schabarum

Orientador(a): Prof(ª). <span class="mark">\<Nome professor\>, \<Esp.,Me., Dr.\></span>

Co-Orientador(a): Prof(ª). <span class="mark">\<Nome professor\>, \<Esp.,Me., Dr.\> Co-Orientador: apenas se tiver</span>

CHAPECÓ, novembro de 2026

<span id="_Toc990000000" class="anchor"></span>Lista de Ilustrações

[**FIGURA 1 -** Representação da mesma nota (dó central, semínima) em MusicXML, \*\*kern e MEI](#_Toc990000006)

[**FIGURA 2 -** Matriz de programação dinâmica de Needleman-Wunsch para as sequências A = ACGT e B = AGT: cálculo de uma célula a partir da diagonal, de cima e da esquerda, e caminho de *traceback* até a origem](#_Toc990000023)

[**FIGURA 3 -** Diagrama de caso de uso do protótipo de alinhamento motívico](#_Toc990000049)

[**FIGURA 4 -** Diagrama de componentes do protótipo, organizado em camadas, com os dados trocados entre os componentes](#_Toc990000052)

[**FIGURA 5 -** Diagrama de classes do protótipo de alinhamento motívico](#_Toc990000054)

<span id="_Toc990000001" class="anchor"></span>Lista de QUADROS

[**QUADRO 1 -** Comparação entre os trabalhos relacionados e este trabalho](#_Toc990000034)

[**QUADRO 2 -** Exemplo de alinhamento entre os sopranos de BWV 244.15 e BWV 244.62](#_Toc990000041)

[**QUADRO 3 -** Pseudocódigo do método de alinhamento motívico](#_Toc990000044)

[**QUADRO 4 -** Descrição dos casos de uso do protótipo](#_Toc990000050)

[**QUADRO 5 -** Interfaces entre os componentes do protótipo](#_Toc990000053)

[**QUADRO 6 -** Campos do relatório de correspondências](#_Toc990000056)

[**QUADRO 7 -** Cronograma do TCC I, de 08/2026 a 12/2026](#_Toc990000065)

[**QUADRO 8 -** Cronograma do TCC II, de 02/2027 a 07/2027](#_Toc990000067)

<span id="_Toc990000002" class="anchor"></span>Lista de Siglas

BLAST - *Basic Local Alignment Search Tool*

MEI - *Music Encoding Initiative*

MIDI - *Musical Instrument Digital Interface*

OMR - *Optical Music Recognition*

Sumário

[Lista de Ilustrações](#_Toc990000000)

[Lista de QUADROS](#_Toc990000001)

[Lista de Siglas](#_Toc990000002)

[1 Introdução](#_Toc990000003)

[1.1 Contextualização](#_Toc990000004)

[1.2 Delimitação do problema](#_Toc990000005)

[1.3 Objetivos](#_Toc990000007)

[1.3.1 Objetivo geral](#_Toc990000008)

[1.3.2 Objetivos específicos](#_Toc990000009)

[1.4 Justificativa](#_Toc990000010)

[1.5 Procedimentos Metodológicos](#_Toc990000011)

[1.6 Estrutura do Trabalho](#_Toc990000012)

[2 Fundamentação Teórico-Musical da Variação entre Versões](#_Toc990000013)

[2.1 Identidade motívica sob transformação](#_Toc990000014)

[2.2 O coral a quatro vozes](#_Toc990000015)

[2.3 Ornamentação e notas estranhas ao acorde](#_Toc990000016)

[2.4 Recursos do contraponto imitativo](#_Toc990000017)

[2.5 Percepção melódica: Narmour e Dowling](#_Toc990000018)

[2.6 Considerações do capítulo](#_Toc990000019)

[3 Alinhamento de Sequências: Fundamentos Computacionais](#_Toc990000020)

[3.1 O problema do alinhamento de sequências](#_Toc990000021)

[3.2 Alinhamento global: Needleman-Wunsch](#_Toc990000022)

[3.3 Alinhamento local: Smith-Waterman](#_Toc990000024)

[3.4 A heurística *seed-and-extend*: BLAST](#_Toc990000025)

[3.5 Considerações do capítulo](#_Toc990000026)

[4 Trabalhos Relacionados em Música Simbólica](#_Toc990000027)

[4.1 Comparação entre versões: o musicdiff e o Measure Map](#_Toc990000028)

[4.2 Descoberta geométrica de padrões: a família SIATEC](#_Toc990000029)

[4.3 Alinhamento local intra-obra](#_Toc990000030)

[4.4 Similaridade entre variantes melódicas](#_Toc990000031)

[4.5 Heurísticas do BLAST aplicadas à música simbólica](#_Toc990000032)

[4.6 Síntese e posicionamento deste trabalho](#_Toc990000033)

[4.7 Considerações do capítulo](#_Toc990000035)

[5 MODELAGEM DO PROTÓTIPO](#_Toc990000036)

[5.1 Descrição da Solução Proposta](#_Toc990000037)

[5.1.1 Representação simbólica](#_Toc990000038)

[5.1.2 Geração e indexação de sementes](#_Toc990000039)

[5.1.3 Busca e extensão com gaps](#_Toc990000040)

[5.1.4 Filtragem e definição operacional de motivo](#_Toc990000042)

[5.1.5 Escolha da heurística seed-and-extend](#_Toc990000043)

[5.2 Elicitação de Requisitos](#_Toc990000045)

[5.2.1 Requisitos Funcionais](#_Toc990000046)

[5.2.2 Requisitos Não Funcionais](#_Toc990000047)

[5.3 Diagrama de Caso de Uso](#_Toc990000048)

[5.4 Projeto do Protótipo](#_Toc990000051)

[5.5 Formato de Saída dos Resultados](#_Toc990000055)

[5.6 Planejamento da Avaliação](#_Toc990000057)

[5.6.1 Corpus](#_Toc990000058)

[5.6.2 Construção dos Pares de Versões para Teste](#_Toc990000059)

[5.6.3 Parâmetros do Método de Alinhamento](#_Toc990000060)

[5.6.4 Critérios Objetivos de Avaliação](#_Toc990000061)

[5.7 Considerações do Capítulo](#_Toc990000062)

[6 CRONOGRAMA](#_Toc990000063)

[6.1 Cronograma do TCC I](#_Toc990000064)

[6.2 Cronograma do TCC II](#_Toc990000066)

[7 ORÇAMENTO](#_Toc990000068)

[Referências](#_Toc990000069)

1.  <span id="_Toc990000003" class="anchor"></span>Introdução

    1.  <span id="_Toc990000004" class="anchor"></span>Contextualização

A musicologia computacional tem se beneficiado da crescente disponibilidade de acervos de partituras em formato simbólico, como MusicXML, \*\*kern e MEI (*Music Encoding Initiative*), o que amplia as possibilidades de análise automatizada não apenas de obras isoladas, mas também das relações entre diferentes versões de uma mesma composição: edições distintas, arranjos, revisões autorais ou transcrições realizadas ao longo do tempo.

Comparar duas versões de uma obra musical, no entanto, exige mais do que identificar diferenças pontuais entre símbolos notacionais. Um motivo, padrão melódico-rítmico reconhecível que funciona como unidade básica de construção temática, pode ser transposto, ornamentado, alterado ritmicamente ou mesmo invertido e retrogradado e ainda assim ser reconhecido como o mesmo motivo por um analista e, no caso da transposição, também por um ouvinte. A teoria musical descreve esse fenômeno de mais de uma forma. No desenvolvimento temático de obras extensas, ele corresponde à ideia schoenberguiana de *developing variation*, a transformação contínua de uma ideia inicial ao longo da obra (ALMADA, 2008), analisada sistematicamente por Réti (1951 apud PEYERL; BARROS, 2017) e por Frisch (1984) em obras de Brahms. Entre versões de uma mesma peça, como as harmonizações de uma melodia de coral, as diferenças mais comuns são de outra natureza: transposição, notas de ornamentação acrescentadas ou suprimidas e alterações rítmicas, descritas pela teoria da harmonia e do contraponto (HINDEMITH, 1998; GOTHAM et al., 2021).

Do lado computacional, encontrar correspondências entre sequências que toleram pequenas variações não é um problema novo. A bioinformática lida com isso há décadas ao comparar sequências de DNA e proteínas. O algoritmo de Needleman e Wunsch (1970) resolve o alinhamento global por programação dinâmica; o de Smith e Waterman (1981) faz o mesmo para alinhamento local. Desses trabalhos surgiu o BLAST (do inglês *Basic Local Alignment Search Tool*; ALTSCHUL et al., 1990), que popularizou a estratégia de *seed-and-extend*: localizar pequenos trechos idênticos entre duas sequências e depois estendê-los, tolerando diferenças, em vez de comparar as sequências inteiras de uma vez.

No domínio da música simbólica, porém, as ferramentas existentes atacam problemas vizinhos, mas distintos, do que é proposto neste trabalho. O musicdiff (FOSCARIN; JACQUEMARD; FOURNIER-S'NIEHOTTA, 2019) realiza uma comparação notacional entre arquivos de partitura, apontando diferenças símbolo a símbolo, sem necessariamente capturar equivalência musical entre trechos transformados. Já os métodos voltados à descoberta de padrões — da família geométrica/*point-set* (MEREDITH; LEMSTRÖM; WIGGINS, 2002) a abordagens mais recentes baseadas em alinhamento local (ZHU et al., 2026) — buscam motivos que se repetem dentro de uma única peça, entre vozes (linhas melódicas simultâneas) ou seções, e não correspondências entre versões diferentes da mesma obra. Há, por outro lado, trabalhos que comparam variantes de uma mesma melodia (MONGEAU; SANKOFF, 1990; JANSSEN; VAN KRANENBURG; VOLK, 2017) e que já adaptaram o BLAST à música simbólica (KILIAN; HOOS, 2004; BOUNTOURIDIS et al., 2017). Eles se voltam, porém, à medição de semelhança, à recuperação de padrões ou à classificação de melodias, e não ao mapeamento de correspondências motívicas entre duas versões de uma obra.

É nesse espaço em aberto — entre o *diff* notacional de baixo nível, a descoberta de motivos intra-obra e a medição de semelhança entre variantes — que se situa o problema investigado neste trabalho.

Preencher essa lacuna interessa diretamente a pesquisadores e editores envolvidos na preparação de edições críticas de obras musicais, bem como a curadores de acervos digitais que reúnem diferentes edições e fontes de uma mesma composição.

2.  <span id="_Toc990000005" class="anchor"></span>Delimitação do problema

Apesar dos avanços recentes em ferramentas de comparação de partituras simbólicas, a literatura consultada não apresenta um método consolidado capaz de reconhecer, entre diferentes versões de uma mesma composição, trechos que preservam a mesma identidade motívica sob transposição, inversão, retrogradação ou variação rítmica, nem critérios objetivos e replicáveis para decidir quando um trecho de uma versão corresponde a um trecho de outra.

As ferramentas de comparação notacional, como o musicdiff (FOSCARIN; JACQUEMARD; FOURNIER-S'NIEHOTTA, 2019), operam no nível do símbolo: apontam inserções, remoções e substituições entre dois arquivos de partitura, mas não avaliam se as diferenças encontradas preservam ou rompem a identidade musical de um motivo. Já os métodos voltados à descoberta de padrões repetidos — da família geométrica (MEREDITH; LEMSTRÖM; WIGGINS, 2002) aos baseados em alinhamento local mais recentes (ZHU et al., 2026) — respondem a uma pergunta diferente: onde um motivo se repete dentro de uma única obra, entre vozes ou seções, e não onde um motivo de uma versão reaparece, transformado, em outra versão da mesma obra. Os trabalhos que comparam variantes melódicas (MONGEAU; SANKOFF, 1990; JANSSEN; VAN KRANENBURG; VOLK, 2017) e os que adaptam o BLAST à música (KILIAN; HOOS, 2004; BOUNTOURIDIS et al., 2017), por sua vez, produzem medidas de semelhança, ocorrências de um padrão de consulta ou rótulos de classificação, e não um mapeamento das correspondências motívicas entre duas versões.

O problema, portanto, é a ausência de um método capaz de alinhar sequencialmente duas versões simbólicas de uma composição, no nível motívico, tolerando transformações musicalmente reconhecíveis, e produzindo um resultado sobre o qual se possam aplicar critérios objetivos de avaliação — em vez de depender exclusivamente do julgamento qualitativo de um analista.

Este trabalho delimita-se à investigação desse problema em partituras simbólicas, tomando como corpus os corais a quatro vozes de J. S. Bach (peças em que quatro linhas melódicas — soprano, contralto, tenor e baixo — soam simultaneamente em harmonia): um corpus de domínio público, amplamente utilizado em pesquisa de musicologia computacional e já fixado antes do início deste trabalho: sua composição não foi escolhida ou ajustada pelo autor em função dos resultados que o método deveria produzir, o que reduz o risco de viés de seleção presente em corpora construídos *ad hoc* pelo próprio autor.

O escopo desta pesquisa limita-se à investigação de um método de alinhamento motívico entre versões simbólicas — não sonoras — de uma mesma composição musical, tomando como corpus de estudo os corais a quatro vozes de J. S. Bach disponíveis em formato simbólico (MusicXML, \*\*kern, MEI).

Dos três formatos, MusicXML foi adotado como formato de trabalho principal: é o formato em que o corpus de corais de Bach já é distribuído nativamente pelo music21 (CUTHBERT; ARIZA, 2010), com suporte completo de leitura e escrita na ferramenta. O \*\*kern permanece relevante como formato de comparação, por sua tradição em pesquisa computacional de música — inclusive em Zhu et al. (2026). Já o MEI, apesar de ser o formato mais alinhado à aplicação de edições críticas que motiva este trabalho, tem hoje suporte apenas de leitura no music21, o que o torna um alvo de interoperabilidade para trabalhos futuros, não o formato de trabalho deste protótipo.

A título de exemplo, a mesma nota — dó central, semínima — é representada nos três formatos conforme a Figura 1.

<img src="media/image2.png" style="width:5.70866in;height:2.81934in" alt="Representação da mesma nota em MusicXML, kern e MEI" />

1.  <span id="_Toc990000006" class="anchor"></span>Representação da mesma nota (dó central, semínima) em MusicXML, \*\*kern e MEI

Fonte: elaborado pelo autor (2026).

O método deve tolerar, no nível motívico, as diferenças mais prováveis entre versões de uma mesma obra: transposição, variação rítmica e inserção ou remoção de notas. Como generalidade, deve tolerar também inversão e retrogradação, transformações relevantes quando uma versão é um arranjo ou uma reelaboração da outra, e não uma edição. Nesta etapa do trabalho, prioriza-se a fundamentação teórica, a especificação da representação simbólica dos motivos e o desenho da heurística de alinhamento; a estratégia concreta de construção dos pares de versões utilizados nos testes — seja a partir de variantes documentadas na tradição de fontes dos corais, de transformações geradas programaticamente sobre o corpus, de harmonizações diferentes de uma mesma melodia presentes no próprio corpus, ou de uma combinação dessas fontes — é detalhada na Seção 5.6.2. Para os fins deste trabalho, o termo *versão* abrange tanto edições e fontes distintas de uma mesma obra quanto harmonizações diferentes, feitas pelo próprio Bach, de uma mesma melodia de coral. A segunda acepção é mais ampla do que a noção editorial de versão, mas é a que o corpus oferece em maior quantidade. Ela é declarada explicitamente para que os resultados obtidos sobre esses pares sejam lidos nessa chave.

A implementação do protótipo e a aplicação preliminar dos critérios de avaliação sobre o corpus não fazem parte do TCC I, estando previstas para o TCC II, conforme o Capítulo 6. Não estão previstos neste escopo: o processamento de áudio ou de imagens de partitura sem codificação simbólica prévia; e a aplicação do método a repertórios distintos dos corais de Bach. 

1.  <span id="_Toc990000007" class="anchor"></span>Objetivos

    1.  <span id="_Toc990000008" class="anchor"></span>Objetivo geral

Desenvolver e implementar, em um protótipo de software, um método para identificação de correspondências motívicas entre diferentes versões simbólicas de uma mesma composição musical, tolerante a transformações como transposição, inversão, retrogradação e variação rítmica, por meio de uma heurística de alinhamento de sequências inspirada no BLAST (*seed-and-extend*), tendo como corpus de estudo os corais a quatro vozes de J. S. Bach, com aplicação voltada à preparação de edições críticas e à curadoria de acervos digitais de partituras simbólicas.

2.  <span id="_Toc990000009" class="anchor"></span>Objetivos específicos

<!-- -->

1)  revisar a fundamentação teórico-musical sobre identidade e variação melódica entre versões (identidade motívica sob transformação, ornamentação e contraponto) e os métodos computacionais de alinhamento de sequências e de descoberta de padrões musicais, situando o método proposto em relação aos trabalhos existentes;

2)  especificar uma representação simbólica dos motivos musicais adequada à aplicação das transformações consideradas (transposição, inversão, retrogradação, variação rítmica) e à comparação entre versões;

3)  adaptar a heurística *seed-and-extend*, originária da bioinformática, ao domínio simbólico musical, definindo os critérios de pontuação e de extensão do alinhamento;

4)  modelar um protótipo de software que implemente o método — requisitos, casos de uso, componentes e parâmetros;

5)  propor critérios objetivos para avaliação das correspondências motívicas identificadas pelo método;

6)  implementar o protótipo modelado, em linguagem Python, com a biblioteca music21 (CUTHBERT; ARIZA, 2010);

7)  aplicar preliminarmente os critérios de avaliação aos dois conjuntos de teste descritos na Seção 5.6.2, comparando o método com a referência de alinhamento exato de Smith-Waterman.

Os objetivos específicos de *a* a *e* são desenvolvidos no TCC I, objeto deste documento; os objetivos *f* e *g*, no TCC II, conforme o cronograma apresentado no Capítulo 6.

1.  <span id="_Toc990000010" class="anchor"></span>Justificativa

Reconhecer quando um motivo reaparece, transformado, em outra versão de uma composição musical tem relevância tanto para a pesquisa em ciência da computação aplicada à música quanto para a prática da análise musical assistida por computador.

Do ponto de vista da musicologia, comparar versões de uma mesma obra (diferentes edições, arranjos ou revisões autorais) é uma tarefa recorrente na crítica textual musical (a comparação sistemática de fontes de uma obra para reconstituir ou documentar sua transmissão), mas que, no nível da identidade motívica, ainda depende em grande parte do julgamento e da disponibilidade de tempo do analista, já que as ferramentas computacionais disponíveis operam sobretudo no nível notacional, como se discute no Capítulo 4. O próprio corpus utilizado neste trabalho ilustra essa relevância prática. Os corais a quatro vozes de Bach chegaram até nós por duas vias distintas — parte transmitida dentro de obras maiores, como cantatas e paixões, muitas vezes em autógrafos do compositor, e parte preservada apenas em coletâneas organizadas postumamente. Entre essas fontes, há casos documentados de uma mesma harmonização registrada em tonalidades diferentes: o coral que encerra a cantata BWV 30, por exemplo, está em lá maior na partitura da cantata e em sol maior na coleção organizada por C. P. E. Bach e publicada pela Breitkopf (DAHN, 2017). Sem apoio computacional, esse tipo de transposição entre fontes só se estabelece pela comparação manual de uma fonte com a outra <span class="mark">\[PREFERIR FONTE ACADÊMICA: o levantamento de Dahn remete ao relatório crítico da Neue Bach-Ausgabe, NBA III/2.2 — perguntar ao coorientador\]</span>. Um método automatizado de alinhamento tolerante a esse tipo de transformação teria aplicação direta para pesquisadores e editores envolvidos na preparação de edições críticas dos corais de Bach, bem como para curadores de acervos digitais que reúnem diferentes edições e fontes de uma mesma obra.

Do ponto de vista computacional, o problema é relevante porque leva heurísticas de alinhamento consolidadas na bioinformática a uma tarefa não tratada nos trabalhos consultados. A analogia entre sequências biológicas e musicais não é nova: o BLAST (ALTSCHUL et al., 1990) já foi adaptado à busca de padrões e à classificação de melodias (KILIAN; HOOS, 2004; BOUNTOURIDIS et al., 2017). Essas adaptações, porém, respondem a perguntas de recuperação e classificação. Aplicar a mesma lógica, de busca por âncoras seguida de extensão tolerante a diferenças, à correspondência motívica entre versões de uma mesma obra, com as transformações explicitamente modeladas e avaliadas, estende essa analogia a um problema diferente e contribui especificamente para a musicologia computacional.

Por fim, a tolerância a transformações aproxima o método da forma como a correspondência motívica é reconhecida na prática, embora com uma distinção importante entre o ouvinte e o analista. A percepção melódica opera sobre relações entre notas, e não sobre a identidade exata de cada nota (NARMOUR, 1990), e por isso um trecho transposto, que preserva essas relações, tende a ser reconhecido como o mesmo trecho. Para as demais transformações, a evidência é mais restrita. Em experimentos com melodias curtas, Dowling (1972) observou que ouvintes reconhecem inversões, retrógrados e retrógrados da inversão acima do acaso, mas com dificuldade crescente nessa ordem. O método proposto não pretende, portanto, modelar o que um ouvinte percebe. Pretende apoiar o analista, que reconhece essas relações pela leitura da partitura, tornando explícitas e verificáveis correspondências que um método restrito a repetições literais deixaria de fora.

2.  <span id="_Toc990000011" class="anchor"></span>Procedimentos Metodológicos

Esta pesquisa é caracterizada segundo as quatro classificações propostas por Prodanov e Freitas (2013): quanto à natureza, aos objetivos, aos procedimentos técnicos e à forma de abordagem do problema. Quanto à natureza, é aplicada: propõe um método com aplicação direta à preparação de edições críticas e à curadoria de acervos digitais de partituras simbólicas, conforme a Seção 1.4. Quanto aos objetivos, é exploratória (GIL, 2002): investiga um problema ainda pouco explorado na literatura consultada, a correspondência motívica entre versões simbólicas de uma composição, sem hipóteses prévias a testar estatisticamente, buscando antes formular e especificar um método viável. Quanto aos procedimentos técnicos, combina pesquisa bibliográfica (Capítulos 2 a 4) com o desenvolvimento de um protótipo de software (Capítulo 5). Quanto à forma de abordagem, combina elementos quantitativos e qualitativos: as correspondências identificadas pelo método são avaliadas por métricas calculadas contra um gabarito, como precisão e cobertura, enquanto as correspondências encontradas nas vozes internas das harmonizações, que não têm gabarito, são examinadas qualitativamente (Seção 5.6).

O corpus é formado pelos corais a quatro vozes de J. S. Bach distribuídos com a biblioteca music21 (CUTHBERT; ARIZA, 2010), de domínio público e fixado antes do início deste trabalho. A caracterização do corpus, os conjuntos de teste construídos a partir dele, os parâmetros do método e os critérios objetivos de avaliação são detalhados na Seção 5.6, depois da apresentação do método, do qual dependem.

O trabalho é executado em oito etapas, que desdobram os sete objetivos específicos (Seção 1.3.2). As etapas 1 a 4 compõem o TCC I, objeto deste documento; as etapas 5 a 8, o TCC II. O cronograma correspondente é apresentado no Capítulo 6.

**Etapa 1 – Revisão bibliográfica (objetivo a; TCC I).** Levantamento e análise da fundamentação teórico-musical sobre identidade e variação melódica entre versões (Capítulo 2), dos algoritmos de alinhamento de sequências (Capítulo 3) e dos trabalhos computacionais relacionados em música simbólica (Capítulo 4), para situar o método proposto e delimitar sua contribuição.

**Etapa 2 – Especificação da representação (objetivo b; TCC I).** Definição da representação de cada voz por intervalos diatônicos, intervalos cromáticos e proporções rítmicas, com as alturas absolutas guardadas à parte, e das operações que derivam dessa representação as formas sob inversão, retrogradação e retrógrado da inversão (Seção 5.1.1).

**Etapa 3 – Adaptação da heurística e modelagem do protótipo (objetivos c e d; TCC I).** Adaptação da estratégia *seed-and-extend* ao domínio musical — sementes com filtro de baixa complexidade, indexação de variantes, extensão com *gaps* e X-drop e filtragem por significância empírica (Seções 5.1.2 a 5.1.5) — e sua tradução em requisitos, casos de uso, componentes e classes (Seções 5.2 a 5.5).

**Etapa 4 – Definição dos critérios de avaliação (objetivo e; TCC I).** Definição dos dois conjuntos de teste (Seção 5.6.2), dos parâmetros a calibrar (Seção 5.6.3) e dos critérios de avaliação, com a referência de Smith-Waterman (Seção 5.6.4).

**Etapa 5 – Implementação do protótipo (objetivo f; TCC II).** Implementação dos seis componentes em Python, com o music21, na ordem do fluxo de dados da Figura 4, e da referência de Smith-Waterman iterativo. Cada componente é verificado isoladamente antes da integração, com casos cujo resultado é conhecido de antemão — por exemplo, uma voz comparada com sua própria transposição deve produzir uma correspondência que cubra a voz inteira, rotulada como transposição com o intervalo correto.

**Etapa 6 – Construção dos conjuntos de teste (objetivo g; TCC II).** Divisão do corpus em subconjuntos de calibração e de avaliação (Seção 5.6.3), geração dos pares sintéticos com seu gabarito e seleção das harmonizações diferentes de uma mesma melodia (Seção 5.6.2).

**Etapa 7 – Calibração dos parâmetros (objetivo g; TCC II).** Execuções piloto sobre o subconjunto de calibração para fixar os sete grupos de parâmetros do método (Seção 5.6.3).

**Etapa 8 – Avaliação preliminar e análise (objetivo g; TCC II).** Execução do método e da referência de Smith-Waterman sobre o subconjunto de avaliação, cálculo dos critérios da Seção 5.6.4 — no conjunto e por tipo de transformação — e análise dos erros, com atenção às correspondências não encontradas e às espúrias, para identificar limitações do método.

3.  <span id="_Toc990000012" class="anchor"></span>Estrutura do Trabalho

Além desta introdução, o trabalho está organizado em seis capítulos. O Capítulo 2 revisa a fundamentação teórico-musical da variação entre versões, da noção schoenberguiana de identidade motívica à ornamentação melódica e à percepção. O Capítulo 3 apresenta os fundamentos computacionais do alinhamento de sequências, do algoritmo de Needleman-Wunsch à heurística do BLAST. O Capítulo 4 examina os trabalhos relacionados em música simbólica e posiciona a contribuição deste trabalho em relação a eles. O Capítulo 5 descreve a modelagem do protótipo que adapta a heurística *seed-and-extend* ao problema de correspondência motívica entre versões e o planejamento de sua avaliação: o corpus, os conjuntos de teste, os parâmetros e os critérios de avaliação. O Capítulo 6 apresenta o cronograma do TCC I e do TCC II, e o Capítulo 7, o orçamento.

2.  <span id="_Toc990000013" class="anchor"></span>Fundamentação Teórico-Musical da Variação entre Versões

Este capítulo revisa a fundamentação teórico-musical que sustenta a premissa central deste trabalho: a de que um trecho melódico pode ser transposto, ornamentado, ritmicamente alterado ou, como generalidade, invertido e retrogradado, e ainda assim ser reconhecido como correspondente a um trecho de outra versão da mesma obra. Parte-se da noção de identidade motívica sob transformação, formulada por Schoenberg e desenvolvida por Réti e Frisch, e de seus limites para o repertório deste trabalho (Seção 2.1). Em seguida, caracteriza-se o coral a quatro vozes (Seção 2.2) e examinam-se as diferenças que de fato aparecem entre versões de um coral: a ornamentação melódica (Seção 2.3) e os recursos do contraponto imitativo que encontram correspondência no método (Seção 2.4). Por fim, o modelo de implicação-realização de Narmour e os experimentos de Dowling deslocam a discussão para o plano perceptivo (Seção 2.5).

Das transformações consideradas, a transposição é a menos contestada: entre as fontes dos corais de Bach, uma mesma harmonização aparece registrada em tonalidades diferentes sem deixar de ser a mesma harmonização (Seção 1.4). Já a variação rítmica não recebe, dos autores revisados, um critério que permita medir quanto de alteração um trecho tolera sem perder sua correspondência com o de outra versão; essa medida é tratada, neste trabalho, no plano computacional, na etapa de pontuação da heurística descrita no Capítulo 5.

<span class="mark">\[REVISAR COM COORIENTADOR: capítulo reorganizado em 27/10/2026 a partir do apontamento do coorientador sobre a inadequação da Grundgestalt e da developing variation ao repertório dos corais de Bach. As Seções 2.2 e 2.3 usam a referência de harmonia indicada por ele (HINDEMITH, 1998); a Seção 2.4 usa Gotham et al. (2021) e depende ainda de Carvalho para a inversão melódica\]</span>

1.  <span id="_Toc990000014" class="anchor"></span>Identidade motívica sob transformação

A ideia de que um motivo preserva sua identidade através de transformações sucessivas tem formulação clássica em Schoenberg. Com o termo *developing variation*, ele descreve a transformação contínua de uma ideia inicial, que gera novos temas e fragmentos ao longo da obra; a célula de que esse processo parte é o que chama de *Grundgestalt*, ou forma básica. Schoenberg, porém, foi pouco sistemático ao definir esses termos (ALMADA, 2008) e os formulou a partir sobretudo da obra de Brahms, a quem dedicou o ensaio *Brahms the Progressive* (SCHOENBERG, 1984 apud ALMADA, 2008).

Rudolph Réti, em *The Thematic Process in Music* (1951), leva intuição semelhante a um método analítico sistemático. Para Réti, a diversidade temática na superfície de uma obra — os diferentes temas de uma sinfonia, por exemplo — esconde uma unidade motívica subjacente: os vários movimentos de uma obra derivariam, em sua leitura, de uma mesma ideia germinal, com o compositor preservando a substância dessa ideia por trás de uma aparência sempre renovada (RÉTI, 1951 apud PEYERL; BARROS, 2017; RÉTI, 1978 apud ALMADA, 2008). O repertório de transformações que Réti reconhece entre essas formas já inclui inversão e retrogradação, além de uma operação própria que chama de interversão: o reagrupamento das notas de uma célula em outra ordem (RÉTI, 1951, p. 68, 72 apud PEYERL; BARROS, 2017) — transformação que este trabalho não se propõe a tratar.

O método de Réti para demonstrar essa unidade, porém, foi alvo de críticas. Frisch (1984, p. 22-23 apud ALMADA, 2008) considera superficiais parte de suas análises, por levarem em conta apenas as alturas e os contornos intervalares dos temas, desvinculados de seu contexto rítmico e harmônico. Essa fragilidade se liga a outra, que é a que mais interessa a este trabalho: a decisão sobre quais notas de um tema pertencem à célula motívica básica e quais são ornamentação cabe ao próprio analista, sem um critério declarado que permita reproduzi-la.

Frisch (1984), por sua vez, aplica o conceito schoenberguiano de *developing variation* a dezoito obras de Brahms, com a atenção ao contexto harmônico e rítmico que ele próprio cobra de Réti. De Réti a Frisch, portanto, uma análise intuitiva dá lugar a uma análise mais disciplinada da transformação motívica — caminho que este trabalho continua, no sentido de que os critérios de pontuação e extensão da heurística proposta (Capítulo 5) substituem o julgamento subjetivo do analista por regras explícitas e reprodutíveis.

Os exemplos dessa tradição analítica, Brahms em Schoenberg e em Frisch, Mozart e Beethoven em Réti e em Almada (ALMADA, 2008), evidenciam seu limite para este trabalho. Ela descreve como uma ideia se desdobra dentro de uma obra extensa, ao longo de seções e movimentos. Os corais de Bach são peças curtas (o soprano de uma harmonização do coral da Paixão tem entre 42 e 56 notas na codificação do corpus; Seção 5.6.2), e o problema aqui investigado não é o desenvolvimento de uma ideia dentro de uma obra, mas a correspondência entre duas versões dela. Dessa tradição, este trabalho retém apenas a noção geral de identidade preservada sob transformação e o repertório de transformações que ela reconhece, incluindo a inversão e a retrogradação. A caracterização das diferenças que de fato ocorrem entre versões de um coral cabe às seções seguintes.

<span class="mark">\[CONFIRMAR COM COORIENTADOR: a decisão de excluir explicitamente a interversão do escopo ainda não foi validada com a orientação. Se houver acesso ao Frisch (1984, p. 22-23), trocar o apud por citação direta\]</span>

2.  <span id="_Toc990000015" class="anchor"></span>O coral a quatro vozes

Os corais de Bach são escritos para quatro vozes (soprano, contralto, tenor e baixo), a mesma disposição que o ensino tradicional da harmonia adota em seus exercícios (HINDEMITH, 1998, p. 1). Nesse ensino, harmonizar uma melodia dada consiste em escrever as demais vozes sob ela, escolhendo os acordes que a sustentam. Hindemith (1998, p. 43-47) propõe esse exercício tanto com os graus da harmonia indicados quanto sem eles; no segundo caso, a escolha dos acordes fica a cargo de quem harmoniza, com especial atenção à elaboração do baixo. Uma mesma melodia admite, portanto, mais de uma harmonização.

É o que se observa no corpus: Bach harmonizou muitas melodias de coral mais de uma vez, em obras e tonalidades diferentes (Seção 5.6.2), e entre duas harmonizações de uma mesma melodia o soprano se mantém, com pequenas variantes, enquanto as vozes internas e o baixo são reescritos. Essa é a base para tratar harmonizações de uma mesma melodia como versões dela (Seção 1.2): a melodia é o elemento dado e compartilhado, e cada harmonização é uma realização diferente sobre ela. Por isso, no segundo conjunto de teste, o gabarito parcial é definido pelo soprano (Seção 5.6.2).

<span class="mark">\[VALIDAR COM COORIENTADOR: uso de Hindemith (1998) como base para tratar harmonizações de uma mesma melodia como versões dessa melodia\]</span>

3.  <span id="_Toc990000016" class="anchor"></span>Ornamentação e notas estranhas ao acorde

Grande parte das diferenças entre versões de um coral está nas notas estranhas ao acorde, isto é, notas que não pertencem à harmonia que soa. Hindemith (1998, p. 40-42) descreve as principais: a bordadura, que aparece entre uma nota do acorde e sua repetição, a uma segunda acima ou abaixo; a nota de passagem, que preenche por grau conjunto o intervalo entre duas notas diferentes de um acorde; o retardo, que prolonga uma nota do acorde anterior e resolve por grau conjunto na nota do acorde correspondente; a antecipação, que apresenta no acorde anterior uma nota do acorde seguinte; a apojatura, um retardo sem preparação; e a escapada. A posição métrica faz parte dessas definições: bordaduras, notas de passagem e antecipações ocorrem em posição métrica mais fraca que as notas do acorde a que se ligam, enquanto o retardo ocorre em posição mais forte que sua preparação e sua resolução. Gotham et al. (2021) agrupam as mesmas notas pelo modo como se ligam às notas vizinhas: por grau conjunto, como a nota de passagem e a bordadura; por salto, como a apojatura e a escapada; e por permanência, como a suspensão, o retardo, o pedal e a antecipação.

Hindemith (1998, p. 43) observa ainda que acordes mais complicados podem, com frequência, ser interpretados como acordes mais simples acrescidos de notas estranhas. Por extensão, uma linha ornamentada e sua versão sem esses ornamentos compartilham a mesma estrutura subjacente, e é essa estrutura comum que o alinhamento entre versões procura reconhecer.

Nos corais de Bach, essas notas não são um enfeite indiferente à textura. Huron (2007), ao analisar 50 harmonizações de corais, observa que o emprego das notas de ornamentação favorece a segregação perceptiva das vozes, isto é, ajuda o ouvinte a acompanhar cada linha como independente, e que Bach tende a distribuí-las alternadamente entre as vozes.

Para o problema deste trabalho, a consequência é direta. Duas versões de um coral podem diferir por notas de passagem ou bordaduras acrescentadas ou suprimidas, por uma suspensão que desloca a resolução de uma voz ou por uma nota longa dividida em notas mais curtas, sem que a linha deixe de corresponder à da outra versão. As duas versões da BWV 18.5 no corpus, que diferem nas vozes internas justamente por notas longas divididas em notas repetidas (Seção 5.6.2), são um exemplo do último caso. Cada uma dessas diferenças tem correspondente no método: a inserção ou remoção de notas é absorvida pela extensão com *gaps* (Seção 5.1.3), a alteração rítmica pela tolerância na pontuação (Equação 7), e o predomínio do movimento por grau conjunto, que torna fragmentos de escala pouco distintivos, motiva o filtro de baixa complexidade das sementes (Seção 5.1.2). O fato de as notas estranhas ocuparem, em geral, posições métricas mais fracas sugere ainda um refinamento possível da pontuação, que penalizaria menos as divergências em tempos fracos; o desenho atual não o incorpora, e ele fica registrado como extensão a avaliar no TCC II.

<span class="mark">\[CONFERIR: volume, número e páginas de Huron (2007). LER: Hindemith (1998, cap. VII), Gotham et al. (2021), capítulo sobre notas de ornamentação, e Huron (2007). Acrescentar Fux (na tradução de Mann) e Carvalho após a leitura\]</span>

4.  <span id="_Toc990000017" class="anchor"></span>Recursos do contraponto imitativo

O contraponto imitativo, em que uma mesma linha melódica reaparece em vozes diferentes, oferece dois paralelos diretos para os mecanismos do método. O primeiro está na relação entre sujeito e resposta na fuga. Gotham et al. (2021) distinguem a resposta real, transposição exata do sujeito uma quinta acima ou uma quarta abaixo, que preserva seus intervalos, da resposta tonal, em que alguns intervalos são ajustados, com a menor alteração possível, para que a resposta não se afaste da tonalidade. A Fuga em dó menor do primeiro livro do *Cravo Bem Temperado* (BWV 847), que os autores tomam como exemplo, tem resposta tonal. A distinção corresponde, no repertório do próprio Bach, à que o método faz entre transposição real e tonal na rotulagem das correspondências (Seção 5.1.4).

O segundo paralelo é o contraponto invertível. Um contracanto invertível à oitava continua funcionando quando passa de cima para baixo do sujeito, isto é, quando as duas vozes trocam de posição (GOTHAM et al., 2021). Se uma linha pode trocar de voz dentro de uma obra, a correspondência entre duas versões também pode aparecer em vozes diferentes, o que fundamenta a comparação entre todas as dezesseis combinações de vozes (Seção 5.1.3).

O termo inversão exige, porém, uma distinção. No contraponto, o adjetivo invertível designa a troca de posição entre vozes, e não a inversão melódica considerada pelo método, em que cada intervalo de uma linha é espelhado (Seção 5.1.1). A inversão melódica e a retrogradação entram neste trabalho como generalidade do método, e não como diferenças típicas entre versões de um coral (Seção 5.1.2); sua inclusão apoia-se, por ora, no repertório de transformações reconhecido por Réti (Seção 2.1).

<span class="mark">\[A DESENVOLVER COM CARVALHO (Contraponto tonal e fuga, 3. ed., 2022): inversão melódica do sujeito como recurso da fuga na obra de Bach; retrogradação como recurso raro, mantido apenas como generalidade\]</span>

5.  <span id="_Toc990000018" class="anchor"></span>Percepção melódica: Narmour e Dowling

Enquanto Schoenberg, Réti e Frisch tratam a transformação motívica do ponto de vista de quem compõe ou analisa uma partitura, Eugene Narmour, em *The Analysis and Cognition of Basic Melodic Structures* (1990), aborda a melodia do ponto de vista de quem ouve. Seu modelo de implicação-realização, que expande a teoria da expectativa melódica de Leonard Meyer (MEYER, 1956), propõe que a percepção de uma melodia é guiada por expectativas geradas nota a nota: cada intervalo ouvido implica, para o ouvinte, algo sobre o intervalo que deve vir a seguir.

O modelo parte de duas hipóteses gerais, fundamentadas em princípios da psicologia da Gestalt. Um padrão melódico similar ao anterior implica continuidade: um pequeno intervalo tende a ser seguido por outro pequeno intervalo, na mesma direção, no que Narmour chama de processo. Um padrão marcadamente diferente, por sua vez, implica mudança: um intervalo grande tende a ser seguido por uma reversão de direção. Essas expectativas não são hipóteses conscientes do ouvinte, mas tendências perceptivas de baixo nível, moduladas por conhecimento estilístico aprendido — fatores que Narmour chama, respectivamente, de ascendentes (*bottom-up*) e descendentes (*top-down*).

A relevância desse modelo para este trabalho está em deslocar a discussão da tolerância à transformação do plano estrutural para o plano perceptivo. Schoenberg, Réti e Frisch explicam por que um compositor pode transformar um motivo sem romper sua identidade. Narmour ajuda a explicar por que certas transformações preservam, para o ouvinte, algo do original: a percepção melódica opera sobre relações, como intervalo e direção, e não sobre a identidade exata de cada nota. Essa explicação cobre bem a transposição real, que conserva todas essas relações. A transposição tonal, feita dentro da mesma tonalidade, conserva a direção e o tamanho dos passos medidos em graus da escala, mas não necessariamente o intervalo exato entre as notas.

O mesmo não vale, sem ressalvas, para inversão e retrogradação. Dowling (1972) testou diretamente o reconhecimento dessas transformações em melodias curtas. Os ouvintes as identificaram acima do acaso, mas com dificuldade crescente da inversão para o retrógrado e deste para o retrógrado da inversão, e sem distinguir as transformações que preservam os intervalos exatos daquelas que preservam apenas o contorno. Esse resultado delimita o alcance da fundamentação perceptiva: ela sustenta a tolerância à transposição, mas não autoriza afirmar que inversões e retrogradações soam como o mesmo motivo. Neste trabalho, a tolerância a essas duas transformações apoia-se, por isso, no plano analítico (Seções 2.1 e 2.4), e não no perceptivo, em coerência com seu reposicionamento como generalidade do método (Capítulo 5).

6.  <span id="_Toc990000019" class="anchor"></span>Considerações do capítulo

Este capítulo partiu da noção de identidade motívica sob transformação, formulada por Schoenberg e desenvolvida por Réti e Frisch, e mostrou seu limite para o problema deste trabalho: ela descreve o desenvolvimento de uma ideia dentro de obras extensas, e não a correspondência entre versões de peças curtas como os corais de Bach. As diferenças que de fato aparecem entre versões de um coral (transposição, ornamentação melódica, alterações rítmicas e reescrita das vozes internas) são descritas pela teoria da harmonia e do contraponto, e cada uma delas tem correspondente nos mecanismos do método, assim como a distinção entre resposta real e tonal e a troca de vozes do contraponto invertível. A perspectiva perceptiva, em Narmour e Dowling, sustenta bem a tolerância à transposição, mas não à inversão e à retrogradação, que permanecem como generalidade. Nenhuma dessas perspectivas, além disso, oferece um critério objetivo e computável para decidir quando um trecho de uma versão corresponde a um trecho de outra. É essa lacuna, situada entre a fundamentação teórico-musical deste capítulo e a fundamentação computacional do Capítulo 3, que a heurística proposta neste trabalho tenta preencher.

3.  <span id="_Toc990000020" class="anchor"></span>Alinhamento de Sequências: Fundamentos Computacionais

Este capítulo apresenta a linha de algoritmos que fundamenta computacionalmente o método proposto. Parte-se do problema geral de comparar duas sequências tolerando diferenças pontuais, passa-se pela solução clássica de programação dinâmica para alinhamento global e por sua variante para alinhamento local, e chega-se à heurística *seed-and-extend* do BLAST — a estratégia adaptada, no Capítulo 5, ao domínio da música simbólica. Cada seção situa o algoritmo correspondente no problema que ele resolve e na limitação que motivou o algoritmo seguinte.

1.  <span id="_Toc990000021" class="anchor"></span>O problema do alinhamento de sequências

Comparar duas sequências — de aminoácidos, de nucleotídeos, ou, como neste trabalho, de eventos musicais — é o problema de encontrar a melhor correspondência possível entre seus elementos, admitindo que nem todo elemento de uma tenha um correspondente exato na outra. Essa correspondência é descrita em termos de três operações básicas: substituição (um elemento de uma sequência corresponde a um elemento diferente na outra), inserção e deleção (um elemento de uma sequência não tem correspondente na outra). Um alinhamento é, portanto, uma forma de dispor as duas sequências lado a lado, com espaços (*gaps*) inseridos onde necessário, de modo a maximizar a semelhança total entre elementos correspondentes (GUSFIELD, 1997).

Duas variantes do problema se distinguem pela extensão da correspondência exigida. No alinhamento global, as duas sequências inteiras devem ser alinhadas de ponta a ponta — adequado quando se espera que sequências completas sejam homólogas[^1]. No alinhamento local, busca-se o par de subsequências mais semelhante entre as duas sequências, ignorando as regiões nas extremidades que não contribuem para esse trecho — adequado quando apenas parte das sequências deve corresponder, com o restante podendo divergir livremente ou não ter correspondente algum (GUSFIELD, 1997).

O que torna esse problema tratável computacionalmente é a propriedade de subestrutura ótima: o melhor alinhamento entre dois prefixos das sequências pode ser construído a partir dos melhores alinhamentos de prefixos menores. Essa propriedade é o que permite resolvê-lo por programação dinâmica[^2], evitando recalcular repetidamente as mesmas subsoluções.

2.  <span id="_Toc990000022" class="anchor"></span>Alinhamento global: Needleman-Wunsch

Needleman e Wunsch (1970) propuseram o primeiro método sistemático para alinhamento global por programação dinâmica, originalmente aplicado à comparação de sequências de aminoácidos em proteínas. O algoritmo constrói uma matriz em que cada célula (i, j) armazena a pontuação do melhor alinhamento possível entre os primeiros i elementos de uma sequência e os primeiros j elementos da outra. Cada célula é calculada a partir de três células vizinhas já resolvidas — a diagonal (correspondendo a um par elemento a elemento, com pontuação de acerto ou penalidade de erro), a célula à esquerda e a célula acima (correspondendo, cada uma, à inserção de um espaço em uma das sequências) — escolhendo-se sempre a opção de maior pontuação acumulada.

Formalmente, sejam a = a₁…aₙ e b = b₁…bₘ as duas sequências, s(aᵢ, bⱼ) a pontuação atribuída à correspondência entre dois elementos e g \> 0 a penalidade por espaço. A célula F(i, j) é dada pela Equação 1, com F(i, 0) = −i·g e F(0, j) = −j·g:

|                                                                           |       |
|---------------------------------------------------------------------------|-------|
| *F(i, j) = máx { F(i−1, j−1) + s(aᵢ, bⱼ), F(i−1, j) − g, F(i, j−1) − g }* | Eq. 1 |

Preenchida a matriz inteira, um processo de retrocesso (*traceback*) percorre o caminho de decisões que levou à célula final, reconstruindo o alinhamento ótimo. Por exigir que as duas sequências sejam percorridas até o fim, o algoritmo garante uma correspondência de ponta a ponta — mas essa mesma exigência é uma limitação quando apenas um trecho das sequências, e não sua totalidade, deve corresponder. A Figura 2 ilustra o preenchimento de uma célula e o caminho de retrocesso.

<img src="media/image3.png" style="width:6.02362in;height:2.63375in" alt="Matriz de programação dinâmica do alinhamento de Needleman-Wunsch" />

2.  <span id="_Toc990000023" class="anchor"></span>Matriz de programação dinâmica de Needleman-Wunsch para as sequências A = ACGT e B = AGT: cálculo de uma célula a partir da diagonal, de cima e da esquerda, e caminho de *traceback* até a origem

Fonte: elaborado pelo autor (2026).

Na Figura 2, a sequência A = ACGT está disposta nas colunas e a sequência B = AGT, nas linhas. A pontuação segue a Equação 1, com s(aᵢ, bⱼ) = +1 quando os dois elementos são iguais (acerto), s(aᵢ, bⱼ) = −1 quando são diferentes (erro) e penalidade g = 2 por espaço. A primeira linha e a primeira coluna recebem os valores F(0, j) = −2j e F(i, 0) = −2i, que correspondem a alinhar um prefixo de uma das sequências inteiramente contra espaços. A célula destacada, que cruza o G da sequência A com o G da sequência B, exemplifica o cálculo das demais: pela diagonal, soma-se o acerto G–G ao valor da célula diagonal (−1 + 1 = 0); de cima, subtrai-se a penalidade de espaço do valor da célula superior (−3 − 2 = −5); da esquerda, subtrai-se a mesma penalidade do valor da célula à esquerda (0 − 2 = −2). Prevalece o maior dos três valores, 0.

O valor do canto inferior direito, 1, é a pontuação do melhor alinhamento global entre as duas sequências. O *traceback* parte dessa célula e retorna à origem seguindo, a cada passo, a vizinha que originou o valor da célula atual: cada passo diagonal corresponde a um par de elementos, e cada passo horizontal, a um espaço inserido na sequência B. O caminho destacado na figura reconstrói, assim, o alinhamento de A–C–G–T com A–(espaço)–G–T, formado por três acertos e um espaço, cuja pontuação, 1 − 2 + 1 + 1 = 1, é igual à do canto da matriz. Entre todas as combinações possíveis de pares e espaços entre as duas sequências, nenhuma obtém pontuação maior sob esse esquema.

1.  <span id="_Toc990000024" class="anchor"></span>Alinhamento local: Smith-Waterman

Smith e Waterman (1981) adaptaram a recorrência de Needleman-Wunsch para o alinhamento local com uma mudança pontual, porém decisiva: pontuações negativas na matriz são zeradas em vez de propagadas. Na prática, isso permite que o algoritmo reinicie o alinhamento em qualquer ponto em que a correspondência deixa de compensar, em vez de carregar um histórico de penalidades acumuladas. O alinhamento ótimo passa a ser lido a partir da célula de maior pontuação em toda a matriz — não necessariamente no canto inferior direito, como em Needleman-Wunsch — e o retrocesso é interrompido assim que encontra uma célula zerada, delimitando o início do trecho correspondente.

A recorrência difere da Equação 1 apenas pelo piso zero e pela inicialização H(i, 0) = H(0, j) = 0:

|                                                                              |       |
|------------------------------------------------------------------------------|-------|
| *H(i, j) = max { 0, H(i−1, j−1) + s(aᵢ, bⱼ), H(i−1, j) − g, H(i, j−1) − g }* | Eq. 2 |

O resultado é a capacidade de encontrar o par de subsequências mais semelhante entre duas sequências maiores, ignorando o que vem antes e depois — exatamente o tipo de correspondência que este trabalho busca entre versões de uma composição, quando apenas um motivo, e não a peça inteira, precisa corresponder. Na formulação usual, com penalidade de *gap* linear, ambos os algoritmos têm a mesma complexidade: O(nm) em tempo e espaço, para sequências de tamanho n e m. Esse custo quadrático é aceitável para comparar duas sequências isoladas, mas torna-se proibitivo quando a busca precisa ser repetida contra um volume grande de sequências — o problema que o BLAST foi desenhado para resolver.

2.  <span id="_Toc990000025" class="anchor"></span>A heurística *seed-and-extend*: BLAST

O BLAST (*Basic Local Alignment Search Tool*; ALTSCHUL et al., 1990) nasceu da necessidade de buscar alinhamentos locais significativos em bancos de dados genômicos grandes demais para que o algoritmo exato de Smith-Waterman fosse aplicado a cada comparação. A ideia central é abrir mão da garantia de encontrar o alinhamento ótimo em troca de um ganho de velocidade suficiente para tornar a busca em larga escala viável — apostando que um alinhamento local genuinamente significativo quase sempre contém, em algum ponto, um pequeno trecho idêntico, ou muito semelhante, entre as duas sequências.

Esse pequeno trecho é a semente (*seed*): uma subsequência curta, de tamanho fixo, extraída da sequência de consulta. Em vez de comparar a consulta contra o banco de dados posição a posição, o BLAST localiza rapidamente onde essas sementes ocorrem — tipicamente por meio de uma tabela de posições pré-indexada — e só então investe processamento nos pontos em que houve uma coincidência (um *hit*). A partir de cada semente encontrada, o algoritmo estende o alinhamento em ambas as direções, acumulando pontuação, e interrompe a extensão assim que a pontuação cai um determinado valor abaixo do melhor escore já observado naquele trecho, critério conhecido como *X-drop*, evitando gastar processamento em extensões que já não têm chance de superar o que foi encontrado até ali. Na formulação original de 1990, essa extensão não admite espaços (*gaps*): uma única inserção ou remoção interrompe o alinhamento. Altschul et al. (1997) superaram esse limite com uma versão do BLAST com *gaps* (*gapped BLAST*). Ela mantém a etapa de sementes, mas passa a estender os *hits* mais promissores por programação dinâmica, explorando apenas as células da matriz cuja pontuação não caia mais do que um limiar abaixo do melhor escore já encontrado. É a mesma lógica de *X-drop*, agora aplicada a um alinhamento que admite inserções e remoções. Esta é a versão adotada pelo método deste trabalho, pelas razões discutidas no Capítulo 5.

Sendo S o escore acumulado no ponto corrente da extensão e Sₘₐₓ o maior escore observado desde o início dela, o critério de X-drop interrompe a extensão quando:

|                 |       |
|-----------------|-------|
| *S \< Sₘₐₓ − X* | Eq. 3 |

O resultado é a estratégia *seed-and-extend*: localizar pequenas âncoras idênticas ou quase idênticas entre duas sequências e, só a partir delas, estender tolerando diferenças, em vez de comparar as sequências inteiras posição a posição. É exatamente essa lógica, e não o BLAST enquanto ferramenta de bioinformática, que este trabalho adapta ao domínio simbólico musical.

3.  <span id="_Toc990000026" class="anchor"></span>Considerações do capítulo

A sequência histórica apresentada — alinhamento global exato, alinhamento local exato, alinhamento local heurístico — é também uma sequência de concessões: cada algoritmo abre mão de uma garantia do anterior em troca de aplicabilidade a um problema que o anterior não resolvia bem. É exatamente o último desses passos, o *seed-and-extend* do BLAST, que este trabalho adapta ao domínio da música simbólica, na heurística descrita no Capítulo 5. Antes de detalhar essa adaptação, porém, é preciso situar o problema dentro do que já foi feito computacionalmente sobre música simbólica, incluindo as próprias adaptações do BLAST à música, assunto do capítulo seguinte.

4.  <span id="_Toc990000027" class="anchor"></span>Trabalhos Relacionados em Música Simbólica

Este capítulo situa o método proposto em relação a cinco linhas de trabalho computacional já aplicadas à música simbólica. Três delas operam dentro de uma única peça ou no nível do símbolo notacional: a comparação entre versões de partitura, no nível do símbolo notacional ou do compasso, a descoberta geométrica de padrões repetidos e o alinhamento local aplicado à extração de motivos entre vozes de uma mesma obra. As outras duas estão mais próximas do problema deste trabalho: a medição de similaridade entre variantes de uma mesma melodia e a adaptação da heurística do BLAST à música simbólica. Nenhuma delas resolve, isoladamente, o problema de correspondência motívica entre versões de uma composição, mas cada uma cobre parte dele. Essa cobertura parcial justifica examinar seus mecanismos em detalhe antes da modelagem apresentada no capítulo seguinte.

1.  <span id="_Toc990000028" class="anchor"></span>Comparação entre versões: o musicdiff e o Measure Map

O musicdiff nasceu de um problema prático: comparar arquivos de partitura para edição colaborativa, controle de versão e avaliação de sistemas de reconhecimento óptico de partituras (OMR, do inglês *Optical Music Recognition*), verificando se a saída de um desses sistemas corresponde à transcrição de referência. Inspirados no modelo clássico do *diff* usado para arquivos de texto — que localiza a menor sequência de inserções, remoções e substituições capaz de transformar um arquivo no outro —, Foscarin, Jacquemard e Fournier-S'niehotta (2019) propõem um procedimento equivalente para partituras em formato XML.

A diferença em relação a um *diff* textual está na representação: os autores constroem uma representação intermediária em árvore do conteúdo notacional da partitura, capturando a estrutura hierárquica de compassos, vozes e eventos, e combinam distância de edição de sequências com distância de edição de árvores para localizar as diferenças entre duas partituras. O resultado aponta, símbolo a símbolo, onde uma nota, uma pausa ou outro elemento notacional foi inserido, removido ou substituído entre as duas versões comparadas.

É justamente essa granularidade — cada diferença corresponde a um símbolo notacional isolado — que separa o musicdiff do problema deste trabalho. Uma passagem transposta um tom acima, por exemplo, é registrada como uma sequência de substituições de altura, nota a nota: sob a métrica do *diff* notacional, quase nada naquele trecho é “igual” entre as duas versões. Para um músico, porém, a passagem é reconhecida instantaneamente como o mesmo motivo, apenas deslocado. O musicdiff responde com precisão à pergunta “o que mudou, símbolo a símbolo?” — mas não à pergunta que motiva este trabalho: essa mudança preserva a identidade motívica do trecho?

Em outro nível de granularidade, Gotham et al. (2023) tratam o alinhamento de versões de uma mesma obra como um problema de bibliotecas digitais para musicologia: os acervos simbólicos passam a incluir, cada vez mais, múltiplas edições e codificações das mesmas obras, e alinhar essas fontes tem sido um obstáculo persistente para combiná-las e compará-las. A solução proposta, o *measure map*, é um formato leve que representa apenas a informação de compassos de cada fonte, acompanhado de código para gerá-lo a partir de diferentes formatos, diagnosticar as diferenças entre fontes e, em parte dos casos, corrigi-las nos próprios arquivos. O Measure Map compartilha com este trabalho a unidade de comparação — versões de uma mesma obra —, mas alinha compassos como referência de localização comum, sem examinar seu conteúdo melódico: duas versões que numeram os compassos da mesma forma, mas diferem por uma transposição ou por uma ornamentação, são indistinguíveis nessa representação. Os dois alinhamentos são, portanto, complementares, e um mapa de compassos entre versões pode servir de referência para localizar as correspondências motívicas relatadas pelo método proposto.

2.  <span id="_Toc990000029" class="anchor"></span>Descoberta geométrica de padrões: a família SIATEC

Meredith, Lemström e Wiggins (2002) atacam um problema diferente do musicdiff: não comparar dois arquivos, mas descobrir, dentro de uma única peça polifônica, quais padrões se repetem. A estratégia representa a peça como um conjunto de pontos em um espaço multidimensional — tipicamente, tempo de início no eixo horizontal e altura no eixo vertical — e busca padrões geométricos que se repetem sob translação nesse espaço.

O algoritmo SIA identifica os padrões máximos passíveis de translação dentro do conjunto de pontos; o SIATEC, construído sobre o SIA, localiza todas as ocorrências de cada padrão descoberto, agrupando-as em classes de equivalência translacional. A elegância dessa formulação geométrica é que uma única operação — a translação no plano tempo-altura — captura ao mesmo tempo repetições no tempo (o mesmo padrão reaparecendo mais adiante na peça) e repetições transpostas (o mesmo padrão reaparecendo em outra altura): ambas são, geometricamente, apenas translações do mesmo conjunto de pontos.

Essa formulação tem, porém, um limite natural: por operar exclusivamente por translação, a família SIATEC não captura, sem extensões adicionais, padrões relacionados por inversão ou retrogradação — transformações que exigem refletir o conjunto de pontos, não apenas deslocá-lo. E, como o musicdiff, o SIATEC opera dentro de uma única peça: sua unidade de comparação é o conjunto de pontos de uma obra, não a correspondência entre duas versões distintas dela.

3.  <span id="_Toc990000030" class="anchor"></span>Alinhamento local intra-obra

Entre os trabalhos que operam dentro de uma única peça, o de Zhu et al. (2026) é o mais próximo deste, por adotar a mesma família algorítmica: o alinhamento local de Smith-Waterman (1981), discutido no Capítulo 3. Os autores extraem, de cada voz de uma peça polifônica, uma sequência de intervalos diatônicos, e aplicam alinhamento local par a par entre as vozes da mesma peça — soprano contra contralto, contralto contra tenor, e assim por diante — para segmentar trechos onde duas vozes se assemelham.

A partir dessa segmentação, os autores aplicam métodos baseados em cadeias de caracteres para identificar motivos candidatos, constroem um grafo acíclico dirigido ponderado para medir a importância relativa de cada motivo encontrado, e aplicam um procedimento de seleção e filtragem guiado por regras e informação estrutural da peça, validando o método sobre o conjunto de dados JKUPDD. Os próprios autores descrevem o problema como detecção de motivo intra-obra (*intra-opus*).

A diferença em relação a este trabalho está no eixo da comparação, não no algoritmo: Zhu et al. (2026) alinham vozes diferentes de uma mesma peça, em busca de repetição e imitação internas a ela; este trabalho alinha versões diferentes da mesma peça, em busca de correspondência entre elas. É a mesma família algorítmica aplicada a dois problemas distintos.

4.  <span id="_Toc990000031" class="anchor"></span>Similaridade entre variantes melódicas

Uma linha de pesquisa anterior às discutidas até aqui trata justamente da comparação entre versões de uma mesma melodia. Mongeau e Sankoff (1990) adaptam conceitos da teoria de comparação de sequências para medir a semelhança global entre duas partituras, com uma medida projetada para reconhecer a mesma linha melódica apesar de diferenças de tonalidade, modo ou andamento. A principal contribuição do trabalho está em duas operações de edição próprias do domínio musical, somadas à inserção, à remoção e à substituição da distância de edição clássica. Na fragmentação, uma nota de uma sequência corresponde a várias notas mais curtas da outra; a consolidação é a operação inversa. Os autores aplicam a medida a um conjunto de variações de Mozart sobre um mesmo tema, e a análise de agrupamento dos resultados reproduz as impressões subjetivas de semelhança entre as variações. O artigo apresenta ainda uma generalização do algoritmo para detectar trechos localmente semelhantes entre duas partituras.

Mais recentemente, Janssen, van Kranenburg e Volk (2017) partem de uma constatação consolidada nos estudos de canções folclóricas: variantes de uma mesma canção são reconhecidas por segmentos melódicos salientes, como frases e motivos, enquanto o restante da melodia pode variar consideravelmente. Os autores comparam diversas medidas de similaridade na tarefa de localizar ocorrências de segmentos melódicos em variantes, entre elas distâncias vetoriais, alinhamento local, transformada *wavelet* e indução de estrutura, e as avaliam contra anotações humanas.

Entre as linhas revisadas, esta é a que compartilha com este trabalho o eixo da comparação: ambas comparam versões, e não vozes ou seções de uma mesma peça. As diferenças estão no tipo de resultado e no repertório de transformações. Mongeau e Sankoff (1990) produzem essencialmente uma medida de semelhança entre partituras, e não um mapeamento das correspondências localizadas entre elas. Janssen, van Kranenburg e Volk (2017) fazem uma avaliação comparativa de medidas já existentes sobre melodias folclóricas monofônicas, e não propõem um método novo. Em ambos os casos, as variações tratadas são as típicas da transmissão de uma melodia, como transposição, alterações rítmicas e ornamentação, sem inversão ou retrogradação. As operações de fragmentação e consolidação, em particular, são diretamente relevantes para a tolerância rítmica exigida pelo método deste trabalho, como se discute no Capítulo 5.

5.  <span id="_Toc990000032" class="anchor"></span>Heurísticas do BLAST aplicadas à música simbólica

A analogia entre sequências biológicas e musicais que motiva este trabalho não é inédita. Kilian e Hoos (2004) propõem o MusicBLAST, que adapta a versão com *gaps* do BLAST (ALTSCHUL et al., 1997) à busca aproximada de padrões em dados musicais simbólicos. A matriz de pontuação entre aminoácidos é substituída por uma função de similaridade entre notas, que pode se basear em altura, intervalo, duração ou proporção rítmica. A partir de janelas de alta similaridade, o algoritmo estende alinhamentos com *gaps* nas duas direções, recupera múltiplas ocorrências de um padrão de consulta, inclusive incompletas e imperfeitas, e as ordena por uma medida de significância. Os autores observam ainda que, em princípio, as operações de fragmentação e consolidação de Mongeau e Sankoff (1990) poderiam ser integradas ao BLAST, ao custo de redesenhar seus critérios de interrupção. A avaliação apresentada é preliminar e se restringe a exemplos ilustrativos, como o alinhamento entre uma execução em MIDI e a partitura correspondente; os autores deixam uma avaliação detalhada para trabalhos posteriores.

Bountouridis et al. (2017) retomam a mesma analogia com outra motivação: o alinhamento par a par por programação dinâmica, método mais usado para comparar melodias codificadas simbolicamente, não escala bem em tempo de execução. Os autores aplicam a indexação do BLAST a duas coleções, uma de melodias folclóricas e outra de melodias de versões *cover*, e obtêm desempenho de classificação comparável ao de abordagens exaustivas. Complementam esse resultado com alinhamento múltiplo de sequências e modelos ocultos de Markov de perfil.

Esses dois trabalhos mostram que a heurística *seed-and-extend* é aplicável à música simbólica. Por isso, a adaptação do BLAST, por si só, não constitui a contribuição deste trabalho. O que os separa do problema aqui investigado é a tarefa. Ambos tratam de recuperação, isto é, localizar onde um padrão de consulta ocorre em uma coleção, ou de classificação, isto é, decidir a que família uma melodia pertence. Nenhum deles trata do mapeamento de correspondências entre duas versões de uma mesma obra. Além disso, nenhum dos dois, pelo que descrevem os próprios autores, modela inversão ou retrogradação, nem avalia a identificação de transformações específicas contra um gabarito.

6.  <span id="_Toc990000033" class="anchor"></span>Síntese e posicionamento deste trabalho

Colocados lado a lado, os trabalhos revisados delimitam por exclusão o problema investigado. O musicdiff compara duas partituras, mas no nível do símbolo notacional, sem tolerância a transformações que preservam a identidade motívica; o Measure Map (GOTHAM et al., 2023) também compara versões de uma mesma obra, mas alinha apenas compassos, sem examinar seu conteúdo melódico. O SIATEC e Zhu et al. (2026) buscam padrões dentro de uma única peça: o primeiro por translação, o que captura repetição e transposição, mas não inversão ou retrogradação; o segundo por alinhamento local entre vozes simultâneas. Mongeau e Sankoff (1990) e Janssen, van Kranenburg e Volk (2017) comparam variantes de uma mesma melodia, mas produzem medidas de semelhança ou localizam segmentos, sem tratar inversão ou retrogradação. Por fim, o MusicBLAST (KILIAN; HOOS, 2004) e Bountouridis et al. (2017) adaptam o BLAST à música simbólica, mas para tarefas de recuperação e classificação. O Quadro 1 resume essas diferenças.

1.  <span id="_Toc990000034" class="anchor"></span>Comparação entre os trabalhos relacionados e este trabalho

| **Trabalho**                                                | **Unidade de comparação**          | **Tipo de resultado**                                       | **Transformações tratadas**                                                      | **Estratégia de busca**                              |
|-------------------------------------------------------------|------------------------------------|-------------------------------------------------------------|----------------------------------------------------------------------------------|------------------------------------------------------|
| musicdiff (FOSCARIN; JACQUEMARD; FOURNIER-S'NIEHOTTA, 2019) | Duas partituras (versões)          | Diferenças notacionais localizadas                          | Nenhuma (comparação símbolo a símbolo)                                           | Distância de edição de sequências e de árvores       |
| Measure Map (GOTHAM et al., 2023)                           | Versões de uma obra                | Correspondência entre compassos                             | Nenhuma (não examina o conteúdo melódico)                                        | Comparação da estrutura de compassos                 |
| SIATEC (MEREDITH; LEMSTRÖM; WIGGINS, 2002)                  | Uma peça                           | Padrões repetidos e suas ocorrências                        | Translação (repetição e transposição)                                            | Geométrica, sobre conjuntos de pontos                |
| ZHU et al. (2026)                                           | Vozes de uma mesma peça            | Motivos da peça                                             | Transposição (intervalos diatônicos)                                             | Alinhamento local (Smith-Waterman)                   |
| MONGEAU; SANKOFF (1990)                                     | Duas melodias (variantes)          | Medida de semelhança                                        | Tonalidade, modo, andamento e ritmo (fragmentação e consolidação)                | Programação dinâmica exaustiva                       |
| JANSSEN; VAN KRANENBURG; VOLK (2017)                        | Segmento e variantes de uma canção | Ocorrências de segmentos                                    | Variação entre variantes folclóricas                                             | Comparação de medidas, incluindo alinhamento local   |
| MusicBLAST (KILIAN; HOOS, 2004)                             | Padrão de consulta e peça          | Ocorrências do padrão, com significância                    | Dependem da função de similaridade adotada                                       | Seed-and-extend com *gaps*                           |
| BOUNTOURIDIS et al. (2017)                                  | Melodia e coleção                  | Classificação de melodias                                   | Variação entre melodias de uma mesma família                                     | Indexação do BLAST                                   |
| **Este trabalho**                                           | **Duas versões de uma obra**       | **Correspondências localizadas, com tipo de transformação** | **Transposição, variação rítmica, inserção e deleção; inversão e retrogradação** | **Seed-and-extend com *gaps* e variantes indexadas** |

Fonte: elaborado pelo autor (2026).

A contribuição deste trabalho, portanto, não está em nenhum desses elementos isolados, e sim em uma combinação que, na literatura consultada, nenhum dos trabalhos revisados reúne. O primeiro elemento é a comparação entre versões de uma mesma obra, com saída na forma de correspondências localizadas em ambas as versões, e não de uma medida global de semelhança ou de uma lista de ocorrências de um padrão de consulta. O segundo é a heurística *seed-and-extend* com indexação explícita das variantes de cada semente sob inversão e retrogradação, ao lado da invariância à transposição obtida pela própria representação. O terceiro são critérios objetivos de avaliação calculados contra um gabarito de transformações conhecidas. É nessa combinação que se situa a heurística apresentada no Capítulo 5.

1.  <span id="_Toc990000035" class="anchor"></span>Considerações do capítulo

Este capítulo revisou cinco linhas de trabalho computacional já aplicadas à música simbólica: comparação entre versões no nível do símbolo e do compasso, descoberta geométrica de padrões, alinhamento local intra-obra, similaridade entre variantes melódicas e adaptações do BLAST à música. Para cada uma, mostrou que parte do problema de correspondência motívica entre versões ela cobre e que parte deixa em aberto. Combinada à fundamentação teórico-musical do Capítulo 2 e à fundamentação computacional do Capítulo 3, essa revisão completa o panorama necessário para apresentar, no capítulo seguinte, a modelagem do protótipo que adapta a heurística *seed-and-extend* a esse problema.

5.  <span id="_Toc990000036" class="anchor"></span>MODELAGEM DO PROTÓTIPO

Este capítulo apresenta a modelagem do protótipo que implementa o método de alinhamento motívico descrito nos capítulos anteriores. Descreve-se a solução proposta em termos de arquitetura geral, os requisitos funcionais e não funcionais que orientam o desenvolvimento, o caso de uso que caracteriza a interação com a ferramenta, o projeto interno de seus componentes e, por fim, o planejamento da avaliação do método. A implementação do protótipo aqui modelado e a aplicação preliminar dos critérios de avaliação estão previstas para o TCC II; este capítulo estabelece o desenho que orienta essa implementação.

1.  <span id="_Toc990000037" class="anchor"></span>Descrição da Solução Proposta

A solução proposta é um protótipo de linha de comando que recebe como entrada duas versões simbólicas, em formato MusicXML, de uma mesma composição — no caso deste trabalho, dois corais a quatro vozes de J. S. Bach — e produz como saída um relatório das correspondências motívicas identificadas entre elas, incluindo a localização de cada correspondência em ambas as versões, o tipo de transformação envolvida (transposição, inversão, retrogradação, variação rítmica, ou uma combinação delas) e uma pontuação associada.

Internamente, o protótipo organiza o processamento em quatro etapas sequenciais, que retomam a estrutura conceitual apresentada nos Capítulos 3 e 4 e são detalhadas nas subseções a seguir: representação simbólica, geração e indexação de sementes, busca e extensão, e filtragem. A última subseção justifica a escolha da heurística *seed-and-extend* diante da alternativa de alinhamento exato.

1.  <span id="_Toc990000038" class="anchor"></span>Representação simbólica

A primeira etapa, de leitura e representação, usa o music21 (CUTHBERT; ARIZA, 2010) para carregar cada versão MusicXML e extrair, de cada voz, uma sequência de eventos musicais, cada um formado por um par de altura e duração. Essa sequência é convertida para uma representação baseada em intervalos melódicos diatônicos e proporções rítmicas, e não em alturas absolutas. Os intervalos são medidos em graus da escala, e não em semitons, por causa da natureza tonal do corpus: nos corais, a inversão musicalmente pertinente é a tonal, que espelha os graus dentro da tonalidade. Essa é também a representação adotada por Zhu et al. (2026). A escolha já embute parte da tolerância a transformações exigida pelo problema, porque uma passagem transposta produz a mesma sequência de intervalos que o original. As demais transformações correspondem a operações simples sobre essa sequência. A inversão equivale a trocar o sinal de cada intervalo. A retrogradação equivale a inverter a ordem da sequência e, ao mesmo tempo, trocar o sinal de cada intervalo, já que percorrer as alturas de trás para frente também inverte a direção de cada passo; as proporções rítmicas, no retrógrado, são lidas em ordem inversa e substituídas por suas recíprocas. Por exemplo, as alturas dó–ré–mi–sol geram os passos diatônicos (+1, +1, +2); seu retrógrado, sol–mi–ré–dó, gera (−2, −1, −1), e não (+2, +1, +1), que seria o retrógrado da inversão.

Formalmente, cada voz é uma sequência de eventos V = (e₁, …, eₙ), com eₖ = (pₖ, dₖ), em que pₖ é a altura e dₖ a duração. Sua representação é a sequência S = (x₁, …, xₙ₋₁), definida pela Equação 4. Nela, δₖ é o intervalo diatônico, medido em graus da escala; cₖ é o intervalo em semitons; e rₖ é a proporção rítmica entre eventos consecutivos. As alturas absolutas pₖ, que essa representação descarta, são guardadas à parte, junto com a localização de cada evento na partitura: não participam da busca nem da pontuação, mas são usadas na rotulagem das transformações (Seção 5.1.4).

|                                                                                 |       |
|---------------------------------------------------------------------------------|-------|
| *xₖ = (δₖ, cₖ, rₖ), δₖ = grau(pₖ₊₁) − grau(pₖ), cₖ = pₖ₊₁ − pₖ, rₖ = dₖ₊₁ / dₖ* | Eq. 4 |

As transformações passam a ser funções sobre S, com m = n − 1 (Equações 5 e 6). A transposição deixa S invariante e é identificada a posteriori, pelas alturas absolutas dos eventos alinhados (Seção 5.1.4). A composição das duas operações, o retrógrado da inversão, é RetInv(S) = Ret(Inv(S)): os intervalos diatônicos aparecem em ordem inversa e com o sinal original.

|                                            |       |
|--------------------------------------------|-------|
| *Inv(S)ₖ = (−δₖ, ∅, rₖ)*                   | Eq. 5 |
| *Ret(S)ₖ = (−δₘ₊₁₋ₖ, −cₘ₊₁₋ₖ, 1 / rₘ₊₁₋ₖ)* | Eq. 6 |

A representação diatônica tem, porém, um custo: um intervalo de terça é codificado da mesma forma, seja ele maior ou menor. Isso torna a representação mais permissiva e tende a aumentar o número de coincidências entre sementes. Para compensar essa perda sem abrir mão da invariância, o protótipo guarda, ao lado de cada intervalo diatônico, o intervalo cromático correspondente, usado apenas na etapa de pontuação como critério de desempate: coincidências diatônicas que também coincidem cromaticamente pontuam mais. Esse desempate não se aplica, porém, a comparações com as formas que envolvem inversão (Inv e RetInv): na inversão tonal, o intervalo cromático não é preservado de forma geral, já que uma terça maior ascendente pode corresponder a uma terça menor descendente. Por isso, o componente cromático de Inv(S) e de RetInv(S) fica indefinido (∅), como na Equação 5, e o termo γ da Equação 7 é omitido nessas comparações. A retrogradação não tem esse problema, porque percorrer as mesmas alturas em ordem inversa preserva exatamente cada intervalo em semitons, com o sinal trocado.

2.  <span id="_Toc990000039" class="anchor"></span>Geração e indexação de sementes

A segunda etapa, de geração e indexação de sementes, percorre a sequência de uma das versões (a versão de consulta) extraindo subsequências curtas de tamanho fixo — as sementes — e as indexa em uma tabela de posições, seguindo a mesma lógica do BLAST (ALTSCHUL et al., 1990) descrita no Capítulo 3. A semente é definida apenas sobre a componente de intervalos melódicos diatônicos da sequência, sem a componente rítmica. Essa escolha é deliberada: inversão, retrogradação e sua composição, o retrógrado da inversão, são operações discretas, cada uma com uma única forma alternativa bem definida para cada semente, o que permite indexar essas variantes de antemão; a variação rítmica, ao contrário, não tem um conjunto finito de formas possíveis — pode envolver alongamento, encurtamento, síncope ou inserção e remoção de notas —, o que inviabiliza o mesmo tratamento. Restringir a semente aos intervalos evita que uma passagem apenas ritmicamente alterada deixe de gerar qualquer *hit*; a tolerância rítmica é tratada inteiramente na pontuação da etapa de extensão, a seguir. Para cada semente, o protótipo indexa não apenas sua forma original, mas também suas variantes sob inversão, retrogradação e retrógrado da inversão, de modo que a etapa seguinte de busca não precise testar cada transformação separadamente. A transposição não exige uma variante indexada equivalente: como a semente já é definida sobre intervalos melódicos diatônicos, e não sobre alturas absolutas, uma passagem transposta gera a mesma sequência de intervalos que o original, produzindo naturalmente um *hit* sem qualquer indexação adicional. Formalmente, a semente iniciada na posição i é wᵢ = (δᵢ, …, δᵢ₊ₖ₋₁). O índice é uma tabela hash I que associa cada semente à lista de pares (i, T) em que ela ocorre, com T ∈ {Id, Inv, Ret, RetInv} indicando a forma sob a qual foi indexada; a consulta a I tem custo esperado constante.

Entre as transformações consideradas, transposição, variação rítmica e inserção ou remoção de notas são as diferenças mais prováveis entre versões de uma mesma obra, como edições, fontes e harmonizações distintas de uma mesma melodia. Inversão e retrogradação raramente aparecem nesse tipo de relação. São mantidas no método como generalidade, relevante quando uma versão é arranjo ou reelaboração da outra, e seu custo é pequeno, porque se resumem a variantes adicionais na tabela de sementes.

Antes da indexação, as sementes passam por um filtro de baixa complexidade. Nos corais, a condução de vozes é predominantemente por graus conjuntos. Sementes formadas apenas por passos na mesma direção, isto é, fragmentos de escala, ocorrem em praticamente qualquer trecho de qualquer voz e geram coincidências sem valor motívico. O problema tem um análogo direto na bioinformática: ali, regiões de baixa complexidade composicional das sequências são identificadas e mascaradas antes da busca (WOOTTON; FEDERHEN, 1993), justamente porque produzem alinhamentos espúrios. O protótipo adota a mesma estratégia. Sementes de baixa complexidade são descartadas da indexação ou têm seu peso reduzido, e o critério exato é definido na calibração (Seção 5.6.3). Como critério inicial, é mascarada toda semente cujos passos são todos iguais e de no máximo um grau (\|δ\| ≤ 1), isto é, notas repetidas ou fragmentos de escala em uma única direção.

3.  <span id="_Toc990000040" class="anchor"></span>Busca e extensão com gaps

A terceira etapa, de busca e extensão, percorre a sequência da outra versão em busca de coincidências com as sementes indexadas (os *hits*). A partir de cada *hit*, o alinhamento é estendido em ambas as direções. Diferentemente da formulação original do BLAST, a extensão admite espaços (*gaps*), seguindo a versão de Altschul et al. (1997) descrita no Capítulo 3: a partir da semente, o alinhamento é calculado por programação dinâmica restrita à vizinhança do *hit* e interrompido pelo critério de *X-drop*. A admissão de *gaps* é necessária porque parte das diferenças esperadas entre versões consiste justamente na inserção ou remoção de notas, como uma nota de passagem acrescentada ou um ornamento suprimido. Uma extensão sem *gaps* não absorve esse tipo de diferença: uma única nota a mais desloca todo o restante do trecho e encerra a extensão. A pontuação acumulada combina os intervalos diatônicos, o desempate cromático e a divergência entre proporções rítmicas, e penaliza os *gaps* segundo um custo a ser calibrado (Seção 5.6.3).

Sendo xᵢ = (δᵢ, cᵢ, rᵢ) um elemento de S e yⱼ = (δ′ⱼ, c′ⱼ, r′ⱼ) um elemento de S′, a pontuação do par é dada pela Equação 7, em que \[·\] vale 1 se a condição é verdadeira e 0 caso contrário. O logaritmo torna simétricas as penalidades de dobrar e de dividir pela metade uma duração. A extensão aplica, a partir da semente, a recorrência da Equação 1 com essa pontuação e penalidade linear g por espaço, mas apenas nas células cujo escore não viola o critério de X-drop (Equação 3). O piso zero do Smith-Waterman não é usado: é o X-drop que encerra a extensão, e o alinhamento permanece ancorado na semente. Os pesos α, β, γ e ρ, a penalidade g e o limiar X são parâmetros do método, calibrados conforme a Seção 5.6.3.

<table>
<colgroup>
<col style="width: 90%" />
<col style="width: 9%" />
</colgroup>
<tbody>
<tr class="odd">
<td><em>s(xᵢ, yⱼ) = α·[δᵢ = δ′ⱼ] − β·[δᵢ ≠ δ′ⱼ] + γ·[δᵢ = δ′ⱼ ∧ cᵢ = c′ⱼ]<br />
− ρ·|log₂(rᵢ / r′ⱼ)|</em></td>
<td>Eq. 7</td>
</tr>
</tbody>
</table>

Uma extensão possível desse esquema são as operações de fragmentação e consolidação propostas por Mongeau e Sankoff (1990) e discutidas no Capítulo 4. Elas modelam diretamente a substituição de uma nota por várias notas mais curtas, e vice-versa, situação comum em variantes rítmicas. Com *gaps*, essa situação é tratada apenas de forma aproximada, como uma substituição seguida de inserções. Kilian e Hoos (2004) observam, porém, que integrar essas operações ao BLAST exigiria redesenhar seus critérios de interrupção. Por isso, o desenho apresentado neste trabalho adota apenas a extensão com *gaps*. A incorporação da fragmentação e da consolidação fica registrada como extensão candidata, a ser avaliada no TCC II a partir do desempenho observado nos casos de variação rítmica.

As etapas de busca e extensão são aplicadas a todas as dezesseis combinações entre as quatro vozes das duas versões, e não apenas às vozes de mesmo nome. Essa escolha permite identificar correspondências em que um motivo muda de voz entre uma versão e outra, como numa troca entre tenor e contralto, e tem custo desprezível para sequências do tamanho de uma voz de coral.

O Quadro 2 ilustra as etapas sobre um par real do segundo conjunto de teste (Seção 5.6.2): os sopranos das harmonizações BWV 244.15 e BWV 244.62 do coral da Paixão. Os pesos foram escolhidos apenas para fins ilustrativos (α = 2, β = 1, γ = 1, ρ = 1, g = 2, X = 5 e k = 4) e não correspondem a valores calibrados.

2.  <span id="_Toc990000041" class="anchor"></span>Exemplo de alinhamento entre os sopranos de BWV 244.15 e BWV 244.62

| **Etapa**             | **Resultado**                                                                                                                                                                                                                                               |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Representação**     | Os dois sopranos começam pela mesma sequência de intervalos diatônicos, (3, −1, −1, −1, −1, 1, 4, 1, …), a partir de fá♯4 (BWV 244.15) e de mi4 (BWV 244.62).                                                                                               |
| **Semente**           | w₁ = (3, −1, −1, −1) tem valores distintos, não é mascarada e é indexada a partir de BWV 244.15.                                                                                                                                                            |
| **Hit**               | w₁ ocorre na posição 1 de BWV 244.62, na forma original (T = Id).                                                                                                                                                                                           |
| **Escore da semente** | 4 pares idênticos × (α + γ) = 12.                                                                                                                                                                                                                           |
| **Extensão**          | Mais 4 pares idênticos levam o escore a 24. Na 9ª posição, BWV 244.15 repete a nota ré5 (δ = 0), sem correspondente em BWV 244.62; um espaço a absorve (−g). A extensão atravessa o trecho ornamentado de BWV 244.62 com substituições e um segundo espaço. |
| **Resultado**         | Escore máximo 31,6, cobrindo as 17 primeiras notas de BWV 244.15 e as 15 primeiras de BWV 244.62.                                                                                                                                                           |
| **Rótulo**            | Transposição real de uma segunda maior descendente (−2 semitons, diferença de altura comum aos pares de eventos alinhados; Seção 5.1.4), com divergências absorvidas por espaços.                                                                           |

Fonte: elaborado pelo autor (2026).

1.  <span id="_Toc990000042" class="anchor"></span>Filtragem e definição operacional de motivo

A quarta etapa, de filtragem e geração do relatório, decide quais correspondências são reportadas. Essa decisão não pode depender de gabarito, que só existe nos pares de teste, e por isso é distinta das métricas de avaliação propostas na Seção 5.6.4. No BLAST, esse papel cabe ao E-value, o número esperado de alinhamentos com escore igual ou superior ao observado que surgiriam por acaso. Seu cálculo, porém, pressupõe um modelo estatístico calibrado para sequências biológicas e para o esquema de pontuação original, que não se transfere diretamente para a representação e a pontuação adotadas aqui. O protótipo estima, por isso, a significância de forma empírica. Para cada par de vozes, a busca completa é repetida P vezes sobre permutações aleatórias π da sequência comparada, e registra-se o escore máximo M(π) obtido em cada repetição. Esses máximos formam a distribuição de referência. O valor-p empírico de uma correspondência com escore S é estimado pela Equação 8, que soma uma unidade ao numerador e ao denominador para que o valor-p nunca seja nulo (PHIPSON; SMYTH, 2010). Usar o escore máximo, e não o escore de cada alinhamento isolado, controla a ocorrência de falsos positivos quando um mesmo par de vozes produz muitas correspondências.

|                                              |       |
|----------------------------------------------|-------|
| *p̂ = ( 1 + \#{ π : M(π) ≥ S } ) / ( 1 + P )* | Eq. 8 |

Uma correspondência só é reportada se seu valor-p não exceder um limiar de significância p\* e se tiver um comprimento mínimo ℓmin, ambos definidos na calibração (Seção 5.6.3).

Cada correspondência reportada recebe, por fim, um rótulo de transformação. A forma T do hit que a originou indica se houve inversão, retrogradação ou retrógrado da inversão. A transposição, porém, não pode ser lida da representação, que é invariante a ela, nem apenas da comparação entre as alturas iniciais dos dois trechos. Como um trecho transposto preserva todos os seus intervalos internos, a transposição de um trecho no interior de uma voz altera somente o intervalo de entrada e o de saída, e o alinhamento pode atravessá-lo com duas substituições sem que a altura inicial revele a mudança. Por isso, o rótulo é atribuído percorrendo os pares de eventos alinhados e calculando, para cada par, a diferença de altura entre as duas versões, medida em graus da escala. Cada sequência maximal de pares com a mesma diferença forma um segmento, rotulado como idêntico, quando a diferença é nula, ou como transposição, caso contrário. A transposição é classificada como real quando a diferença em semitons também é constante ao longo do segmento, e o relatório informa esse intervalo; quando apenas a diferença em graus é constante, como numa transposição dentro da mesma tonalidade, ela é classificada como tonal, e o relatório informa o intervalo diatônico. A variação rítmica é atribuída aos segmentos em que as proporções rítmicas divergem. Uma mesma correspondência pode, assim, ser desdobrada em um segmento idêntico seguido de um segmento transposto, e cada segmento ocupa uma linha do relatório (Quadro 6).

Essas etapas permitem dar ao termo *motivo*, no contexto do protótipo, uma definição operacional. Uma correspondência motívica é um trecho alinhado entre duas versões que atinge o comprimento mínimo, supera o limiar de significância empírica e não se reduz a uma região de baixa complexidade. A definição é deliberadamente mais estreita do que o conceito musicológico discutido no Capítulo 2 (não captura, por exemplo, a função formal de um motivo na obra), mas é o que torna a identificação reprodutível e avaliável por critérios objetivos.

2.  <span id="_Toc990000043" class="anchor"></span>Escolha da heurística seed-and-extend

O tamanho das sequências comparadas levanta uma questão legítima. Se cada voz de um coral tem poucas dezenas de eventos, o alinhamento exato de Smith-Waterman (1981), de custo quadrático, é viável, e o principal argumento a favor do BLAST, a escala, não se aplica à comparação de um único par de versões. Também não procede o argumento de que o alinhamento exato produziria uma única correspondência: aplicado de forma iterativa, mascarando a cada rodada o trecho já alinhado, ele produz várias, e pode ser repetido sobre as formas invertida e retrógrada a um custo apenas constante. A escolha pela heurística não se apoia, portanto, em economia de processamento no tamanho de um coral, mas em duas razões de desenho. Primeiro, no *seed-and-extend* cada correspondência nasce de um *hit* e carrega, desde a origem, a forma T sob a qual foi encontrada, o que torna direta a rotulagem da transformação e dispensa decidir a ordem das rodadas de mascaramento entre as diferentes formas. Segundo, o mesmo desenho permite, sem mudança estrutural, buscar um motivo contra o corpus inteiro, cenário fora do escopo deste trabalho, mas em que o argumento de escala volta a valer, como mostram Bountouridis et al. (2017). Em contrapartida, a heurística pode deixar de encontrar correspondências que o alinhamento exato encontraria. Medir essa perda é justamente o papel do Smith-Waterman iterativo como referência de comparação na avaliação (Seção 5.6.4): se ela se mostrar grande, a heurística não se justifica para o problema aqui tratado.

O Quadro 3 apresenta o pseudocódigo do método completo, reunindo as quatro etapas descritas nas subseções anteriores, e o parágrafo seguinte estima seu custo, em comparação com a complexidade O(nm) dos algoritmos exatos apresentada na Seção 3.3.

3.  <span id="_Toc990000044" class="anchor"></span>Pseudocódigo do método de alinhamento motívico

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Algoritmo CorrespondenciasMotivicas(A, B, θ)</p>
<p>Entrada: A, B: partituras a quatro vozes (objetos Score do music21)</p>
<p>θ = (k, α, β, γ, ρ, g, X, P, p*, ℓmin, σ) ▹ σ: semente do gerador aleatório</p>
<p>Saída: C: conjunto de correspondências rotuladas</p>
<p>Variáveis:</p>
<p>u, v: vozes de A e de B, sequências de eventos (p, d)</p>
<p>S, S′: representações de u e v, sequências de triplas (δ, c, r) ▹ Eq. 4</p>
<p>I: tabela hash semente → lista de pares (i, T), com</p>
<p>T ∈ {Id, Inv, Ret, RetInv} e i a posição da semente em T(S)</p>
<p>R: conjunto de alinhamentos do par (u, v)</p>
<p>N: lista dos P escores máximos obtidos sobre permutações de S′</p>
<p>a: alinhamento = (forma T, pares de posições alinhadas, escore)</p>
<p>1 C ← ∅</p>
<p>2 para cada voz u de A e cada voz v de B faça ▹ 16 pares</p>
<p>3 S ← Representa(u); S′ ← Representa(v) ▹ Eq. 4</p>
<p>4 I ← ConstroiIndice(S, k)</p>
<p>5 R ← Busca(I, S, S′, θ)</p>
<p>6 N ← lista vazia</p>
<p>7 para t ← 1 até P faça</p>
<p>8 π ← permutação aleatória de S′ ▹ gerador iniciado com σ</p>
<p>9 M ← maior escore em Busca(I, S, π, θ), ou 0 se vazio</p>
<p>10 acrescente M a N</p>
<p>11 para cada a ∈ R com |a| ≥ ℓmin faça</p>
<p>12 se ValorP(escore(a), N, P) ≤ p* então ▹ Eq. 8</p>
<p>13 C ← C ∪ Rotula(a, u, v) ▹ um ou mais segmentos</p>
<p>14 retorne C</p>
<p>Função ConstroiIndice(S, k)</p>
<p>1 I ← tabela hash vazia</p>
<p>2 para cada T ∈ {Id, Inv, Ret, RetInv} faça</p>
<p>3 Sᵀ ← T(S) ▹ Eq. 5 e 6</p>
<p>4 para i ← 1 até |Sᵀ| − k + 1 faça</p>
<p>5 w ← (δᵢ, …, δᵢ₊ₖ₋₁) de Sᵀ</p>
<p>6 se w não é de baixa complexidade então ▹ Seção 5.1.2</p>
<p>7 acrescente (i, T) a I[w]</p>
<p>8 retorne I</p>
<p>Função Busca(I, S, S′, θ)</p>
<p>1 R ← ∅</p>
<p>2 para j ← 1 até |S′| − k + 1 faça</p>
<p>3 w′ ← (δ′ⱼ, …, δ′ⱼ₊ₖ₋₁) de S′</p>
<p>4 para cada (i, T) ∈ I[w′] faça ▹ hit</p>
<p>5 se nenhum a ∈ R de forma T contém o par (i, j) então</p>
<p>6 R ← R ∪ { Estende(T(S), S′, i, j, T, θ) }</p>
<p>7 retorne R</p>
<p>Função Estende(Q, Z, i, j, T, θ)</p>
<p>▹ a semente ocupa Q[i … i+k−1] e Z[j … j+k−1]</p>
<p>1 s₀ ← Σ s(Q[i+t], Z[j+t]), para t = 0 … k−1 ▹ Eq. 7</p>
<p>2 (s_d, caminho_d) ← ExtensaoXDrop(Q[i+k …], Z[j+k …], θ)</p>
<p>3 (s_e, caminho_e) ← ExtensaoXDrop(reverso de Q[… i−1],</p>
<p>reverso de Z[… j−1], θ)</p>
<p>4 retorne (T, caminho_e + semente + caminho_d, s₀ + s_d + s_e)</p>
<p>Função ExtensaoXDrop(Q, Z, θ)</p>
<p>▹ alinha prefixos de Q e Z com gaps; células inexistentes</p>
<p>▹ ou podadas valem −∞</p>
<p>1 H(0, 0) ← 0; Hmax ← 0; melhor ← (0, 0)</p>
<p>2 para p ← 0 até |Q| faça</p>
<p>3 para q ← 0 até |Z|, exceto (p, q) = (0, 0), faça</p>
<p>4 H(p, q) ← máx { H(p−1, q−1) + s(Q[p], Z[q]),</p>
<p>H(p−1, q) − g, H(p, q−1) − g } ▹ Eq. 1 e 7</p>
<p>5 se H(p, q) &lt; Hmax − X então H(p, q) ← −∞ ▹ Eq. 3: poda</p>
<p>6 senão, se H(p, q) &gt; Hmax então</p>
<p>7 Hmax ← H(p, q); melhor ← (p, q)</p>
<p>8 se todas as células da linha p foram podadas então interrompa</p>
<p>9 retorne (Hmax, traceback de melhor até (0, 0))</p>
<p>Função ValorP(S, N, P)</p>
<p>1 retorne (1 + número de M ∈ N com M ≥ S) / (1 + P) ▹ Eq. 8</p>
<p>Função Rotula(a, u, v) ▹ Seção 5.1.4</p>
<p>1 para cada par alinhado, calcula a diferença de altura, em graus,</p>
<p>entre os eventos de u e de v</p>
<p>2 divide a em sequências maximais de pares com a mesma diferença</p>
<p>3 rotula cada segmento com a forma T e como idêntico (diferença nula)</p>
<p>ou transposição (intervalo em semitons); acrescenta variação</p>
<p>rítmica se as proporções rítmicas do segmento divergem</p>
<p>4 retorne os segmentos rotulados</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Fonte: elaborado pelo autor (2026).

Essa estimativa não pretende justificar a heurística, possibilidade já descartada na Seção 5.1.5 para sequências do tamanho de um coral. Ela tem dois propósitos: verificar que o teste de permutação, que repete a busca P vezes, é compatível com o RNF03 e indicar em que cenário a diferença em relação ao alinhamento exato passa a pesar. Sejam n e m os tamanhos das duas vozes, k o tamanho da semente, h o número de *hits* e L·w a área da matriz efetivamente explorada em cada extensão, limitada pelo X-drop. A construção do índice custa O(nk), com quatro formas por semente. A busca custa O(mk) em consultas ao índice, mais O(h·L·w) em extensões; a condição da linha 5 da função Busca evita estender repetidamente *hits* que já pertencem a um alinhamento encontrado. O custo por par de vozes é, portanto, O(nk + (P + 1)(mk + h·L·w)), multiplicado pelos 16 pares. O fator P + 1 domina essa expressão: com o ponto de partida P = 999 (Seção 5.6.3), a busca é executada mil vezes por par de vozes, e é ele, mais do que o tamanho das vozes, que decide se o RNF03 é atendido. O Smith-Waterman iterativo, com R rodadas de mascaramento, custa O((P + 1)·R·nm) por par, e o mesmo fator P + 1 se aplica a ele. A diferença assintótica entre as duas abordagens só passa a pesar na busca de um motivo contra o corpus inteiro, de tamanho total N: o custo do alinhamento exato cresce com O(n·N), enquanto o da heurística depende de N apenas pela varredura de sementes, O(Nk), mais as extensões em torno dos *hits*.

1.  <span id="_Toc990000045" class="anchor"></span>Elicitação de Requisitos

Por se tratar de uma ferramenta de análise sem interface de usuário final, os requisitos abaixo descrevem o comportamento esperado do protótipo como um todo — não telas ou fluxos de interação gráfica.

1.  <span id="_Toc990000046" class="anchor"></span>Requisitos Funcionais

**RF01.** O sistema deve receber como entrada duas versões simbólicas, em formato MusicXML, de uma mesma composição musical.

**RF02.** O sistema deve extrair, de cada voz das duas versões, uma sequência de eventos musicais representada por intervalos melódicos diatônicos e proporções rítmicas, preservando o intervalo cromático correspondente a cada intervalo e a altura absoluta de cada evento.

**RF03.** O sistema deve gerar sementes de tamanho fixo a partir da componente de intervalos diatônicos da sequência de uma das versões, descartar ou reduzir o peso das sementes de baixa complexidade e indexar as demais, incluindo suas variantes sob inversão, retrogradação e retrógrado da inversão.

**RF04.** O sistema deve localizar, na sequência da outra versão, ocorrências (*hits*) das sementes indexadas.

**RF05.** O sistema deve estender cada *hit* em ambas as direções por alinhamento com *gaps*, acumulando pontuação e interrompendo a extensão segundo o critério de *X-drop*.

**RF06.** O sistema deve reportar apenas as correspondências que atinjam um comprimento mínimo e cujo escore supere um limiar de significância estimado empiricamente, por alinhamento contra permutações aleatórias da sequência comparada.

**RF07.** O sistema deve produzir um relatório estruturado das correspondências identificadas, contendo localização em cada versão, tipo de transformação (transposição, inversão, retrogradação, variação rítmica ou combinação) e pontuação, incluindo o intervalo de transposição, quando houver; uma correspondência que reúna trechos com transformações diferentes é desdobrada em segmentos rotulados separadamente.

**RF08.** O sistema deve aplicar o alinhamento a todas as combinações entre as vozes das duas versões, e não apenas às vozes de mesmo nome.

**RF09.** O sistema deve permitir a configuração dos parâmetros do método descritos na Seção 5.6.3, adotando valores padrão para os parâmetros não informados e registrando no relatório os valores utilizados.

**RF10.** O sistema deve exportar o relatório de correspondências nos formatos CSV e JSON.

**RF11.** O sistema deve calcular, quando fornecido o gabarito de um par de versões, os critérios de avaliação definidos na Seção 5.6.4.

**RF12.** O sistema deve executar, sobre os mesmos pares de vozes, a referência de alinhamento exato por Smith-Waterman iterativo descrita na Seção 5.6.4, para comparação com o método.

2.  <span id="_Toc990000047" class="anchor"></span>Requisitos Não Funcionais

**RNF01.** O sistema deve ser operável via linha de comando ou como biblioteca importável, dispensando interface gráfica.

**RNF02.** O sistema deve ser determinístico: a mesma entrada e os mesmos parâmetros devem produzir sempre o mesmo relatório de saída. Para isso, as permutações do teste de significância são geradas a partir de uma semente fixa do gerador de números aleatórios, que integra os parâmetros θ e é registrada no relatório.

**RNF03.** O sistema deve processar um par de corais de Bach em tempo hábil para uso interativo em uma sessão de análise.

**RNF04.** O sistema deve depender exclusivamente de bibliotecas Python de código aberto, com o music21 (CUTHBERT; ARIZA, 2010) como dependência central para leitura e manipulação simbólica.

**RNF05.** O sistema deve ser estruturado de modo a permitir, no futuro, a adição de outros formatos de entrada (\*\*kern, MEI) sem alteração do núcleo do algoritmo de alinhamento.

<span class="mark">NOTA: RNF03 depende de parâmetros (tamanho da semente, limiar de *X-drop*, custo de *gap*, critério de baixa complexidade, limiar de significância e comprimento mínimo) ainda não fixados — decisão adiada para a calibração no TCC II (Seção 5.6.3)</span>

2.  <span id="_Toc990000048" class="anchor"></span>Diagrama de Caso de Uso

O protótipo possui um único ator, o **Pesquisador/Editor**, que interage com o sistema por linha de comando ou importando-o como biblioteca (RNF01). A Figura 3 apresenta os casos de uso derivados dos requisitos funcionais da Seção 5.2.1, e o Quadro 4 descreve cada um deles e os requisitos que atende, de modo que todo requisito funcional tenha ao menos um caso de uso correspondente. Os casos de uso UC03.1 a UC03.4 correspondem às quatro etapas do método (Seção 5.1): não são acionados isoladamente pelo ator, mas incluídos (relação *include*) em *Executar alinhamento*, e foram explicitados para tornar rastreável a correspondência entre cada etapa e seu requisito. *Exportar relatório* estende (relação *extend*) *Consultar relatório de correspondências*, pois ocorre apenas quando o ator solicita a gravação dos resultados em arquivo. *Avaliar resultados com gabarito* é usado apenas sobre os pares de teste descritos na Seção 5.6.2.

<img src="media/image4.png" style="width:6.01487in;height:4.22096in" alt="Diagrama de caso de uso do protótipo" />

3.  <span id="_Toc990000049" class="anchor"></span>Diagrama de caso de uso do protótipo de alinhamento motívico

Fonte: elaborado pelo autor (2026).

4.  <span id="_Toc990000050" class="anchor"></span>Descrição dos casos de uso do protótipo

| **Caso de uso**                                | **Descrição**                                                                                                                                                                                        | **Requisitos**                            |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| UC01 – Submeter par de versões                 | O ator informa os caminhos de dois arquivos MusicXML (Versão A e Versão B). O sistema verifica se ambos podem ser lidos e se contêm as quatro vozes; em caso de falha, informa o arquivo e o motivo. | RF01                                      |
| UC02 – Configurar parâmetros do método         | Opcional. O ator define os parâmetros θ da Seção 5.6.3. Parâmetros não informados assumem valores padrão, registrados no relatório.                                                                  | RF09                                      |
| UC03 – Executar alinhamento                    | O ator dispara o processamento, que executa UC03.1 a UC03.4 para cada uma das 16 combinações de vozes entre as duas versões.                                                                         | RF08; RF02 a RF06, por meio das inclusões |
| UC03.1 – Extrair representação                 | Converte cada voz em uma sequência de intervalos diatônicos e proporções rítmicas, preservando os intervalos cromáticos, as alturas absolutas e a localização de cada evento (Seção 5.1.1).          | RF02                                      |
| UC03.2 – Indexar sementes e mascarar           | Gera as sementes da versão de consulta e suas variantes sob inversão, retrogradação e retrógrado da inversão, descarta as de baixa complexidade e registra as demais no índice (Seção 5.1.2).        | RF03                                      |
| UC03.3 – Buscar e estender com gaps            | Localiza os *hits* na outra versão e estende cada um em ambas as direções, admitindo espaços, até o critério de X-drop (Seção 5.1.3).                                                                | RF04, RF05                                |
| UC03.4 – Filtrar por significância             | Estima o valor-p de cada alinhamento por permutação e descarta os que não atingem p\* ou o comprimento mínimo (Seção 5.1.4).                                                                         | RF06                                      |
| UC04 – Consultar relatório de correspondências | O ator obtém as correspondências, com localização em cada versão, tipo de transformação, intervalo de transposição e pontuação (Quadro 6).                                                           | RF07                                      |
| UC05 – Exportar relatório                      | Extensão de UC04: grava o relatório nos formatos CSV e JSON (Seção 5.5).                                                                                                                             | RF10                                      |
| UC06 – Avaliar resultados com gabarito         | O ator fornece o gabarito de um par de teste (Seção 5.6.2); o sistema calcula os critérios da Seção 5.6.4 para o método e para a referência de Smith-Waterman.                                       | RF11, RF12                                |

Fonte: elaborado pelo autor (2026).

1.  <span id="_Toc990000051" class="anchor"></span>Projeto do Protótipo

O protótipo é organizado em seis componentes, distribuídos em quatro camadas — interface, entrada, alinhamento e saída —, conforme a Figura 4. Cinco deles correspondem às quatro etapas descritas na Seção 5.1, com a leitura e a extração de representação tratadas como componentes distintos; o sexto, na camada de interface, recebe as solicitações do usuário:

– **Interface de Linha de Comando/API**: recebe os caminhos das duas versões e os parâmetros θ (UC01 e UC02), valida-os, completa os parâmetros não informados com valores padrão e repassa a cada componente apenas os parâmetros de que ele depende.

– **Leitor MusicXML**: interface com o music21 para carregar os arquivos de entrada e extrair as vozes de cada versão.

– **Extrator de Representação**: converte cada voz em uma sequência de intervalos diatônicos e proporções rítmicas, preservando os intervalos cromáticos, as alturas absolutas e a localização de cada evento, e deriva as variantes sob inversão, retrogradação e retrógrado da inversão.

– **Indexador de Sementes**: aplica o filtro de baixa complexidade e constrói a tabela de posições das sementes extraídas da versão de consulta.

– **Motor de Busca e Extensão**: localiza *hits* e executa a extensão com *gaps* e *X-drop* para cada combinação de vozes.

– **Pontuador e Gerador de Relatório**: estima a significância empírica por permutação, aplica o comprimento mínimo, traduz as posições alinhadas em compasso e posição e produz a saída estruturada, exportada em CSV e JSON.

Essa divisão em componentes independentes tem uma motivação adicional além da clareza arquitetural: isola a lógica de alinhamento (Motor de Busca e Extensão) da representação simbólica de entrada (Leitor MusicXML, Extrator de Representação), o que sustenta a extensibilidade a outros formatos prevista em RNF05. A Figura 4 apresenta esses componentes e suas dependências.

A integração entre as camadas segue um fluxo único e unidirecional: cada componente recebe do anterior uma estrutura de dados definida e entrega outra ao seguinte, sem acessar o estado interno dos demais. Essas estruturas correspondem às classes do diagrama da Figura 5, e o Quadro 5 descreve o que cada componente recebe e entrega. Duas dependências atravessam as camadas fora desse fluxo principal. A primeira é o conjunto de parâmetros θ, recebido pela camada de interface e lido apenas pelos componentes que dependem dele: o tamanho da semente k e o critério de baixa complexidade pelo Indexador; os pesos α, β, γ e ρ, a penalidade g e o limiar X pelo Motor; e P, p\* e ℓmin pelo Pontuador. A segunda é a localização de cada evento na partitura (compasso e posição), registrada pelo Extrator: como o alinhamento opera sobre índices das sequências, e não sobre compassos, o Pontuador consulta essa informação para traduzir cada alinhamento em uma correspondência localizável nas duas versões (Quadro 6).

<img src="media/image5.png" style="width:6.2336in;height:4.27384in" alt="Diagrama de componentes do protótipo" />

4.  <span id="_Toc990000052" class="anchor"></span>Diagrama de componentes do protótipo, organizado em camadas, com os dados trocados entre os componentes

Fonte: elaborado pelo autor (2026).

5.  <span id="_Toc990000053" class="anchor"></span>Interfaces entre os componentes do protótipo

| **Componente**                    | **Recebe**                                                                                     | **Entrega**                                                                                                           |
|-----------------------------------|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Interface de Linha de Comando/API | Caminhos das duas versões e parâmetros θ informados pelo usuário                               | Caminhos validados; θ completo, com valores padrão                                                                    |
| Leitor MusicXML                   | Caminhos das duas versões                                                                      | Uma partitura por versão (objeto Score do music21), separada em quatro vozes                                          |
| Extrator de Representação         | Partituras das duas versões                                                                    | Uma SequenciaVoz por voz: sequência de (δ, c, r), altura absoluta e localização de cada evento                        |
| Indexador de Sementes             | SequenciaVoz da versão de consulta; k e critério de baixa complexidade                         | IndiceSementes: posições de cada semente não mascarada, nas formas Id, Inv, Ret e RetInv                              |
| Motor de Busca e Extensão         | IndiceSementes; SequenciaVoz das duas versões; α, β, γ, ρ, g e X                               | Hits e Alinhamentos (trechos em A e B, escore e gaps) para cada um dos 16 pares de vozes                              |
| Pontuador e Gerador de Relatório  | Alinhamentos; escores máximos obtidos sobre P permutações; p\* e ℓmin; localização dos eventos | Correspondencias com valor-p, rótulo de transformação e localização, reunidas no Relatorio e exportadas em CSV e JSON |

Fonte: elaborado pelo autor (2026).

O diagrama de classes da Figura 5 detalha as estruturas de dados que implementam esses componentes: a representação de cada voz (SequenciaVoz, composta de objetos Evento), o índice de sementes, os hits e alinhamentos produzidos pela classe Alinhador e as correspondências que compõem o relatório final.

<img src="media/image6.png" style="width:5.35871in;height:5.32248in" alt="Diagrama de classes do protótipo" />

5.  <span id="_Toc990000054" class="anchor"></span>Diagrama de classes do protótipo de alinhamento motívico

Fonte: elaborado pelo autor (2026).

1.  <span id="_Toc990000055" class="anchor"></span>Formato de Saída dos Resultados

O relatório produzido pelo protótipo organiza cada correspondência motívica identificada em uma ou mais linhas, uma por segmento rotulado (Seção 5.1.4), com as colunas descritas no Quadro 6.

6.  <span id="_Toc990000056" class="anchor"></span>Campos do relatório de correspondências

| **Campo**              | **Descrição**                                                                                                                                                                                                                          |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID do motivo           | Identificador sequencial da correspondência                                                                                                                                                                                            |
| Localização (Versão A) | Voz, compasso e posição de início/fim na primeira versão                                                                                                                                                                               |
| Localização (Versão B) | Voz, compasso e posição de início/fim na segunda versão                                                                                                                                                                                |
| Transformação          | Tipo identificado: transposição, inversão, retrogradação, variação rítmica ou combinação, com o intervalo de transposição, quando aplicável; uma correspondência com trechos de transformações diferentes ocupa uma linha por segmento |
| Pontuação              | Escore de alinhamento resultante da etapa de extensão                                                                                                                                                                                  |

Fonte: elaborado pelo autor (2026).

O relatório é exportado em dois formatos (RF10). O formato CSV contém uma linha por segmento, com as colunas do Quadro 6, e destina-se à inspeção em planilhas e à análise estatística dos resultados. O formato JSON preserva a estrutura completa de cada correspondência, incluindo o alinhamento evento a evento e o valor-p, e registra os parâmetros θ usados na execução, o que o torna adequado ao consumo por outros programas e à reprodução dos resultados (RNF02).

1.  <span id="_Toc990000057" class="anchor"></span>Planejamento da Avaliação

Esta seção reúne o planejamento da avaliação do método, que será executada no TCC II: o corpus (Seção 5.6.1), a construção dos pares de versões usados nos testes (Seção 5.6.2), os parâmetros a calibrar (Seção 5.6.3) e os critérios objetivos de avaliação (Seção 5.6.4). O planejamento é apresentado depois da modelagem porque cada um desses elementos depende do método descrito nas seções anteriores, e é descrito com detalhe suficiente para que outro pesquisador possa reproduzir a avaliação.

1.  <span id="_Toc990000058" class="anchor"></span>Corpus

O corpus deste trabalho é composto pelos corais a quatro vozes de J. S. Bach distribuídos com o music21 (CUTHBERT; ARIZA, 2010). A coleção de referência desses corais, na numeração de Riemenschneider, reúne 371 peças, mas nem todas estão disponíveis na biblioteca. Um levantamento preliminar feito pelo autor sobre a versão 10.5 do music21 identificou 433 arquivos atribuídos a Bach, dos quais 365, em MusicXML, correspondem a corais a quatro vozes.[^3] Esse é o conjunto efetivamente utilizado. O corpus é de domínio público e distribuído nativamente em MusicXML pela ferramenta, o que dispensa etapas de conversão de formato para o protótipo descrito nas seções anteriores. Arquivos que codificam o mesmo coral em formatos diferentes são tratados como duplicatas e excluídos.

2.  <span id="_Toc990000059" class="anchor"></span>Construção dos Pares de Versões para Teste

Conforme indicado na Delimitação do problema (Seção 1.2), os pares de versões usados para testar o protótipo podem ser constituídos a partir de variantes documentadas na tradição de fontes dos corais, de transformações geradas programaticamente sobre o corpus, de harmonizações diferentes de uma mesma melodia, ou de uma combinação dessas fontes. Este trabalho adota dois conjuntos de teste complementares. O primeiro, e principal, é construído programaticamente: a partir de um coral do corpus (Versão A), gera-se uma Versão B aplicando, a um ou mais trechos motívicos selecionados, uma ou mais das transformações consideradas (transposição, inversão, retrogradação, variação rítmica e inserção ou remoção de notas), mantendo o restante da voz estruturalmente inalterado. A localização exata e o tipo de transformação aplicada em cada par gerado são registrados como gabarito (*ground truth*) — informação indisponível quando se depende exclusivamente de variantes históricas reais, mas indispensável para o cálculo dos critérios objetivos de avaliação propostos na Seção 5.6.4. No caso da transposição, o gabarito registra também se ela é real ou tonal (Seção 5.1.4). Os trechos não transformados também integram o gabarito, como segmentos idênticos entre as duas versões.

Essa estratégia tem uma limitação metodológica que vale reconhecer: os mesmos mecanismos que o protótipo usa para tolerar as quatro transformações consideradas — invariância por construção da representação, no caso da transposição; indexação de variantes, no caso de inversão e retrogradação; tolerância na etapa de pontuação, no caso da variação rítmica; e extensão com gaps, no caso da inserção ou remoção de notas (Seção 5.1) — são também os mecanismos usados para gerar os pares de teste sintéticos. Por isso, o desempenho do protótipo sobre esses pares valida principalmente a correção da implementação de cada mecanismo, não necessariamente sua capacidade de generalizar para variantes reais e não documentadas, que podem envolver combinações de transformações mais complexas ou irregularidades que esses mecanismos não antecipam. Essa limitação é inerente à etapa de design deste trabalho. O segundo conjunto de teste, descrito a seguir, a mitiga parcialmente; a inclusão de transformações não triviais nos pares sintéticos fica como direção para trabalhos futuros.

O segundo conjunto de teste é formado por pares reais extraídos do próprio corpus. Bach harmonizou muitas melodias de coral mais de uma vez, em obras e tonalidades diferentes. A melodia conhecida como coral da Paixão, por exemplo, aparece harmonizada cinco vezes na Paixão segundo São Mateus (BWV 244.15, 244.17, 244.44, 244.54 e 244.62), além de outras harmonizações no mesmo corpus. Um levantamento preliminar feito pelo autor agrupou os corais cujo soprano começa pela mesma sequência de dez intervalos diatônicos e identificou 63 melodias com duas ou mais harmonizações, somando 175 arquivos. A contagem é conservadora, porque o critério não agrupa harmonizações cujo início difere por uma nota de passagem. É o caso do próprio BWV 244.62, cujo soprano se afasta das demais harmonizações já no nono intervalo: ele não entra na contagem, mas é incluído no conjunto de teste por identificação direta. Conforme a definição apresentada na Delimitação do problema (Seção 1.2), harmonizações diferentes de uma mesma melodia são tratadas como versões dessa melodia.

Esses pares não têm gabarito completo, mas têm um gabarito parcial conhecido de antemão: o soprano de uma harmonização deve corresponder, do início ao fim, ao soprano da outra, com um intervalo de transposição dado pela diferença de tonalidade. Contêm também variantes reais que o método precisa absorver. Entre as harmonizações do coral da Paixão, o soprano varia de 42 a 56 notas na codificação do corpus, o que indica notas de passagem e alterações rítmicas acrescentadas, e o BWV 244.62, como já observado, diverge das demais a partir do nono intervalo. As vozes internas, por outro lado, são reescritas a cada harmonização e não têm gabarito; as correspondências encontradas nelas são examinadas qualitativamente. Esse conjunto não substitui os pares sintéticos, mas testa o método sobre variações que ele próprio não gerou.

Variantes documentadas na tradição de fontes dos corais, como a mudança de tonalidade entre fontes mencionada na Justificativa (Seção 1.4), entram como complemento ilustrativo, e não como base principal de avaliação. O corpus contém ao menos um caso desse tipo: o coral BWV 18.5, quinto movimento da cantata BWV 18, codificado em dois arquivos que correspondem às versões de Weimar e de Leipzig da cantata. Para a apresentação em Leipzig, a cantata foi transposta para lá menor (DAHN, 2019), e os dois arquivos registram a mesma harmonização a um tom de distância. Um levantamento feito pelo autor com o music21 sobre os dois arquivos mostra que soprano e baixo são idênticos em intervalos e ritmo; no contralto e no tenor, três notas da versão de Leipzig aparecem divididas em duas notas repetidas na versão de Weimar. O par tem, portanto, gabarito completo conhecido de antemão (transposição real de dois semitons em todas as vozes e três divisões rítmicas pontuais) e testa em particular o tratamento aproximado da fragmentação por meio de *gaps* (Seção 5.1.3).

3.  <span id="_Toc990000060" class="anchor"></span>Parâmetros do Método de Alinhamento

O método descrito nas seções anteriores depende de sete grupos de parâmetros: o tamanho da semente; o critério de baixa complexidade aplicado às sementes; os pesos de pontuação atribuídos a coincidências e divergências diatônicas, cromáticas e rítmicas; o custo de *gap*; o limiar de *X-drop*; o limiar de significância empírica p\*, com o número de permutações P usado para estimá-lo; e o comprimento mínimo de uma correspondência reportada. Nenhum deles é fixado a priori neste trabalho. Todos serão calibrados empiricamente no TCC II, por meio de execuções piloto.

Para que a calibração não contamine a avaliação, o corpus é dividido em dois subconjuntos disjuntos: um de calibração, sobre o qual os parâmetros são ajustados, e outro de avaliação, sobre o qual os critérios da Seção 5.6.4 são calculados. Sem essa separação, o desempenho medido refletiria em parte o próprio ajuste dos parâmetros aos pares avaliados.

Alguns pontos de partida orientam a calibração. Para o tamanho da semente, adota-se como hipótese de trabalho que motivos relevantes nos corais têm poucos eventos, da ordem de três a cinco intervalos; a hipótese será verificada na própria calibração. Como a semente é definida apenas sobre intervalos diatônicos (Seção 5.1.2), seu tamanho pesa mais na seletividade da busca. Uma semente curta demais, somada à condução predominantemente conjunta das vozes, tende a gerar muitos *hits* espúrios, efeito que o filtro de baixa complexidade atenua, mas não elimina. Para a significância, um ponto de partida é adotar p\* = 0,01, o que equivale a exigir que o escore de uma correspondência supere o percentil 99 da distribuição de máximos obtida com as sequências permutadas (Seção 5.1.4), com P = 999 permutações, número que permite resolver valores-p de até 0,001.

<span class="mark">DEFINIR NO TCC II: valores definitivos dos sete grupos de parâmetros e critério de divisão do corpus entre calibração e avaliação, conforme descrito acima</span>

4.  <span id="_Toc990000061" class="anchor"></span>Critérios Objetivos de Avaliação

Em atendimento ao quinto objetivo específico deste trabalho, propõem-se os seguintes critérios objetivos para avaliação das correspondências motívicas identificadas pelo protótipo, calculáveis a partir do gabarito descrito na Seção 5.6.2:

– **Precisão**: proporção dos segmentos reportados pelo protótipo que efetivamente correspondem a um segmento do gabarito.

– **Cobertura (*recall*)**: proporção dos segmentos do gabarito que foram efetivamente identificados pelo protótipo.

– **Medida-F**: média harmônica entre precisão e cobertura, combinando os dois critérios anteriores em uma única medida.

– **Acurácia de classificação da transformação**: entre os segmentos corretamente identificados, a proporção em que o tipo de transformação relatado pelo protótipo (transposição, inversão, retrogradação, variação rítmica ou combinação) corresponde ao tipo efetivamente injetado.

Além dessas métricas, o método é comparado a uma referência de alinhamento exato. O algoritmo de Smith-Waterman (1981) é aplicado aos mesmos pares de vozes, com o mesmo esquema de pontuação e também contra as formas Inv, Ret e RetInv da versão de consulta, de forma iterativa: a cada rodada, o trecho já alinhado é mascarado, de modo a produzir múltiplas correspondências. Seus resultados passam pelos mesmos critérios. A comparação responde à pergunta levantada na Seção 5.1.5: quanto a heurística perde em cobertura em troca das vantagens que a justificam. Para isso, mede-se a proporção das correspondências encontradas pela referência exata que também são encontradas pela heurística, ao lado do tempo de execução de cada abordagem.

No segundo conjunto de teste, em que o gabarito é parcial, as métricas são calculadas apenas sobre o soprano. A cobertura mede a proporção da melodia de uma harmonização alinhada à melodia da outra, e a acurácia de classificação verifica se o intervalo de transposição relatado corresponde à diferença de tonalidade entre as duas harmonizações.

Os critérios de precisão e cobertura dependem de uma definição operacional de correspondência correta: um segmento reportado pelo protótipo é considerado correto quando sua sobreposição com um segmento do gabarito — a proporção de posições em comum entre o trecho relatado e o trecho do gabarito — atinge um limiar mínimo. O valor exato desse limiar será calibrado empiricamente junto aos demais parâmetros do método (Seção 5.6.3); um ponto de partida razoável, a ajustar conforme os resultados piloto, é exigir sobreposição de ao menos metade das posições do trecho do gabarito.

A unidade de avaliação é, portanto, o segmento rotulado (Seção 5.1.4), e não a correspondência inteira. Como o gabarito inclui os trechos não transformados, um segmento idêntico reportado sobre um trecho inalterado conta como acerto, e não como falso positivo. Para que esses segmentos, que formam a maior parte de cada voz, não inflem os resultados, as métricas são calculadas também separadamente sobre os segmentos transformados e por tipo de transformação, que são o objeto principal da avaliação.

Consistente com a Delimitação do problema (Seção 1.2) e com o quinto objetivo específico, este trabalho propõe esses critérios, a serem aplicados preliminarmente aos resultados obtidos após a implementação do protótipo, no TCC II; mesmo então, esses critérios não constituirão uma validação experimental extensiva sobre a totalidade do corpus.

2.  <span id="_Toc990000062" class="anchor"></span>Considerações do Capítulo

A modelagem apresentada neste capítulo traduz em software o método de alinhamento motívico fundamentado nos capítulos anteriores: uma ferramenta de linha de comando organizada em seis componentes, distribuídos em quatro camadas, dos quais o Motor de Busca e Extensão concentra a adaptação da heurística *seed-and-extend* do BLAST (Capítulo 3) ao domínio simbólico musical. A modelagem situa-se no nível arquitetural e deixa em aberto os parâmetros concretos do algoritmo, como o tamanho da semente, o limiar de X-drop e os pesos de pontuação. O capítulo planejou também a avaliação do método: dois conjuntos de teste complementares, um de pares sintéticos com gabarito completo e outro de harmonizações diferentes de uma mesma melodia, com gabarito parcial; os sete grupos de parâmetros, a calibrar no TCC II sobre um subconjunto do corpus separado do usado na avaliação; e os critérios objetivos de avaliação, acompanhados da comparação com o Smith-Waterman como referência exata. O capítulo seguinte apresenta o cronograma que organiza essas etapas.

6.  <span id="_Toc990000063" class="anchor"></span>CRONOGRAMA

Este capítulo apresenta o cronograma do trabalho em dois quadros, no formato definido pelo modelo institucional: o Quadro 7, do TCC I, de agosto a dezembro de 2026, e o Quadro 8, do TCC II, de fevereiro a julho de 2027.

1.  <span id="_Toc990000064" class="anchor"></span>Cronograma do TCC I

O TCC I tem entrega prevista para 15 de novembro de 2026. Quatro reuniões de orientação foram distribuídas ao final das etapas de maior densidade de conteúdo: na primeira semana de setembro, na última de setembro, na terceira de outubro e na primeira de novembro. As atividades e seus meses de execução estão no Quadro 7.

7.  <span id="_Toc990000065" class="anchor"></span>Cronograma do TCC I, de 08/2026 a 12/2026

| **Projeto**                                                                | **Cronograma** |              |              |              |              |
|----------------------------------------------------------------------------|----------------|--------------|--------------|--------------|--------------|
| **Atividades**                                                             | **ago/2026**   | **set/2026** | **out/2026** | **nov/2026** | **dez/2026** |
| Fundamentação teórica e trabalhos relacionados (Capítulos 2 a 4)           |                |              |              |              |              |
| Modelagem do protótipo (Capítulo 5)                                        |                |              |              |              |              |
| Procedimentos metodológicos e planejamento da avaliação (Seções 1.5 e 5.6) |                |              |              |              |              |
| Cronograma e orçamento (Capítulos 6 e 7)                                   |                |              |              |              |              |
| Revisão geral e validação com orientação                                   |                |              |              |              |              |
| Formatação final e entrega do relatório                                    |                |              |              |              |              |
| Apresentação do TCC I                                                      |                |              |              |              |              |

Fonte: elaborado pelo autor (2026).

1.  <span id="_Toc990000066" class="anchor"></span>Cronograma do TCC II

O TCC II abrange a implementação do protótipo, a construção dos conjuntos de teste e a aplicação preliminar dos critérios de avaliação, etapas já delimitadas no Capítulo 5 e na Seção 1.5. O Quadro 8 distribui essas atividades de fevereiro a julho de 2027.

8.  <span id="_Toc990000067" class="anchor"></span>Cronograma do TCC II, de 02/2027 a 07/2027

| **Projeto**                                                  | **Cronograma** |              |              |              |              |              |
|--------------------------------------------------------------|----------------|--------------|--------------|--------------|--------------|--------------|
| **Atividades**                                               | **fev/2027**   | **mar/2027** | **abr/2027** | **mai/2027** | **jun/2027** | **jul/2027** |
| Implementação do protótipo e da referência de Smith-Waterman |                |              |              |              |              |              |
| Construção dos conjuntos de teste e divisão do corpus        |                |              |              |              |              |              |
| Calibração dos parâmetros                                    |                |              |              |              |              |              |
| Avaliação preliminar e análise dos resultados                |                |              |              |              |              |              |
| Redação dos capítulos de resultados e conclusão              |                |              |              |              |              |              |
| Entrega da monografia                                        |                |              |              |              |              |              |
| Defesa                                                       |                |              |              |              |              |              |

Fonte: elaborado pelo autor (2026).

7.  <span id="_Toc990000068" class="anchor"></span>ORÇAMENTO

Este trabalho não prevê custos com aquisição de equipamentos, licenças ou assinaturas de software. O protótipo será desenvolvido em Python com bibliotecas de código aberto, tendo o music21 (CUTHBERT; ARIZA, 2010) como dependência central; o corpus de corais de Bach é de domínio público e distribuído com essa mesma biblioteca; e o desenvolvimento usa o computador pessoal do autor. Eventuais despesas não previstas, inclusive com a obtenção de fontes bibliográficas, serão assumidas pelo próprio estudante.

1.  <span id="_Toc990000069" class="anchor"></span>Referências

ALMADA, C. O conceito de variação em desenvolvimento no primeiro movimento da Sonata para Piano op. 2/1, de Beethoven. **Música Hodie**, v. 8, n. 2, p. 83-94, 2008.

ALTSCHUL, S. F. et al. Basic local alignment search tool. **Journal of Molecular Biology**, v. 215, n. 3, p. 403-410, 1990.

ALTSCHUL, S. F. et al. Gapped BLAST and PSI-BLAST: a new generation of protein database search programs. **Nucleic Acids Research**, v. 25, n. 17, p. 3389-3402, 1997.

BOUNTOURIDIS, D. et al. Melody retrieval and classification using biologically-inspired techniques. In: CORREIA, J.; CIESIELSKI, V.; LIAPIS, A. (ed.). **Computational intelligence in music, sound, art and design**: EvoMUSART 2017. Cham: Springer, 2017. p. 49-64. (Lecture Notes in Computer Science, v. 10198).

CUTHBERT, M. S.; ARIZA, C. Music21: a toolkit for computer-aided musicology and symbolic music data. In: INTERNATIONAL SOCIETY FOR MUSIC INFORMATION RETRIEVAL CONFERENCE (ISMIR), 11., 2010, Utrecht. **Anais \[...\]**. \[S.l.\]: ISMIR, 2010. p. 637-642.

DAHN, L. Chorales appearing in different keys in early collections. In: DAHN, L. **The four-part chorales of J. S. Bach**. \[S.l.\], 2017. Disponível em: https://bach-chorales.com/ChoraleKeys.htm. Acesso em: 27 out. 2026.

DAHN, L. BWV 18.5. In: DAHN, L. **The four-part chorales of J. S. Bach**. \[S.l.\], 2019. Disponível em: https://bach-chorales.com/BWV0018_5.htm. Acesso em: 27 out. 2026.

DOWLING, W. J. Recognition of melodic transformations: inversion, retrograde, and retrograde inversion. **Perception & Psychophysics**, v. 12, p. 417-421, 1972.

FOSCARIN, F.; JACQUEMARD, F.; FOURNIER-S'NIEHOTTA, R. A *diff* procedure for music score files. In: INTERNATIONAL CONFERENCE ON DIGITAL LIBRARIES FOR MUSICOLOGY (DLfM), 6., 2019, Haia. **Anais \[...\]**. New York: ACM, 2019. p. 58-64.

FRISCH, W. **Brahms and the principle of *developing variation***. Berkeley: University of California Press, 1984. (California Studies in 19th-Century Music, v. 2).

GIL, A. C. **Como elaborar projetos de pesquisa**. 4. ed. São Paulo: Atlas, 2002.

GOTHAM, M. et al. **Open music theory**: version 2. \[S.l.: s.n.\], 2021. Disponível em: https://viva.pressbooks.pub/openmusictheory/. Acesso em: 27 out. 2026.

GOTHAM, M. et al. The ‘Measure Map’: an inter-operable standard for aligning symbolic music. In: INTERNATIONAL CONFERENCE ON DIGITAL LIBRARIES FOR MUSICOLOGY (DLfM), 10., 2023, Milão. **Anais \[...\]**. New York: ACM, 2023. p. 91-99.

GUSFIELD, D. **Algorithms on strings, trees, and sequences**: computer science and computational biology. Cambridge: Cambridge University Press, 1997.

HINDEMITH, P. **Curso condensado de harmonia tradicional**: com predomínio de exercícios e um mínimo de regras. Tradução de Souza Lima. 13. ed. São Paulo: Irmãos Vitale, 1998.

HURON, D. On the role of embellishment tones in the perceptual segregation of concurrent musical parts. **Empirical Musicology Review**, 2007. <span class="mark">\[CONFERIR volume, número e páginas\]</span>

JANSSEN, B.; VAN KRANENBURG, P.; VOLK, A. Finding occurrences of melodic segments in folk songs employing symbolic similarity measures. **Journal of New Music Research**, v. 46, n. 2, p. 118-134, 2017.

KILIAN, J.; HOOS, H. H. MusicBLAST: gapped sequence alignment for MIR. In: INTERNATIONAL CONFERENCE ON MUSIC INFORMATION RETRIEVAL (ISMIR), 5., 2004, Barcelona. **Anais \[...\]**. Barcelona: Universitat Pompeu Fabra, 2004. p. 38-39.

MEREDITH, D.; LEMSTRÖM, K.; WIGGINS, G. A. Algorithms for discovering repeated patterns in multidimensional representations of polyphonic music. **Journal of New Music Research**, v. 31, n. 4, p. 321-345, 2002.

MEYER, L. B. **Emotion and meaning in music**. Chicago: University of Chicago Press, 1956.

MONGEAU, M.; SANKOFF, D. Comparison of musical sequences. **Computers and the Humanities**, v. 24, p. 161-175, 1990.

NARMOUR, E. **The analysis and cognition of basic melodic structures**: the implication-realization model. Chicago: University of Chicago Press, 1990.

NEEDLEMAN, S. B.; WUNSCH, C. D. A general method applicable to the search for similarities in the amino acid sequence of two proteins. **Journal of Molecular Biology**, v. 48, n. 3, p. 443-453, 1970.

PEYERL, K.; BARROS, G. S. de. Sonata nº 1 para piano de Edino Krieger: análise formal e motívica do primeiro movimento. **Revista Vórtex**, Curitiba, v. 5, n. 2, p. 1-23, 2017.

PHIPSON, B.; SMYTH, G. K. Permutation p-values should never be zero: calculating exact p-values when permutations are randomly drawn. **Statistical Applications in Genetics and Molecular Biology**, v. 9, n. 1, art. 39, 2010.

PRODANOV, C. C.; FREITAS, E. C. de. **Metodologia do trabalho científico**: métodos e técnicas da pesquisa e do trabalho acadêmico. 2. ed. Novo Hamburgo: Feevale, 2013.

RÉTI, R. **The thematic process in music**. New York: Macmillan, 1951.

RÉTI, R. **The thematic process in music**. Westport: Greenwood Press, 1978.

SMITH, T. F.; WATERMAN, M. S. Identification of common molecular subsequences. **Journal of Molecular Biology**, v. 147, n. 1, p. 195-197, 1981.

WOOTTON, J. C.; FEDERHEN, S. Statistics of local complexity in amino acid sequences and sequence databases. **Computers & Chemistry**, v. 17, n. 2, p. 149-163, 1993.

ZHU, T. et al. A novel local alignment-based approach to motif extraction in polyphonic music. In: INTERNATIONAL SYMPOSIUM ON COMPUTER MUSIC MULTIDISCIPLINARY RESEARCH (CMMR), 16., 2023, Tóquio. **Music and Sound Generation in the AI Era**. Cham: Springer, 2026. p. 378-389. (Lecture Notes in Computer Science, v. 15236).

[^1]: Na bioinformática, duas sequências são consideradas homólogas quando descendem de uma origem evolutiva comum, o que costuma se refletir em semelhança estrutural ou funcional entre elas.

[^2]: Técnica de resolução de problemas que consiste em dividi-los em subproblemas menores e sobrepostos, resolvendo e armazenando a solução de cada subproblema uma única vez para reaproveitá-la sempre que necessário, em vez de recalculá-la repetidamente.

[^3]: Esta contagem e a das melodias harmonizadas mais de uma vez (Seção 5.6.2) foram obtidas por um script em Python sobre o music21, disponível no repositório do projeto (github.com/pedro-schabarum/motif-align, scripts/levantamento_corpus.py).
