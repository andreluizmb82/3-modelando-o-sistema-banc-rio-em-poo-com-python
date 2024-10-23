import os

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

