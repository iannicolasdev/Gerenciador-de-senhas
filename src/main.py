import sqlite3
from cli import *
from password_utils import *
from db import *
from menu import *

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
    add_password(conn, service, username, password) 

    # Armazena os dados após o SELECT na tabela
    resultado = view_passwords(conn)

    # Exibe os dados da tabela no terminal
    list_table(resultado) 

    # Executa de forma dinâmica quais alterações o user deseja
    choose_password_update(conn)

    conn.close()

if __name__ == "__main__":
    main()