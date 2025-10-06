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

    print("""
    ---------Comandos---------
    1 - Adicionar 
    2 - Visualizar
    3 - Atualizar
    4 - Excluir
    """)

    command = int(input("Insira sua escolha: "))
    print("\n")

    if command == 1:
        username, service = get_inputs()

        password = choose_password_method()

        add_password(conn, service, username, password)

    elif command == 2:
        resultado = view_passwords(conn) 

        list_table(resultado)

    elif command == 3:
        choose_password_update(conn)

    elif command == 4:
        delete_password(conn)

    else:
        print("Erro: Comando inválido")

    conn.close()

if __name__ == "__main__":
    main()