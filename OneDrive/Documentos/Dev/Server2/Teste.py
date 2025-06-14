import sqlite3

# Cria (ou abre) o banco de dados local
conn = sqlite3.connect("teste.db")
cursor = conn.cursor()

# Cria uma tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER
)
""")

# Insere uma pessoa
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", ("Cayo", 23))

# Lê e exibe todos os registros
cursor.execute("SELECT * FROM pessoas")
for linha in cursor.fetchall():
    print(linha)

conn.commit()
conn.close()
