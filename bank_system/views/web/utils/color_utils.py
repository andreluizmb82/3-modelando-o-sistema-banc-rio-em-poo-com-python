RED = "[31m"
GREEN = "[32m"
YELLOW = "[33m"

RESET_COLOR = RC = "[0m"


def decode_colors(msg: str) -> str:
    msg = msg.replace("\n", "<br>")
    msg_list = msg.split("\033")
    new_msg = ""
    for part in msg_list:
        if part.startswith(RED):
            part = part.replace(RED, "<span class='red'>") + "</span>"
        elif part.startswith(YELLOW):
            part = part.replace(YELLOW, "<span class='yellow'>") + "</span>"
        elif part.startswith(GREEN):
            part = part.replace(GREEN, "<span class='green'>") + "</span>"
        elif RESET_COLOR in part:
            part = part.replace(RESET_COLOR, "")
            
        new_msg += part
        
    return new_msg



if __name__ == "__main__":
    msg = "Olá, seja bem vindo ao \033[33mBanco Python! \033[31m\nOlá, seja bem vindo ao \033[32mBanco Python!\033[0m"
    print(decode_colors(msg))