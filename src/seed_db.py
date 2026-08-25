import database as db

def popular_banco():
    # 1. Garante que a tabela existe antes de inserir
    db.criar_tabela()

    # 2. Lista de dados fictícios para injetar
    jogadores_mock = [
        ("FAKER", 1250, "CHALLENGER"),
        ("BRTT", 850, "GRANDMASTER"),
        ("KAMI", 900, "CHALLENGER"),
        ("YODA", 450, "MASTER"),
        ("AYEL", 600, "GRANDMASTER"),
        ("JUKS", 150, "DIAMOND I"),
        ("MINERVA", 320, "MASTER")
    ]

    print("🌱 Populando banco de dados com dados de teste...")
    
    # 3. Faz um loop chamando a sua função original de armazenar
    for invocador, pdl, elo in jogadores_mock:
        db.armazenar_usuario(invocador, pdl, elo)
        print(f" -> {invocador} ({elo} - {pdl} PDL) adicionado.")

    print("\n✅ Banco de dados populado com sucesso! Pode rodar o main.py agora.")

if __name__ == "__main__":
    popular_banco()