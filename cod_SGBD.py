
import time
import sqlite3
from pathlib import Path

def ConexaoBD(database):
    """
    Estabelece uma conexão com o banco de dados SQLite especificado.

    Parâmetros:
    - database: string contendo o nome do arquivo do banco de dados SQLite.

    Retorna:
    - conector: objeto de conexão SQLite.
    """

    if not Path(database).is_file():
        # Se não existir, cria o arquivo no diretório de execução
        Path(database).touch()

    conector = sqlite3.connect(database)
    return conector

def Inserir_tabela(conector):
    """
    Cria uma nova tabela no banco de dados.

    Parâmetros:
    - conector: objeto de conexão SQLite.

    Retorna:
    - nomeDaTabela: string contendo o nome da tabela criada.
    """
    cursor = conector.cursor()

    nomeDaTabela = input("Qual o nome da tabela que você quer criar? >>> ")
    cursor.execute("CREATE TABLE IF NOT EXISTS {} (ID INTEGER PRIMARY KEY AUTOINCREMENT)".format(nomeDaTabela))

    print("Tabela '{}' criada com sucesso. \n Com ID integer primary key autoincrement.".format(nomeDaTabela))

    conector.commit()

    return nomeDaTabela

def tabela_existe(nomeDaTabela):
    """
    Verifica se uma tabela com o nome especificado existe no banco de dados.

    Parâmetros:
    - nomeDaTabela: string contendo o nome da tabela a ser verificada.

    Retorna:
    - True se a tabela existe, False caso contrário.
    """
    database = "database.db"
    conector = ConexaoBD(database)

    cursor = conector.cursor()
    cursor.execute("""
        SELECT count(name) FROM sqlite_master
        WHERE type='table' AND name=?
    """, (nomeDaTabela,))
    return cursor.fetchone()[0] == 1


def Adicionar_coluna(conector,nomeDaTabela):
    """
    Adiciona uma nova coluna à tabela especificada no banco de dados.

    Parâmetros:
    - conector: objeto de conexão SQLite.
    - nomeDaTabela: string contendo o nome da tabela à qual a coluna será adicionada.
    """
    cursor = conector.cursor()
    if nomeDaTabela == "":
        while True:
            nomeDaTabela = input("Qual o nome da tabela ?")
            if tabela_existe(nomeDaTabela):
                print(f"A tabela '{nomeDaTabela}' existe no banco de dados.")
                break
            else:
                print(f"A tabela '{nomeDaTabela}' não existe no banco de dados. Por favor, tente novamente.")
                
    adicionar_colunas = input("Deseja adicionar colunas à tabela? (S/N) >>> ").lower()
    while adicionar_colunas == "s":
        coluna_nome = input("Digite o nome da nova coluna >>> ")
        coluna_tipo = input("Digite o tipo da nova coluna >>> ")
        cursor.execute("ALTER TABLE {} ADD COLUMN {} {}".format(nomeDaTabela, coluna_nome, coluna_tipo))
        print("Coluna '{}' adicionada com sucesso à tabela '{}'.".format(coluna_nome, nomeDaTabela))
        
        adicionar_colunas = input("Deseja adicionar mais colunas à tabela? (S/N) >>> ").lower()

    conector.commit()

def Inserir_dados(conector):
    """
    Insere novos dados em uma tabela existente no banco de dados.

    Parâmetros:
    - conector: objeto de conexão SQLite.
    """
    cursor = conector.cursor()

    tabela = input("Qual tabela deseja inserir os dados? >>> ")

    cursor.execute("PRAGMA table_info({})".format(tabela))
    colunas = [coluna[1] for coluna in cursor.fetchall() if coluna[1] != 'ID']

    dados = []
    for coluna in colunas:
        dado = input("Qual o valor para a coluna '{}'? >>> ".format(coluna))
        dados.append(dado)

    consulta = "INSERT INTO {} ({}) VALUES ({})".format(tabela, ", ".join(colunas), ", ".join(["?" for _ in colunas]))
    
    cursor.execute(consulta, tuple(dados))
    conector.commit()

    print("Dados inseridos com sucesso na tabela '{}'.".format(tabela))

def Atualizar_dados(conector, tabela):
    """
    Atualiza os dados em uma tabela existente no banco de dados.

    Parâmetros:
    - conector: objeto de conexão SQLite.
    - tabela: string contendo o nome da tabela a ser atualizada.
    """
    cursor = conector.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tabela,))
    tabela_existente = cursor.fetchone()
    if not tabela_existente:
        print("A tabela '{}' não existe.".format(tabela))
        return

    cursor.execute("PRAGMA table_info({})".format(tabela))
    colunas = [coluna[1] for coluna in cursor.fetchall()]

    varUpd = input("Qual coluna da tabela '{}' receberá os dados atualizados? >>> ".format(tabela))
    if varUpd not in colunas:
        print("A coluna '{}' não existe na tabela '{}'.".format(varUpd, tabela))
        return

    varAntigo = input("Qual o valor antigo que você quer mudar na coluna '{}'? >>> ".format(varUpd))

    cursor.execute("SELECT {} FROM {} WHERE {} = ?".format(varUpd, tabela, varUpd), (varAntigo,))
    valor_antigo_existente = cursor.fetchone()
    if not valor_antigo_existente:
        print("O valor '{}' não existe na coluna '{}' da tabela '{}'.".format(varAntigo, varUpd, tabela))
        return

    varAtual = input("Qual o novo valor para a coluna '{}'? >>> ".format(varUpd))

    cursor.execute("UPDATE {} SET {} = ? WHERE {} = ?".format(tabela, varUpd, varUpd), (varAtual, varAntigo))
    conector.commit()

    print("Dados atualizados com sucesso na coluna '{}' da tabela '{}'.".format(varUpd, tabela))

def Mostrar_dados(conector, tabela):
    """
    Mostra os dados de uma tabela existente no banco de dados.

    Parâmetros:
    - conector: objeto de conexão SQLite.
    - tabela: string contendo o nome da tabela a ser exibida.
    """
    cursor = conector.cursor()
    cursor.execute(f"SELECT * FROM {tabela}")
    dados = cursor.fetchall()
    if not dados:
        print("\nNão HÁ DADOS....\n")
        print("Voltando para a tela inicial...\n")
    else:
        for linha in dados:
            print(linha)

def Mostrar_tabelas(conector):
    """
    Mostra todas as tabelas existentes no banco de dados, juntamente com suas colunas.

    Parâmetros:
    - conector: objeto de conexão SQLite.
    """
    cursor = conector.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tabelas = cursor.fetchall()
    for tabela in tabelas:
        print("Tabela:", tabela[0])
        cursor.execute("PRAGMA table_info({})".format(tabela[0]))
        colunas = cursor.fetchall()
        for coluna in colunas:
            print("    -", coluna[1])

def deletar_registro(conector, tabela, condicao):
    """
    Deleta registros de uma tabela existente no banco de dados com base em uma condição especificada.

    Parâmetros:
    - conector: objeto de conexão SQLite.
    - tabela: string contendo o nome da tabela da qual os registros serão excluídos.
    - condicao: string contendo a condição para excluir os registros (por exemplo, "id=1").
    """
    cursor = conector.cursor()
    cursor.execute("DELETE FROM {} WHERE {}".format(tabela, condicao))
    conector.commit()

def excluir_tabela(conector):
    """
    Exclui uma tabela existente no banco de dados.

    Parâmetros:
    - conector: objeto de conexão SQLite.
    """
    cursor = conector.cursor()

    tabela = input("Qual é o nome da tabela que você deseja excluir? >>> ")

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tabela,))
    tabela_existente = cursor.fetchone()
    if not tabela_existente:
        print("A tabela '{}' não existe.".format(tabela))
        return

    confirmacao = input("Tem certeza que deseja excluir a tabela '{}'? (S/N) >>> ".format(tabela)).lower()
    if confirmacao != "s":
        print("Operação cancelada.")
        return

    cursor.execute("DROP TABLE {}".format(tabela))
    conector.commit()
    print("Tabela '{}' excluída com sucesso.".format(tabela))

def main():
    """
    Função principal que controla o fluxo do programa.
    """
    database = "database.db"
    conector = ConexaoBD(database)
    escolha = 1

    while escolha != 0:

        print("LENDO BANCO DE DADOS...\n")
        time.sleep(2)
        print("--_|MOSTRANDO TABELAS E COLUNAS|_--")
        print("--------------------------------------------------\n")
        Mostrar_tabelas(conector)
        print("\n--------------------------------------------------\n")

        escolha = int(input("Qual ação deseja fazer? \n0 - PARA SAIR \n1 - Inserir Tabela \n2 - Inserir Dados \n3 - Inserir Coluna \n4 - Atualizar Dados \n5 - Mostrar Dados \n6 - DELETAR DADOS \n7 - DELETAR TABELA \n>>> "))

        if escolha == 1:
            nomeDaTabela = Inserir_tabela(conector)
            Adicionar_coluna(conector, nomeDaTabela)

        elif escolha == 2:
            Inserir_dados(conector)

        elif escolha == 3:
            Empty = ""
            Adicionar_coluna(conector, Empty)

        elif escolha == 4:
            tabela = input("Qual é o nome da tabela que você deseja atualizar? >>> ")
            Atualizar_dados(conector, tabela)

        elif escolha == 5:
            tabela = input("Selecione a tabela que você quer ver os dados? \nDigite a tabela>>> ").upper()
            Mostrar_dados(conector, tabela)

        elif escolha == 6:
            tabela = input("De qual tabela você deseja deletar um registro? >>> ")
            condicao = input("Qual a condição para deletar o registro? (Exemplo: id=1) >>> ")
            deletar_registro(conector, tabela, condicao)

        elif escolha == 7:
            excluir_tabela(conector)

        elif escolha == 0:
            quit()


if __name__ == '__main__':
    main()
