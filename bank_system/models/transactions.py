from datetime import datetime

RED = "\033[31m"
GREEN = "\033[32m"
RESET_COLOR = RC = "\033[0m"

from abc import ABC

class Transaction(ABC):
    def __init__(self, value: float) -> None:
        self._value: float = value
        date = datetime.now()
        self._date: str = date.strftime("%d/%m/%Y %H:%M")
    
    @property
    def value(self) -> float:
        return self._value
    
    @property
    def date(self) -> str:
        return self._date    


class Withdraw(Transaction): 
    def __str__(self) -> str:
        return RED + f"Saque: \t\tR$ {self.value:.2f} \t {self.date}\n" + RESET_COLOR
    

class Deposit(Transaction): 
    def __str__(self) -> str:
        return GREEN + f"Depósito: \tR$ {self.value:.2f}\t {self.date}\n" + RESET_COLOR
    
if __name__ == "__main__":
    print(Withdraw(100))
    print(Deposit(100))