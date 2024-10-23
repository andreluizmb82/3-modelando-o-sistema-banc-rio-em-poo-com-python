from views.console.menu_console import Menu
from views.web.menu_html import start_menu_web
from utils.console_utils import *

def main()-> None:
    clear()
    while True:
        OI = f"{BLUE}Olá, seja bem vindo ao Banco Python!{RESET_COLOR}"
        MENU = f"""
{YELLOW}---- MENU ------------------------------------------{RESET_COLOR}
{color_menu_character('c')}\t Entrar em modo console \t\t   |
{color_menu_character("w")}\t Entrar em modo web    \t\t\t   |
{color_menu_character('q')}\t Sair                  \t\t\t   | 
{OI}\t\t   | 
{YELLOW}----------------------------------------------------{RESET_COLOR}
=>"""            

        operation = input(MENU).lower()
        match operation:
            case "q":
                clear()
                break
            case "c":
                clear()
                Menu.start_menu()
            case "w":
                clear()
                start_menu_web()
                
            case _:
                print(MSG_INVALID)
 
    
    #Menu.start_menu()
        
if __name__ == "__main__":
    main()
