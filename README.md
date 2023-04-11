# TP1_ES: Escopo
O objetivo é desenvolver um sistema de reconhecimento de voz e síntese de fala que utiliza as tecnologias de Google Text to Speech, OpenAI e IBM Watson. O sistema permite que o usuário envie uma gravação de áudio de sua voz para o Text To Speech, que utiliza sua tecnologia de processamento de linguagem natural para transcrever o áudio em um texto. Em seguida, o texto é enviado para o OpenAI que analisa e responde, em seguida o texto é enviado para o IBM Watson, que utiliza sua tecnologia de síntese de fala para transformá-lo novamente em áudio. As principais features deste software incluem: 
- Reconhecimento de voz: O software é capaz de reconhecer e transcrever o áudio da voz do usuário em um texto. 

- Processamento de linguagem natural: A tecnologia de Text To Speech permite que o software processe e entenda a linguagem natural usada pelo usuário. 

- Síntese de fala: O IBM Watson é capaz de transformar o texto gerado pelo OpenAI em um áudio de qualidade. 

- Integração de tecnologias: O software combina a tecnologia de reconhecimento de voz, OpenAI e a tecnologia de síntese de fala de IBM Watson, oferecendo um resultado final de qualidade. 

- Facilidade de uso: O software é simples e fácil de usar, permitindo que qualquer pessoa possa utilizá-lo.

- Escalabilidade: O software pode ser facilmente escalado para lidar com grandes quantidades de áudio, tornando-o adequado para uso em empresas ou organizações que precisam transcrever grandes quantidades de dados de áudio em texto.

# Membros 
Nome | Função
-----|-------
Cristovao|Backend
Elias|Frontend
Giovanni|Frontend
Luiz|Full Stack
Yurih|BD

# Tecnologias (linguagem, frameworks e BD)
- python3
- pyweb/flask ou JS
- MySQL
- React

# Backlog do Produto
1 - Como usuário, eu gostaria de conseguir me cadastrar no sistema.

2 - Como usuário, eu gostaria de conseguir fazer login no sistema.

3 - Como usuário, eu gostaria de falar minha pergunta.

4 - Como usuário, eu gostaria de ouvir a resposta da minha pergunta.

5 - Como usuário, eu gostaria que as minhas perguntas e respostas ficassem salvas.

6 - Como usuário, eu gostaria de poder deletar minhas perguntas e respostas.

7 - Como usuário, eu gostaria de deletar minha conta no site.

8 - Como usuário, eu gostaria de ver minha resposta através de um robô interativo no sistema.

# Backlog do Sprint
História | Atividade | Responsável
---------|------------|-------------
1,2 | Instalar banco de dados e criar primeiras tabelas | Yurih
0 | Instalar python, flask | Cristovao
3 | Fazer integração do textToSpeech | Luiz
4 | Fazer integração entre chatgpt e watson | Luiz
3,4 | Implementação da API das integrações | Luiz
3 | Implementar no backend lógica de criação de perguntas | Cristovao
3,4 | Implementação da interface de áudio | Cristovao
0 | Implementar versão inicial da tela principal | Elias
0 | Integração front e back | Elias
0 | Instalar  nodejs  | Elias / Giovanni
1,2 | Implementar tela de login e formulário de criar usuário de forma responsiva | Giovanni
5 | Implementar tela principal do projeto, com possibilidade de incorporar perguntas | Giovanni
1,2,6,7 | Implementar api de controle de contas | Elias
1,2,5 | Integração do projeto ao database | Yurih
