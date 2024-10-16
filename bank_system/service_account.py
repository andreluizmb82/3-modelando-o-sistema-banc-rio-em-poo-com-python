from utils_print import  Pu, color_menu_character, clear, println
from service_validation import *
from type_define import Account, Users

def menu()->str:
    OI = f"{Pu.BLUE}Olá, seja bem vindo ao Banco Python!{Pu.RESET_COLOR}"
    MENU = f"""
{Pu.YELLOW}---- MENU ---------------------------{Pu.RESET_COLOR}
{color_menu_character('d')}\t Depositar                  |
{color_menu_character('s')}\t Sacar                      |
{color_menu_character('e')}\t Extrato                    |
{color_menu_character('nu')}\t Criar novo usuário         |
{color_menu_character("nc")}\t Criar nova conta           |
{color_menu_character("bu")}\t Buscar usuário             |
{color_menu_character("lu")}\t Listar usuários            |
{color_menu_character("lc")}\t Listar contas              |
{color_menu_character('q')}\t Sair                       |
{OI}|
{Pu.YELLOW}-------------------------------------{Pu.RESET_COLOR}
=>"""
    return MENU
    

def deposit(balance: float, value: float, statement: str, /) -> tuple[float, str, str]:
    if validate_deposit(value):
        new_balance = balance + value
        new_statement = statement + f"{Pu.GREEN}Depósito: \tR$ {value:.2f}\n{Pu.RESET_COLOR}"
        return (
            new_balance,  
            new_statement, 
            f"{Pu.GREEN}Depósito realizado com sucesso!{Pu.RESET_COLOR}"
            )
    
    return (
        balance, 
        statement, 
        f"{Pu.RED}Operação falhou! O valor informado é inválido.{Pu.RESET_COLOR}"
        )


def withdraw(*,
    balance: float,
    value: float,
    statement: str,
    withdrawal_amount_limit: float,
    withdrawal_number: int,
    withdrawal_number_limit: int,
    ) -> tuple[float, str, int, str]:
    valid, msg = validate_withdrawal(
        balance,
        value,
        withdrawal_amount_limit,
        withdrawal_number,
        withdrawal_number_limit
        )
    if valid:
        new_balance = balance - value
        new_statement = statement + f"{Pu.RED}Saque: \tR$ {value:.2f}\n{Pu.RESET_COLOR}"
        new_withdrawal_number = 1 + withdrawal_number
        return (
            new_balance,
            new_statement,
            new_withdrawal_number,
            msg + 
            f"{Pu.YELLOW }Saldo: R$ {new_balance:.2f}\n{Pu.RESET_COLOR}" + 
            f"{Pu.YELLOW}Valor do saque: R$ {value:.2f}\n{Pu.RESET_COLOR}"
            )

    return (
        balance,
        statement,
        withdrawal_number,
        msg
        )

    
  
def show_statement(balance: float, /, *, statement: str)-> None:
    clear()
    print(Pu.YELLOW + "EXTRATO".center(50, "=") + Pu.RESET_COLOR)
    print("Não foram realizadas movimentações." if not statement else statement)
    print(Pu.GREEN + f"\nSaldo: R$ {balance:.2f}")
    print(Pu.YELLOW + "FIM".center(50, "=") + Pu.RESET_COLOR)



def create_new_user(cpf: str, name:str, date_of_birth:str, address: str)-> tuple[User, str]:
    clear()
    user: User = {
        "cpf": cpf,
        "name": name,
        "date_of_birth": date_of_birth,
        "address": address,
        "accounts": []
    }

    msg = f"{Pu.GREEN}Usuário {Pu.YELLOW}{user['name']}{Pu.GREEN} criado com sucesso!{Pu.RESET_COLOR}"
    
    return user, msg



def create_new_account(
    cpf: str, 
    users: Users, 
    account_number: int,
    bank_branch: str = "0001"
    ) -> tuple[User|None, Account|None, str, int]|None:
    
    user = filter_user(cpf, users)
    
    if user:
        new_account_number: int = 1 + account_number
        msg = f"{Pu.GREEN}Conta {new_account_number}, criada com sucesso!{Pu.RESET_COLOR}"
        account = {
            "bank_branch": bank_branch,
            "account_number": new_account_number,
        }
        return user, account, msg, new_account_number
    msg = f"{Pu.RED}Falha ao tentar criar uma nova conta. {Pu.BOLD}{Pu.BB}Usuário não cadastrado!{Pu.RESET_COLOR}"
    return None, None, msg, account_number



def users_list(users: Users):
    clear()
    result: str = ""
    if len(users) == 0:
        result += f"{Pu.RED}Não há nenhum usuário na base de dados!{Pu.RESET_COLOR}"
        return result
    for user in users:
        if user:
            result += Pu.YELLOW + "Informações do usuário".center(50,"-") + Pu.RESET_COLOR
            result += Pu.GREEN + f"\n\nNome:\t {user["name"]}"
            result += f"\nCPF:\t {user["cpf"]}" + Pu.RESET_COLOR
            result += f"\n{Pu.YELLOW}" + "Informações de conta(s)".center(50,"-") + Pu.RESET_COLOR
            if user["accounts"]:
                for account in user["accounts"]:
                    result += Pu.GREEN + f"\n\nAgencia: \t{account["bank_branch"]}"
                    result += f"\nNúmero da conta: {account["account_number"]}" + Pu.RESET_COLOR
                
            else:
                result += f"{Pu.RED}\nO usuário não possui conta!{Pu.RESET_COLOR}"
            result += f"\n{Pu.YELLOW}" + "".center(50,"=") + Pu.RESET_COLOR
        
    return result
                
                

def accounts_list(users: Users):
    clear()
    result: str = ""
    if len(users) == 0:
        result += f"{Pu.RED}Nenhuma conta encontrada em nossa base de dados!{Pu.RESET_COLOR}"
        return result
    
    users = [user for user in users if len(user["accounts"]) > 0]
    for user in users:
        if user["accounts"]:
            for account in user["accounts"]:
                result += Pu.GREEN + f"\n\nAgencia: \t{account['bank_branch']}"
                result += f"\nConta: \t\t{account['account_number']}" + Pu.RESET_COLOR
                result += f"\n{Pu.YELLOW}Usuario: \t{user['name']}" + Pu.RESET_COLOR
                result += f"\n{Pu.YELLOW}CPF: \t\t{user['cpf']}" + Pu.RESET_COLOR
    print(users)
    if result == "":
        result += f"{Pu.RED}Nenhuma conta encontrada em nossa base de dados!{Pu.RESET_COLOR}"
    return result

