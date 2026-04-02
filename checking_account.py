from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        available = self.get_balance() + self.overdraft_limit
        if amount > available:
            raise Exception(f"Cannot withdraw ${amount}. Available (including overdraft): ${available:.2f}")
        balance = self.get_balance() - amount
        self._BankAccount__balance = balance
        self._BankAccount__transaction_history.append(f"Withdraw: -{amount}")
        print(f"✓ Withdrew ${amount}. New balance: ${balance:.2f}")
        return balance
    
    def get_account_info(self):
        super().get_account_info()
        print(f"Overdraft Limit: ${self.overdraft_limit:.2f}")