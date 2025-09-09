import sqlite3
from cli import *
from password_utils import *
from db import *

def main():
    # Inicio do SQLite / Conexão com o banco de dados
    conn = sqlite3.connect("data/passwords.db")

    create_table(conn)

    username, service = get_inputs()

    password = choose_password_method()

    add_password(conn, service, username, password)

    conn.close()

if __name__ == "__main__":
    main()