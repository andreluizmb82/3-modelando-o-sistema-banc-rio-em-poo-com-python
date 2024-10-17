from transactions import Transaction

class Statement:
    def __init__(self) -> None:
        self._transactions: list[Transaction] = []
        
    def add_transaction(self, transaction: Transaction) -> None:
        pass
        