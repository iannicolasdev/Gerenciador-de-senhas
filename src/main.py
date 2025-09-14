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

    resultado = view_passwords(conn)

    print(f"| {'ID':>3} | {'Service':<20} | {'User':<20} | {'Password':<20} |")
    print("-" * 76)

    for linha in resultado:
        id_, service, user, password = linha

        print(f"| {id_:>3} | {service:<20} | {user:<20} | {password:<20} |")

    conn.close()

if __name__ == "__main__":
    main()