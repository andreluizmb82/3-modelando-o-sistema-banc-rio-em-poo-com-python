from abc import ABC, abstractmethod
from typing import Any
from .account import Account

RED = "\033[31m"
YELLOW = Y = "\033[33m"
GREEN = "\033[32m"
RESET_COLOR = RC = "\033[0m"

class Client(ABC):
    _clients: list[Any] = []
    def __init__(self, id: str, address: str) -> None:
        self._id: str = id
        self.address: str = address
        self.accounts: list[Account] = []
        Client._clients.append(self)
    
    @property
    def id(self) -> str:
        return self._id
    
    @classmethod
    def get_clients(cls) -> list[Any]:
        return cls._clients[:]
    
    @classmethod
    def get_str_clients(cls) -> str:
        if cls._clients == []:
            return f"{RED}Nenhum cliente encontrado em nossa base de dados!{RESET_COLOR}"
        
        clients = ""
        for client in cls._clients:
            clients += client.get_str_client()
        return clients
    
    @staticmethod
    def get_client(id: str) -> Any:
        result = [client for client in Client.get_clients() if client.id == id]
        return result[0] if len(result) > 0 else None
        
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ".join(
            [
                f"{key} = {value}" for key, value in self.__dict__.items()
            ])}"

    
    


class Individual(Client): 
    def __init__(
        self, 
        cpf: str, 
        name: str, 
        date_of_birth: str, 
        address: str, 
        create_account: bool = False
    ) -> None:
        
        clients = Client.get_clients()
        for client in clients : 
            if client.id == cpf:
                 raise ValueError(RED + "O cpf: " + YELLOW + cpf + RED + " ja existe em nossa base de dados!" + RESET_COLOR)
             
        super().__init__(id = cpf, address=address)
        
        self._name = name
        self._date_of_birth = date_of_birth
        if create_account:
            self.create_account(cpf)
            
        
    @property
    def cpf(self) -> str:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def date_of_birth(self) -> str:
        return self._date_of_birth
    
    def add_account(self, account: Account) -> str:
        if account in self.accounts:
            return RED + "\nEssa conta já está vinculada a este usuário!" + RESET_COLOR
        if account.cpf_client != self.cpf:
            return RED + "\nEssa conta não está vinculada a este usuário!" + RESET_COLOR
        self.accounts.append(account)
        return GREEN + "\nConta vinculada com sucesso!" + RESET_COLOR
    
    def link_account(self, account: Account) -> str: 
        if account in self.accounts:
            return RED + "\nEssa conta já está vinculada a este usuário!" + RESET_COLOR
        if account.cpf_client != self.cpf:
            return RED + "\nEssa conta pertence a outro usuário!" + RESET_COLOR
        self.accounts.append(account)
        return GREEN + "\nConta vinculada com sucesso!" + RESET_COLOR
    
    def create_account(self, cpf: str = "") -> str:

        account: Account = Account(cpf)

        if account:
            self.accounts.append(account)
            return GREEN + "Conta criada com sucesso!" + RESET_COLOR
        return RED + "Falha ao criar uma nova conta!" + RESET_COLOR
    
    def get_str_client(self) -> str:
        # Header
        client = YELLOW + "\n" + " Clientes ".center(52,"=") + RESET_COLOR
        
        # Body
        client += f"{YELLOW}\nNome: {self.name}{RESET_COLOR}"
        client += f"{YELLOW}\nCPF: {self.cpf}{RESET_COLOR}"
        client += f"{YELLOW}\nData de nascimento: {self.date_of_birth}{RESET_COLOR}"
        client += f"{YELLOW}\nEndereço: {self.address}{RESET_COLOR}"
        
        client += YELLOW + "\n" + " Contas ".center(52,"-") + RESET_COLOR
        if len(self.accounts) <= 0:
            client += f"{RED}\nNenhuma conta vinculada a este usuário!{RESET_COLOR}"
        else:
            for account in self.accounts:
                client += account.get_str_account()
            
        
        
        # Footer
        client += YELLOW + "\n" + "".center(52,"=") + RESET_COLOR
        
        return client
    
    
    @property
    def str_accounts(self) -> str:
        accounts = ""
        for account in self.accounts:
            accounts += account.get_str_account()
        return accounts
    
if __name__ == "__main__":
    try:
        a = Individual("111.111.111-11", "Joaão", "01/01/2000", "Rua dos Bobos, 0", True)
        print(a)
    except ValueError as exp:
        print(exp)
    
    try:
        b = Individual("111.111.111-11", "Joaão-Dinovo", "01/01/2000", "Rua dos Bobos, 0", False)
        print(b)
    except ValueError as exp:
        print(exp)
    
    try:
        c = Individual("222.222.222-22", "Maria", "01/01/2000", "Rua dos Bobos, 0", True)
        print(c)
        
        c.create_account()
        
        
        print(c.str_accounts)
        
        print(c.get_str_clients())
    except ValueError as exp:
        print(exp)
        