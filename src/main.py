import random 
import string as st
import sqlite3

# Caracteres incluidos na geração de senhas
caracteres = st.ascii_letters + st.digits + st.punctuation

# Entrada de dados do usuário
length = int(input("Qual o tamanho da senhas?: "))

username = str(input("Qual o seu nome?: "))

service = str(input("Qual o serviço da senha?: "))

# Geração de senha aleatória
password = (''.join(random.choices(caracteres, k=length)))

# Inicio do SQLite / Conexão com o banco de dados
conn = sqlite3.connect("data/passwords.db")
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

# Comando INSERT para inserir os dados do usuário na tabela
cursor.execute("""
INSERT INTO passwords (service, username, password) 
VALUES (?, ?, ?);
""", (service, username, password))

conn.commit()