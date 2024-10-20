import os
from models.account import Account
from models.client import Individual


RED = "\033[31m"
YELLOW = Y = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"
BLUE_BACKGROUND = BB= "\033[44m"
RESET_COLOR = RC = "\033[0m"

MSG_INVALID = f"{RED}Operação inválida, por favor selecione uma das opções disponíveis no menu.{RESET_COLOR}"

def color_menu_character (letra: str)-> str:
    return f"{RED}{BB}[{letra}]{RC}"

def clear() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Menu:
    @staticmethod
    def start_menu() -> None:
        clear()
        while True:
            OI = f"{BLUE}Olá, seja bem vindo ao Banco Python!{RESET_COLOR}"
            MENU = f"""
{YELLOW}---- MENU ------------------------------------------{RESET_COLOR}
{color_menu_character('f')}\t Entrar como funcionário \t\t   |
{color_menu_character("c")}\t Entrar como cliente     \t\t   |
{color_menu_character('q')}\t Sair                  \t\t\t   | 
{OI}\t\t   | 
{YELLOW}----------------------------------------------------{RESET_COLOR}
=>"""            

            operation = input(MENU).lower()
            match operation:
                case "q":
                    clear()
                    break
                case "f":
                    clear()
                    Menu.employee_menu()
                case "c":
                    clear()
                    Menu.account_menu()
                case _:
                    print(MSG_INVALID)
                    
    
    @staticmethod
    def employee_menu() -> None:
        clear()
        OI = f"{BLUE}Olá, seja bem vindo ao Banco Python!{RESET_COLOR}"
        client = None
        while True:
            MENU = f"""
{YELLOW}---- MENU ------------------------------------------{RESET_COLOR}
{color_menu_character('su')}\t Selecione usuário  \t\t\t   |
{color_menu_character('nu')}\t Criar novo usuário \t\t\t   |
{color_menu_character("nc")}\t Criar nova conta   \t\t\t   |               
{color_menu_character("bc")}\t Buscar conta       \t\t\t   |        
{color_menu_character("lu")}\t Listar usuários    \t\t\t   |        
{color_menu_character("lc")}\t Listar contas      \t\t\t   |        
{color_menu_character('q')}\t Sair                \t\t\t   |       
{OI}\t\t   |
{YELLOW}----------------------------------------------------{RESET_COLOR}
=>"""
            operation = input(MENU).lower()
            match operation:
                case "q":
                    clear()
                    return
                case "su":
                    clear()
                    cpf = input(f"{YELLOW}Informe o cpf do usuário: {RESET_COLOR}")
                    client = Individual.get_client(cpf)
                
                    if client != None:
                        clear()
                        print(f"Usuario de cpf {cpf} foi selecionado:")
                        print(client)
                        continue
                    print(f"{RED}Usuário não encontrado em nossa base de dados!{RESET_COLOR}")
                    
            
                case "nu":
                    clear()
                    client = Individual(
                        cpf = input(f"{YELLOW}Informe o cpf do usuário: {RESET_COLOR}"),
                        name = input(f"{YELLOW}Informe o nome do usuário: {RESET_COLOR}"),
                        date_of_birth = input(f"{YELLOW}Informe a data de nascimento (dd-mm-aaaa): {RESET_COLOR}"),
                        address = input(f"{YELLOW}Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): {RESET_COLOR}"),
                        create_account= True if input(f"{YELLOW}Deseja criar uma conta?(Digite 's' para sim).lower() {RESET_COLOR}") == "s" else False
                    )
                    print(f"{GREEN}Usuário de cpf {client.cpf} foi criado e esta selecionado:{RESET_COLOR}")
                    print(client.get_str_client())
                case "nc":
                    clear()
                    if client == None:
                        print(f"{RED}Selecione ou cria um usuário primeiro!{RESET_COLOR}")
                        continue
                    
                    print(client.create_account())

                case "bc":
                    clear()
                    try:
                        number = int(input(f"{YELLOW}Informe o número da conta: {RESET_COLOR}"))
                        account = Account.get_account(number)
                        if account != None:
                            print(account)
                            continue
                    except ValueError as exp:
                        clear()
                        print(f"\n{exp}")
                        
                case "lu":
                    clear()
                    print(Individual.get_str_clients())
                    
                case "lc":
                    clear()
                    print(Account.get_str_accounts())
                case _:
                    clear()
                    print(MSG_INVALID)
    
    @staticmethod
    def account_menu() -> None:
        OI = f"{BLUE}Olá, seja bem vindo ao Banco Python!{RESET_COLOR}"
        clear()
        account = None
        while True:
            MENU = f"""
{YELLOW}---- MENU ------------------------------------------{RESET_COLOR}
{color_menu_character('a')}\t Acessar conta       \t\t\t   |
{color_menu_character('d')}\t Depositar           \t\t\t   |
{color_menu_character('s')}\t Sacar               \t\t\t   |
{color_menu_character('e')}\t Extrato             \t\t\t   |
{color_menu_character('q')}\t Sair                \t\t\t   |   
{OI}\t\t   |
{YELLOW}----------------------------------------------------{RESET_COLOR}
=>"""
            operation = input(MENU).lower()
            match operation:
                case "q":
                    clear()
                    return
                case "a":
                    clear()
                    try:
                        account = Account.get_account(
                            number = int(input(f"{YELLOW}Informe o número da conta: {RESET_COLOR}"))
                        )
                        print(account.get_str_account())
                    except ValueError as error:
                        clear()
                        print(error)
                        continue
                case "d":
                    clear()
                    if not account:
                        print("Acesse uma conta valida!")
                        continue
                    msg = account.deposit(float(input(f"{YELLOW}Qual valor deseja depositar? {RESET_COLOR}")))
                    print(msg)
                    
                case "s":
                    clear()
                    if not account:
                        print("Acesse uma conta valida!")
                        continue
                    msg = account.withdraw(float(input(f"{YELLOW}Qual valor deseja sacar? {RESET_COLOR}")))
                    print(msg)
                    
                case "e":
                    clear()
                    if not account:
                        print("Acesse uma conta valida!")
                        continue
                    print(account.get_statement())
                case _:
                    clear()
                    print(MSG_INVALID)
    