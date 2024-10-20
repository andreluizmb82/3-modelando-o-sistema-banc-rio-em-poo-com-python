from .transactions import Transaction, Deposit, Withdraw

RED = "\033[31m"
YELLOW = Y = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"
BOLD = B = "\033[1m"
BLUE_BACKGROUND = BB= "\033[44m"
RESET_COLOR = RC = "\033[0m"


class Statement:
    def __init__(self) -> None:
        self._history: str = ""
        
    def add_transaction(self, transaction: Transaction) -> None:
        self._history += str(transaction)
        
    
    def get_statement(self, balance: float) -> str:
        # Header 
        statement =YELLOW + "\n" + "EXTRATO".center(52, "=") + RESET_COLOR
        
        # Body
        if self._history == "":
            statement += RED + "\nNão foram realizadas movimentações."  + RESET_COLOR
        else:
            statement += self._history
                   
        # Footer
        statement += GREEN + f"\n\nSaldo: R$ {balance:.2f}" + RESET_COLOR
        statement += (YELLOW + "\n" + " FIM ".center(52, "=") + RESET_COLOR)
        return statement
        
    def __str__(self) -> str:
        return self._history
        
if __name__ == "__main__":
    statement = Statement()
    
    print (statement)
    

    statement.add_transaction(Deposit(100))
    statement.add_transaction(Deposit(150))
    statement.add_transaction(Withdraw(200))
    print (statement)