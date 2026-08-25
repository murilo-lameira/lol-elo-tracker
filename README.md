# 🏆 LoL Elo Tracker (CLI)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Uma aplicação de interface de linha de comando (CLI) desenvolvida em Python para gerenciar um banco de dados local de ranqueadas de League of Legends. O sistema permite o cadastro, consulta e ranqueamento de Invocadores através de uma interface interativa diretamente no terminal.

## 🎯 Funcionalidades

* **CRUD Completo:** Cadastro, leitura, atualização e exclusão de Invocadores, Elos e PDLs.
* **Leaderboard Dinâmico:** Geração de uma tabela ranqueada, ordenando automaticamente os jogadores por pontuação utilizando queries SQL.
* **UI/UX no Terminal:** Interface de texto colorida e formatada em tabelas, garantindo uma navegação limpa e intuitiva para o usuário.
* **Arquitetura Limpa:** Separação estrutural entre a lógica de banco de dados (`database.py`) e a interface do usuário (`main.py`).

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Banco de Dados:** `sqlite3`
* **Formatação Visual:** Bibliotecas `tabulate` (estruturação de tabelas) e `colorama` (colorização de strings).

## 🚀 Como Executar

1. Clone este repositório em sua máquina:
```bash
git clone [https://github.com/murilo-lameira/lol-elo-tracker.git](https://github.com/murilo-lameira/lol-elo-tracker.git)