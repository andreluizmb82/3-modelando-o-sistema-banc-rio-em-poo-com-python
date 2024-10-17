from account import Account

from abc import ABC, abstractmethod
class Transaction(ABC):
    def __init__(self, value: float, date: str) -> None:
        self.value: float = value
        self.date: str = date
        
    
    @abstractmethod
    def register(self, account: Account) -> None:
        pass

class Withdraw(Transaction): 
    def register(self, account: Account) -> None:
        # TODO
        pass

class Deposit(Transaction): 
    def register(self, account: Account) -> None:
        # TODO
        pass 