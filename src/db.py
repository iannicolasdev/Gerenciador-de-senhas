import sqlite3
from cli import get_update_inputs, get_delete_inputs

def create_table(conn):
    cursor = conn.cursor() 

    # Comando CREATE para criar a tabela no banco para receber os dados 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS passwords ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service TEXT NOT NULL,
        username TEXT,
        password TEXT NOT NULL
    )
    """) # Ela cria a tabela apenas uma vez
    conn.commit()

def add_password(conn, service, username, password):
    cursor = conn.cursor()

    # Comando INSERT para inserir os dados do usuário na tabela
    cursor.execute("""
    INSERT INTO passwords (service, username, password) 
    VALUES (?, ?, ?);
    """, (service, username, password))
    conn.commit()

def view_passwords(conn):
    cursor = conn.cursor()
    # Comando SELECT para visualizar os dados na tabela
    cursor.execute("""
    SELECT * FROM passwords 
    """)

    resultado = cursor.fetchall()

    return resultado

# Função de atualização do serviço 
def update_service(conn):
    cursor = conn.cursor()

    id_, new_service = get_update_inputs("do serviço", "o novo serviço")

    cursor.execute("""
    UPDATE passwords
    SET service = ?
    WHERE id = ?    
    """, (new_service, id_))

    conn.commit()

# Função de atualização do user
def update_user(conn):
    cursor = conn.cursor()

    id_, new_user = get_update_inputs("do user", "o novo user")

    cursor.execute("""
    UPDATE passwords
    SET username = ?
    WHERE id = ?
    """, (new_user, id_))

    conn.commit()

# Função de atualização da senha
def update_password(conn):
    cursor = conn.cursor()

    id_, new_password = get_update_inputs("da senha", "a nova senha")

    cursor.execute("""
    UPDATE passwords
    SET password = ?
    WHERE id = ?
    """, (new_password, id_))
    
    conn.commit()

def delete_password(conn):
    cursor = conn.cursor()

    delete_id = get_delete_inputs()

    cursor.execute("""
    DELETE FROM passwords
    WHERE id = ?
    """, (delete_id,))

    conn.commit()