from transactions import Transaction, Deposit, Withdraw
from datetime import datetime

RED = "\033[31m"
YELLOW = Y = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"
BOLD = B = "\033[1m"
BLUE_BACKGROUND = BB= "\033[44m"
RESET_COLOR = RC = "\033[0m"


class Statement:
    def __init__(self) -> None:
        self._transactions: list[Transaction] = []
        
    def add_transaction(self, transaction: Transaction) -> None:
        self._transactions.append(transaction)
        
    def __str__(self) -> str:
        statement_body = ""
        
        for transaction in self._transactions:
            statement_body += transaction.__str__()
        
        statement =YELLOW + "EXTRATO".center(50, "=") + RESET_COLOR
        if statement_body == "":
            statement += RED + "\nNão foram realizadas movimentações."
        else:
            statement += statement_body
        
        return statement
        
if __name__ == "__main__":
    statement = Statement()
    
    print (statement)
    
    date = datetime.now()
    ste_date = date.strftime("%d/%m/%Y %H:%M")
    statement.add_transaction(Deposit(100))
    statement.add_transaction(Deposit(150))
    statement.add_transaction(Withdraw(200))
    print (statement)