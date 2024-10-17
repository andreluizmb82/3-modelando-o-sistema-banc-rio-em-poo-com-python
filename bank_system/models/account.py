from abc import ABC
from typing import Any
from statement import Statement
from transactions import Deposit, Withdraw

RED = "\033[31m"
YELLOW = Y = "\033[33m"
GREEN = "\033[32m"
RESET_COLOR = RC = "\033[0m"

class Account (ABC):
    _total_number_of_accounts: int = 0
    
    _accounts: list[Any] = []
    def __init__(
        self, 
        cpf_client: str,
        balance: float = 0,  
        bank_branch: str = "0001",
        statement: Statement|None = None
    ) -> None:
        self._limit_number_of_withdrawals = 3
        self._limit_amount_per_withdrawal = 500  
        self._withdrawal_number = 0
        
        self._balance = balance
        self._bank_branch = bank_branch
        self._cpf_client = cpf_client
        
        Account._total_number_of_accounts += 1
        self._account_number = Account._total_number_of_accounts
        
        if statement:
            self._statement = statement
        else:
            self._statement = Statement()
            
        Account._accounts.append(self)
            
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
    
    @staticmethod
    def get_total_number_of_accounts():
        return Account._total_number_of_accounts
    
    @staticmethod
    def get_accounts() -> list[Any]:
        return Account._accounts[:]
    
    @classmethod
    def get_str_accounts(cls) -> str:
        if cls._accounts == []:
            return "Nenhuma conta encontrada em nossa base de dados!"
        accounts = ""
        for account in Account._accounts:
            accounts += account.get_str_account()
        return accounts
    
    def get_str_account(self) -> str:
        # Header
        str_account = f"{YELLOW}\n" + "".center(52,"=") + RESET_COLOR
        
        # Body
        str_account += f"{YELLOW}\nConta:   {self.account_number}{RESET_COLOR}"
        str_account += f"{YELLOW}\nAgência: {self.bank_branch}{RESET_COLOR}"
        str_account += f"{YELLOW}\nCPF:     {self.cpf_client}{RESET_COLOR}"
        str_account += f"{YELLOW}\nSaldo:   {GREEN}R$ {self.balance:.2f}{RESET_COLOR}"
        
        # Footer
        str_account += f"{YELLOW}\n" + "".center(52,"=") + RESET_COLOR
        
        return str_account
    
    def _validate_withdrawal(
        self, 
        value: float, 
        balance: float,
    ) -> tuple[bool, str]:
        if value > balance: # excedeu_saldo
            return (
                False, 
                f"{RED}Operação falhou! Você não tem saldo suficiente.{RESET_COLOR}"
            )
        if value > self._limit_amount_per_withdrawal: # excedeu_limite
            return (
                False, 
                f"{RED}Operação falhou! O valor do saque excede o limite de {self._limit_amount_per_withdrawal}.{RESET_COLOR}"
            )
        if self._withdrawal_number >= self._limit_number_of_withdrawals: # excedeu_saques
            return (
                False, 
                f"{RED}Operação falhou! Número máximo de {self._limit_number_of_withdrawals} saques diários excedido.{RESET_COLOR}"
            )
        if(value <= 0):
            return (
                False,
                f"{RED}Operação falhou! O valor de R${value} é inválido.{RESET_COLOR}"
            )
        return (
            True, 
            f"{GREEN}Saque realizado com sucesso!\n{RESET_COLOR}"
        )
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ".join(
            [
                f"{key} = {value}" for key, value in self.__dict__.items()
            ])}"
        
    def withdraw(self, value: float) -> str:
        valid, msg = self._validate_withdrawal(
            value, 
            self._balance, 
       )
        if valid:
            self._balance -= value
            self._statement.add_transaction(Withdraw(value))
            self._withdrawal_number += 1
        return msg
    def deposit(self, value: float):
        if value <= 0:
            return f"{RED}Operação falhou! O valor de R${value} é inválido.{RESET_COLOR}"
        self._balance += value
        self._statement.add_transaction(Deposit(value))
        return f"{GREEN}Depósito realizado com sucesso!\n{RESET_COLOR}"
    
    def get_statement(self)-> str:
        return self._statement.get_statement(self._balance)

        
        

    
class Client_individual(Account):   
    
    @staticmethod
    def new_account( 
        cpf_client: str
    ) -> Account:
        return Account(cpf_client, 0)
    
    def __str__(self) -> str:
        return super().__str__()
    
    
    
if __name__ == "__main__":
    a = Client_individual.new_account("111.111.111-11")
    print(a)
    
    b = Client_individual.new_account("111.111.111-11")
    print(b)
    
    c = Client_individual.new_account("222.222.222-22")
    print(c)
    
    print(c.withdraw(100))
    print(c.deposit(2000))
    print(c.withdraw(-100))
    print(c.withdraw(700))
    print(c.withdraw(500))
    print(c.withdraw(500))
    print(c.withdraw(500))
    print(c.withdraw(500))
        
    print(c.get_statement())
    print(Account.get_str_accounts())