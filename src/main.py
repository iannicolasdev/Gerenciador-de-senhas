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

# if os.path.exists("data/password.json"):
#     try:
#         with open("data/password.json", "r") as file:
#             data = json.load(file)
#     except json.JSONDecodeError:
#         data = {"passwords": []}  
# else:
#     data = {"passwords": []}  

# data["passwords"].append(password)

# with open("data/password.json", "w") as file:
#     json.dump(data, file, indent=4)

