
CÓDIGO FEITO E EDITADO NO VISUAL STUDIO CODE. 
UTILIZADO SQLITE3 PARA CRIAR O BANCO DE DADOS E PARA FAZER A MANIPULAÇÃO DO MESMO.
ARQUIVO SQL PARA MOSTRAR O QUE TEM NO BANCO DE DADOS...
ARQUIVO database.db CRIADO COMO BANCO DE DADOS.

## Instalação e Requisitos

Este script requer Python 3.x e a biblioteca `sqlite3`.

necessário: pip install sqlite3

## Documentação do Código Python para Manipulação de Banco de Dados SQLite
Módulos Utilizados
sqlite3: Fornecerá a funcionalidade para interagir com o banco de dados SQLite.
time: Utilizado para adicionar pausas no programa para melhorar a experiência do usuário.

## Funções Principais
1. ConexaoBD(database)
Descrição: Estabelece uma conexão com o banco de dados SQLite especificado.
Parâmetros:
database: string contendo o nome do arquivo do banco de dados SQLite.
Retorno:
conector: objeto de conexão SQLite.
2. Inserir_tabela(conector)
Descrição: Cria uma nova tabela no banco de dados.
Parâmetros:
conector: objeto de conexão SQLite.
Retorno:
nomeDaTabela: string contendo o nome da tabela criada.
3. Adicionar_coluna(conector, nomeDaTabela)
Descrição: Adiciona uma nova coluna à tabela especificada no banco de dados.
Parâmetros:
conector: objeto de conexão SQLite.
nomeDaTabela: string contendo o nome da tabela à qual a coluna será adicionada.
4. Inserir_dados(conector)
Descrição: Insere novos dados em uma tabela existente no banco de dados.
Parâmetros:
conector: objeto de conexão SQLite.
5. Atualizar_dados(conector, tabela)
Descrição: Atualiza os dados em uma tabela existente no banco de dados.
Parâmetros:
conector: objeto de conexão SQLite.
tabela: string contendo o nome da tabela a ser atualizada.
6. Mostrar_dados(conector, tabela)
Descrição: Mostra os dados de uma tabela existente no banco de dados.
Parâmetros:
conector: objeto de conexão SQLite.
tabela: string contendo o nome da tabela a ser exibida.
7. Mostrar_tabelas(conector)
Descrição: Mostra todas as tabelas existentes no banco de dados, juntamente com suas colunas.
Parâmetros:
conector: objeto de conexão SQLite.
8. deletar_registro(conector, tabela, condicao)
Descrição: Deleta registros de uma tabela existente no banco de dados com base em uma condição especificada.
Parâmetros:
conector: objeto de conexão SQLite.
tabela: string contendo o nome da tabela da qual os registros serão excluídos.
condicao: string contendo a condição para excluir os registros (por exemplo, "id=1").
9. excluir_tabela(conector)
Descrição: Exclui uma tabela existente no banco de dados.
Parâmetros:
conector: objeto de conexão SQLite.
Função Principal
10. main()
Descrição: Função principal que controla o fluxo do programa.
Funcionalidade: Oferece um menu de opções para o usuário interagir com o banco de dados, incluindo inserir tabela, inserir dados, inserir coluna, atualizar dados, mostrar dados, deletar dados, deletar tabela e sair do programa.
Execução do Programa
A função main() é executada quando o script Python é chamado diretamente.
