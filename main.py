import sys
import os
from relatorio import Relatorio  # Importação corrigida
from sistema_faltas import Sistema
from auditoria import Auditoria
from colorama import init, Fore

# Inicializa o colorama
init(autoreset=True)

# Função para limpar o terminal
def limpar_tela():
    os.system("cls" if sys.platform == "win32" else "clear")

# Função de boas-vindas
def boas_vindas():
    limpar_tela()
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "Bem-vindo ao Sistema de Registro de Faltas!")
    print(Fore.CYAN + "=" * 50)

def menu():
    sistema = Sistema()
    auditoria = Auditoria()
    relatorio = Relatorio(sistema)  # Criando uma instância da classe Relatorio

    while True:
        limpar_tela()
        print(Fore.GREEN + "=" * 50)
        print(Fore.GREEN + "1. Registrar Falta")
        print(Fore.YELLOW + "2. Listar Faltas")
        print(Fore.MAGENTA + "3. Gerar Relatório")
        print(Fore.RED + "4. Sair")
        print(Fore.GREEN + "=" * 50)

        opcao = input(Fore.WHITE + "Escolha uma opção: ")

        if opcao == '1':
            sistema.registrar_falta(auditoria)
        elif opcao == '2':
            sistema.listar_faltas()
        elif opcao == '3':
            relatorio.gerar_relatorio()  # Agora chama a função corretamente
        elif opcao == '4':
            print(Fore.RED + "Saindo do sistema...")
            sys.exit()
        else:
            print(Fore.RED + "Opção inválida!")
            input(Fore.WHITE + "Pressione Enter para tentar novamente.")

if __name__ == "__main__":
    boas_vindas()
    menu()
