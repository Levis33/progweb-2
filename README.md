Trabalho INF1407 - Donation

Grupo:

Thiago Levis Alambert Rodrigues
Pedro Feres Manhães

<hr>

Tema do trabalho:

O nosso projeto consiste em um site de doações com dois tipos de usuários, os administradores e os doadores. Os administradores criam as campanhas e gerenciam os usuários enquanto os doadores podem doar para as campanhas ativas.

<hr>

Funcionalidades:

O site foi implementado em python, com a utilização do framework Django para o backend, e para o frontend utlizamos o framework bootstrap, fontawsome para icones, datatables para as tabelas, Jquery, Ajax e javascript. Para o servidor utilizamos o pythonanywhere. Para a validação de CPF utilizamos uma biblioteca do python chamada validate-docbr 1.10.0, e para a consulta de CEPs através do ajax utilizamos o site ViaCep.

<hr>

Usuários

Como foi citado acima temos 2 tipos de usuários, os administradores e os doadores

Doadores:

Esses conseguem acessar o site e visualizar as informações básicas, como Home, FAQ e as campanhas ativas. Sua principal função é acessar uma campanha e doar, além disso ele pode acompanhar as campanhas ativas e enviar mensagens para os administradores através da FAQ

Administradores:

O administrador apresenta todas as funções do Doador e além delas ele tem as funções de criar, editar, deletar e visualizar e finalizar todas as campanhas. Além disso ele também pode criar novos usuários administradores, assim como gerenciar os usuários para desativalos ou ativalos. Outra funcionaliade do administrador é poder visualizar as mensagens enviadas por usuários na FAQ.

<hr>

CRUD

As 4 operações foram implementadas através da criação de uma campanha, como administrador podemos clicar em "Criar Campanhas" na nav bar para a sua criação.
Para visualizar todas as campanhas é preciso clicar em "Gerenciar Campanhas" na navbar
Para deletar existe o botão excluir na tabela mencionada na parte de visualizar.
Por fim, para a edição basta clicar no nome da campanha na tabela, que levara a uma página de edição da campanha selecionada.

Doação

Para fazer uma doação o usuário deve estar logado, a partir disso ele deve clicar no botão "Doar" da navbar e depois clicar em "Doar Agora!" de uma campanha, depois é so preencher o formulário que a doação sera registrada.

Envio de mensagens para administradores

O envio de mensagens ocorre através do botão "Perguntas Frequentes" da navbar, no final da página tera um formulário para enviar sua mensagem. O administrador poderá acessa-la clicando no 🙍 da navbar e clicando em "Mensanges FAQ", que irá mostrar uma tabela contendo todas as mensagens. 

Criação de usuários

A criação de doador é realizada quando um usuário clica no botão "Doar" sem ter feito login, assim ele é redirecionado para uma página de login e também aparece uma opção de criar uma nova conta.
A criação de administradores so pode ser feita através de outro administrador, que ao clicar no botão 🙍 e depois "Criar Administrador" é levado a um formulário para criar o novo usuário.
