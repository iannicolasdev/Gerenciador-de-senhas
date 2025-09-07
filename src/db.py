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