import string as st
import sqlite3

def get_inputs():
    # Entrada de dados do usuário
    length = int(input("Qual o tamanho da senhas?: "))
    username = str(input("Qual o seu nome?: "))
    service = str(input("Qual o serviço da senha?: "))
    return length, username, service

def generate_password(length):
    import random
    # Caracteres incluidos na geração de senhas
    caracteres = st.ascii_letters + st.digits + st.punctuation

    # Geração de senha aleatória
    password = (''.join(random.choices(caracteres, k=length)))
    return password

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


# Inicio do SQLite / Conexão com o banco de dados
conn = sqlite3.connect("data/passwords.db")

length, username, service = get_inputs()
password = generate_password(length)
add_password(conn, service, username, password)

conn.close()