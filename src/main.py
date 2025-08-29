import random 
import string as st
import sqlite3
import json
import os

# caracteres = st.ascii_letters + st.digits + st.punctuation

# length = int(input("Qual o tamanho da senhas? "))

# password = (''.join(random.choices(caracteres, k=length)))

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
VALUES ('GitHub', 'ian', '12345678');
""")

conn.commit()