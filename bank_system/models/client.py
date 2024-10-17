from abc import ABC
from account import Account

class Client(ABC):
    def __init__(self, address: str) -> None:
        self.address = address
        
    def perform_transaction(self, account: Account) -> None:
        pass
    
    def add_account(self, account: Account) -> None:
        pass


class Individual(Client): 
    def __init__(self, cpf: str, name: str, date_of_birth: str, address: str) -> None:
        super().__init__(address=address)
        self._cpf = cpf
        self._name = name
        self._date_of_birth = date_of_birth
        
    @property
    def cpf(self) -> str:
        return self._cpf
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def date_of_birth(self) -> str:
        return self._date_of_birth
    
    