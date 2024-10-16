import os
from type_define import * 
class Pu:
    RED = "\033[31m"
    YELLOW = Y = "\033[33m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    BOLD = B = "\033[1m"
    BLUE_BACKGROUND = BB= "\033[44m"
    RESET_COLOR = RC = "\033[0m"

def color_menu_character (letra: str)-> str:
    return f"{Pu.B}{Pu.Y}{Pu.BB}[{letra}]{Pu.RC}"
   
def clear() -> None:
    my_print("")
    
def my_print(msg: str|Accounts|Account|User|Users) -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(msg)
    
    
def println(msg:str)-> None:
    print(msg + "\n")


    