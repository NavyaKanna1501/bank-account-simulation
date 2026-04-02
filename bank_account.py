class BankAccount:
    """Base class for all bank accounts"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.__transaction_history = []
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self.__transaction_history.append(f"Deposit: +{amount}")
        print(f"✓ Deposited ${amount}. New balance: ${self.__balance:.2f}")
        return self.__balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise Exception("Insufficient funds")
        self.__balance -= amount
        self.__transaction_history.append(f"Withdraw: -{amount}")
        print(f"✓ Withdrew ${amount}. New balance: ${self.__balance:.2f}")
        return self.__balance
    
    def get_balance(self):
        return self.__balance
    
    def get_account_info(self):
        print(f"\n{'='*50}")
        print(f"Account Owner: {self.owner}")
        print(f"Account Type: {self.__class__.__name__}")
        print(f"Current Balance: ${self.__balance:.2f}")
        print(f"{'='*50}\n")
    
    def print_transaction_history(self):
        print(f"\nTransaction History for {self.owner}:")
        if not self.__transaction_history:
            print("No transactions yet")
        else:
            for transaction in self.__transaction_history:
                print(f"  - {transaction}")
        print()