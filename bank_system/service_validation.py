from utils_print import Pu
from type_define import Users, User

def validate_deposit(valor: float) -> bool:
    return valor >= 0

def validate_withdrawal(
    balance: float, 
    value: float, 
    withdrawal_amount_limit: float,
    withdrawal_number: int,
    withdrawal_number_limit: int
    ) -> tuple[bool, str]:
    if value > balance: # excedeu_saldo
        return (
            False, 
            f"{Pu.RED}Operação falhou! Você não tem saldo suficiente.{Pu.RESET_COLOR}"
        )
    if value > withdrawal_amount_limit: # excedeu_limite
        return (
            False, 
            f"{Pu.RED}Operação falhou! O valor do saque excede o limite de {withdrawal_amount_limit}.{Pu.RESET_COLOR}"
        )
    if withdrawal_number >= withdrawal_number_limit: # excedeu_saques
        return (
            False, 
            f"{Pu.RED}Operação falhou! Número máximo de {withdrawal_number_limit} saques diários excedido.{Pu.RESET_COLOR}"
        )
    if(value <= 0):
        return (
            False,
            f"{Pu.RED}Operação falhou! O valor de R${value} é inválido.{Pu.RESET_COLOR}"
        )
    return (
        True, 
        f"{Pu.GREEN}Saque realizado com sucesso!\n{Pu.RESET_COLOR}"
    )
    
    
def filter_user(cpf: str, users: Users) -> User | None:
    filtered_users = [user for user in users if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None