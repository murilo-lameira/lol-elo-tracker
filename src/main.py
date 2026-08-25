import os
import time
from tabulate import tabulate
from colorama import Fore, Style, init
import database as db

# Inicializa o colorama para funcionar corretamente no Windows
init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        limpar_tela()
        print(60 * "-")
        print(Fore.LIGHTBLUE_EX + '''
    =======================================
    |   Bem vindo ao Banco de Dados do    |
    |   Ranking de League of Legends      |
    =======================================''')
        
        comando = input('''
            [1] Inserir Invocador
            [2] Consultar Invocador
            [3] Leaderboard
            [4] Atualizar Rank
                            
            [0] Sair
            [8] Informações
            [9] Apagar os dados
                            
            Qual opção deseja: ''')
        
        print(60 * "-")

        if comando == '1':
            invocador = input("Digite o nome do invocador: ").strip().upper()
            elo = input("Digite o Elo: ").strip().upper()
            pdl = int(input("Digite o PDL: "))
            db.armazenar_usuario(invocador, pdl, elo)
            print(Fore.GREEN + "\nInvocador cadastrado com sucesso!")
            time.sleep(1.5)

        elif comando == '2':
            invocador = input("Digite o nome do invocador: ").strip().upper()
            usuario = db.consultar_usuario(invocador)
            if usuario:
                print("\n" + Fore.LIGHTBLUE_EX + tabulate([usuario], headers=['INVOCADOR', 'ELO', 'PDL'], tablefmt='pretty'))
            else:
                print(Fore.RED + "\nUsuário não encontrado.")
            input("\nPressione ENTER para voltar ao menu...")

        elif comando == '3':
            usuarios = db.obter_leaderboard()
            if usuarios:
                print("\n" + Fore.YELLOW + tabulate(usuarios, headers=['Invocador', 'PDL', 'ELO'], tablefmt='pretty'))
            else:
                print(Fore.YELLOW + "\nNenhum jogador cadastrado ainda.")
            input("\nPressione ENTER para voltar ao menu...")

        elif comando == '4':
            invocador = input("Digite o nome do invocador: ").strip().upper()
            elo = input("Digite o novo Elo: ").strip().upper()
            pdl = int(input("Digite o novo PDL: "))
            
            sucesso = db.atualizar_usuario(invocador, pdl, elo)
            if sucesso:
                print(Fore.GREEN + "\nRank atualizado com sucesso!")
            else:
                print(Fore.RED + "\nUsuário não encontrado.")
            time.sleep(1.5)

        elif comando == '8':
            infos()

        elif comando == '9':
            certeza = input("Tem certeza que deseja apagar tudo? (S/N): ").strip().upper()
            if certeza == 'S':
                db.apagar_dados()
                print(Fore.RED + "\nDados apagados com sucesso!")
            else:
                print(Fore.YELLOW + "\nOperação cancelada.")
            time.sleep(1.5)

        elif comando == '0':
            print(Fore.CYAN + "\nConexão finalizada. Até logo!")
            break
        
        else:
            print(Fore.RED + "\nComando inválido!")
            time.sleep(1)

def infos():
    limpar_tela()
    print(Fore.LIGHTBLUE_EX + '''
    =======================================
    |            DEVELOPERS               |
    |   Dev Senior: Murilo Lameira        |
    |   Dev Jr:     Leonardo Retori       |
    |   Dev Jr:     Matheus Soares        |
    =======================================
    |   Linguagem: Python                 |
    |   Banco de Dados: SQLite            |
    |   Data: 23/11/2023                  |
    =======================================''')
    input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    db.criar_tabela()
    menu()