# EP1 Craps-Insper

![Capa](Capa.jpg)

**DESCRIÇÃO**

  Craps é um jogo de dados no qual os jogadores apostam no resultado da jogada, ou uma série de jogadas, de um par de dados. E esta versão é um trabalho escrito por dois alunos de graduação em engenharia do Insper.

**LINGUAGEM UTILIZADA**
- Python

**REGRAS**
  
  O jogador inicia o jogo com 1000 fichas, estas são apostas de diversas maneiras e a finalidade do jogo é acertar a soma de dois dados comuns (1 a 6) que são sorteados aleatoriamente pelo programa.
  O jogo é feito basicamente por meio de rodadas consecutivas, onde em cada uma delas o jogador escolhe apostar suas fichas ou não (processo que se encerra quando as fichas acabarem). A primeira rodada pode ter duas fases, uma delas chamada de "Come Out" e conforme o resultado, é aberta outra fase, chamada de "Point". O jogador pode fazer vários tipos de apostas conforme a fase. 

**TIPOS DE APOSTA**
- **Pass Line Bet -** Esta aposta só pode ser feita na fase de “Come Out”. Se a soma dos dados lançados for 7 ou 11 o jogador ganha (por exemplo: se apostou 10 fichas, mantem as 10 e recebe mais 10). Já se os dados somarem 2, 3 ou 12 (chamado de craps) o jogador perde   (ou seja, se apostou 10 fichas, não recebe nada e perde essas 10). Já se a soma dos dados der 4, 5, 6, 8, 9 ou 10 o jogo muda para a fase de “Point” e o objetivo muda. A aposta já feita continua valendo, porém, o valor tirado se torna o Point e para o jogador ganhar agora, a soma do novo lançamento dos dados deve ser igual ao do Point. Se a nova soma dos dados é a mesma do que foi guardado no Point,o jogador ganha o mesmo valor que apostou. Se sair uma soma de valor 7 o jogador perde tudo. Caso saia qualquer outro número, se mantem na fase de “Point” sem perder ou ganhar e se continua lançando os dados até um veredito, quando sair ou o número do Point ou o 7, terminando essa rodada e deixando começar uma nova em “Come Out”.
- **Field -** Esta aposta pode ser feita em qualquer fase do jogo. Nesta aposta se os dados derem 5, 6, 7 ou 8 o jogador perde tudo, já se derem 3, 4, 9, 10, ou 11 o jogador ganha o mesmo valor que apostou, já se a soma for 2 o jogador ganha o dobro do que apostou (se apostou 10 fichas, fica com as 10 e ganha mais 20), e finalmente se sai 12 nos dados o jogador ganha o triplo (se apostou 10 fichas, fica com as 10 e ganha mais 30).
- **Any Craps -** Esta aposta pode ser feita em qualquer fase do jogo. Nesta aposta se o dados derem 2, 3 ou 12 o jogador ganha sete vezes o que apostou, senão perde a aposta.
- **Twelve -** Esta aposta pode ser feita em qualquer fase do jogo. Nesta aposta se o dados derem 12 o jogador ganha trinta vezes o que apostou, senão perde a aposta.

**JOGABILIDADE**
1. No primeiro passo, o programa perguntará se o jogador deseja realizar uma aposta. A resposta será 's' para aceitar e prosseguir, ou 'n' para não realizar, desse modo será feita outra pergunta para a confirmação da resposta anterior. Assim, o programa entenderá que ocorreu uma desistência no jogo e mostrará com quantas fichas o jogador estava no momento. A pergunta inicial se repetirá sempre que uma nova rodada de apostas for aberta.
2. No segundo passo, após confirmado o desejo de realizar a aposta, são apresentados os tipos de aposta (com uma legenda simples e intuitiva). Após essa escolha, é aberto o comando para o jogador escolher o valor da aposta. Posterior a esse processo, é mostrado um pequeno relatório contendo as apostas realizadas na rodada em questão, a quantidade de fichas que não foram apostadas (fichas em mão) e a quantidade de fichas que estão sendo apostadas (fichas em aposta). 
3. Em um terceiro passo, é mostrado uma figura com os dados sorteados e logo abaixo sua respectiva soma. Além disso, é informado ao apostador se a fase de Point foi iniciada (com o valor de fichas apostados no Pass Line Bet), o número de fichas disponíveis para iniciar a próxima rodada de apostas também é comunicado. Se houver algum ganho ou perda de fichas durante a rodada isso será informado ao jogador e, posteriormente, suas fichas disponíveis serão mostradas.
4. Por fim, se o jogador não pressionar 'x' e sair do jogo em qualquer uma das rodadas jogadas, o programa expulsa o apostador quando é contabilizado que não existem mais fichas disponíveis para a aposta, caraterizando um verdadeiro jogo de AZAR!
