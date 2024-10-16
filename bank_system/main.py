from service_account import *#menu, deposit, withdraw, show_statement, create_new_account
from service_validation import filter_user
from utils_print import my_print, Pu, clear
from util_create_new_user import util_create_new_user
from type_define import *

def main()-> None:
    balance:float = 0
    withdrawal_amount_limit: float = 500
    statement: str = ""
    withdrawal_number: int = 0
    WITHDRAWAL_NUMBER_LIMIT: int = 3
    users: Users = []
    user: User = {}
    account_number: int = 0
    bank_branch = "0001"
    while True:
        operacao = input(menu()).lower()
        match operacao:
            case "d":
                clear()
                value = float(input(f"{Pu.YELLOW}Informe o valor do depósito: R${Pu.RESET_COLOR}"))
                balance, statement, msg = deposit(balance, value, statement)
                my_print(msg)
                print(f"{Pu.YELLOW}Saldo: R$ {balance:.2f}{Pu.RESET_COLOR}")
                
            case "s":
                clear()
                value = float(input(f"{Pu.YELLOW}Informe o valor do saque: R${Pu.RESET_COLOR}"))
                balance, statement, withdrawal_number, msg = withdraw(
                    balance = balance,
                    value = value,
                    statement = statement,
                    withdrawal_amount_limit = withdrawal_amount_limit,
                    withdrawal_number = withdrawal_number,
                    withdrawal_number_limit = WITHDRAWAL_NUMBER_LIMIT
                )
                my_print(msg)
                
            case "e":
                show_statement(balance, statement = statement)
    
            case "nu":
                user, msg, is_nwe_user = util_create_new_user(users)
                if is_nwe_user and user:
                    users.append(user)
                my_print(msg)
                
            case "nc":
                clear()
                cpf = input(f"{Pu.YELLOW}Informe o cpf do usuário: ")
                
                user, new_account, msg, account_number = create_new_account(cpf, users, account_number, bank_branch)
                if new_account:
                    user["accounts"].append(new_account)
                
                my_print(msg)
                    
            case "bu":
                clear()
                cpf = input(f"{Pu.YELLOW}Informe o cpf do usuário: {Pu.RESET_COLOR}")
                user = filter_user(cpf, users)
                
                if user != None:
                    my_print(user)
                    continue
                my_print(f"{Pu.RED}Usuário não encontrado em nossa base de dados!{Pu.RESET_COLOR}")
                
            case "lu":
                print(users_list(users))
                
            case "lc":
                print(accounts_list(users))
                
            case "q":
                clear()
                break
            
            case _:
                my_print(f"{Pu.RED}Operação inválida, por favor selecione uma das opções disponíveis no menu.{Pu.RESET_COLOR}")
                
if __name__ == "__main__":
    main()
