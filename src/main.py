import random 
import string as st
import sqlite3

caracteres = st.ascii_letters + st.digits + st.punctuation

length = int(input("Qual o tamanho da senhas?: "))

username = str(input("Qual o seu nome?: "))

service = str(input("Qual o serviço da senha?: "))

password = (''.join(random.choices(caracteres, k=length)))

conn = sqlite3.connect("data/passwords.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service TEXT NOT NULL,
    username TEXT,
    password TEXT NOT NULL
)
""")

cursor.execute("""
INSERT INTO passwords (service, username, password) 
VALUES (?, ?, ?);
""", (service, username, password))

conn.commit()