# CargaEmocionalDireito

Esse repositório guarda os resultados do Field Project "Quantificando a carga emocional do direito", desenvolvido no primeiro semestre de 2020 no curso de graduação da FGV Direito Rio.

Ao longo do semestre, os alunos Carolina Soares, Clara Svartz, Gabriel Rogenfisch, Henrique Torres, Giulia Reis, João Antonio Rocha, Luiza Romeiro e Marcelle Dumas, sob a supervisão do professor Guilherme da Franca Couto Fernandes de Almeida, desenvolveram uma função em Python que usa os léxicos [Oplexicon](https://www.inf.pucrs.br/linatural/wordpress/recursos-e-ferramentas/oplexicon/) e [SentiLex-pt](https://www.inesc-id.pt/ficheiros/publicacoes/11406.pdf) para tentar quantificar a carga emocional do direito.

A aplicação da função a uma amostra aleatória de decisões do STF mostra que a distribuição da valência se aproxima de uma distribuição normal. Infelizmente, os esforços de validação da ferramenta foram inconclusivos. Quando tentamos construir datasets anotados sistemáticos de decisões do STF, notamos muita discordância entre os anotadores, o que torna difícil usar o conjunto de dados resultante para avaliar a performance da função criada. Esforços futuros devem se iniciar por testes mais rigorosos da ferramenta.

Na construção desse método, usamos ideias descritas em [Avanço e Nunes, 2014](http://www.producao.usp.br/bitstream/BDPI/48648/1/2652288.pdf) e [Avanço, 2015](https://www.teses.usp.br/teses/disponiveis/55/55134/tde-24032016-171420/pt-br.php).
