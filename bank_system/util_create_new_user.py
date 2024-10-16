from service_validation import filter_user
from service_account import create_new_user
from type_define import Users, User
from utils_print import Pu, clear

# This is an impure function, its purpose is to remove this code 
# from the main() function and keep the create_new_user and filter_user functions pure
def util_create_new_user(users: Users)-> tuple[User, str, bool]:
    clear()
    cpf = input(f"{Pu.YELLOW}Informe o CPF do usuário: {Pu.RESET_COLOR}")
    user = filter_user(cpf, users)
    if user:
        msg =f"{Pu.RED}O usuario de CPF {cpf} já existe!{Pu.RESET_COLOR}"
        return user, msg, False
    name = input(f"{Pu.YELLOW}Informe o nome completo: {Pu.RESET_COLOR}")
    date_of_birth = input(f"{Pu.YELLOW}Informe a data de nascimento (dd-mm-aaaa): {Pu.RESET_COLOR}")
    address = input(f"{Pu.YELLOW}Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): {Pu.RESET_COLOR}")
    
    user, msg = create_new_user(cpf, name, date_of_birth, address)
    return user, msg, True
    
    