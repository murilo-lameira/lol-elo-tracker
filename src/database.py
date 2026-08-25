import sqlite3 as sq
import os

# Garante que o banco seja salvo na pasta 'data' na raiz do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'data', 'Ranking.db')

def _conectar():
    """Cria a pasta data se não existir e retorna a conexão."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sq.connect(DB_PATH)

def criar_tabela():
    with _conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS Usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Invocador TEXT NOT NULL,
                Pdl INTEGER NOT NULL,
                Elo TEXT NOT NULL
            )
        """)

def armazenar_usuario(invocador, pdl, elo):
    with _conectar() as conexao:
        # Uso de '?' evita falhas de segurança (SQL Injection)
        conexao.execute("INSERT INTO Usuario (Invocador, Pdl, Elo) VALUES (?, ?, ?)", (invocador, pdl, elo))

def consultar_usuario(invocador):
    with _conectar() as conexao:
        cur = conexao.cursor()
        cur.execute("SELECT Invocador, Elo, Pdl FROM Usuario WHERE Invocador = ?", (invocador,))
        return cur.fetchone()

def obter_leaderboard():
    with _conectar() as conexao:
        cur = conexao.cursor()
        cur.execute("SELECT Invocador, Pdl, Elo FROM Usuario ORDER BY Pdl DESC")
        return cur.fetchall()

def atualizar_usuario(invocador, pdl, elo):
    with _conectar() as conexao:
        cur = conexao.cursor()
        cur.execute("UPDATE Usuario SET Pdl = ?, Elo = ? WHERE Invocador = ?", (pdl, elo, invocador))
        return cur.rowcount > 0 # Retorna True se o usuário existia e foi alterado

def apagar_dados():
    with _conectar() as conexao:
        conexao.execute("DELETE FROM Usuario")