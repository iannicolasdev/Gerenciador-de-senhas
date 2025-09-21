import sqlite3
from cli import *
from password_utils import *
from db import *

def main():
    # Inicio do SQLite / Conexão com o banco de dados
    conn = sqlite3.connect("data/passwords.db")

    # Cria a tabela 
    create_table(conn)

    # Recebe os dados de usuário e serviço da senha
    username, service = get_inputs()

    # Recebe o dado da senha
    password = choose_password_method()

    # Adiciona os dados na tabela
    add_password(conn, service, username, password) # --ADICIONA--

    # Armazena os dados após o SELECT na tabela
    resultado = view_passwords(conn)

    # Exibe os dados da tabela no terminal
    list_table(resultado) # --VISUALIZA--

    # Teste com update
    update_password(conn) # --ATUALIZA SENHA--

    update_service(conn) # --ATUALIZA SERVIÇO--

    update_user(conn) # --ATUALIZA USER--

    conn.close()

if __name__ == "__main__":
    main()