from abc import ABC
from .statement import Statement

class Account (ABC):
    def __init__(
        self, 
        balance: float, 
        account_number: int, 
        cpf_client: str,
        statement: Statement|None,
        bank_branch: str = "0001"
    ) -> None:
        self._balance = balance
        self._account_number = account_number
        self._bank_branch = bank_branch
        self._cpf_client = cpf_client
        if statement:
            self._statement = statement
        else:
            self._statement = Statement()
            
    @property
    def balance(self) -> float:
        return self._balance
    
    @property
    def account_number(self) -> int:
        return self._account_number
    
    @property
    def bank_branch(self) -> str:
        return self._bank_branch
    @property
    def statement(self) -> Statement:
        return self._statement
    
    @property
    def cpf_client(self) -> str:
        return self._cpf_client
    

        
    
    
class Client_individual(Account):
    def __init__(
        self, 
        balance: float, 
        account_number: int, 
        bank_branch: str, 
        cpf_client: str,
        statement: Statement
    ) -> None:
        pass