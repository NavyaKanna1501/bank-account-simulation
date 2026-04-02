from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.03):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.get_balance() * (self.interest_rate / 12)
        self.deposit(interest)
        print(f"Interest added: ${interest:.2f} (Annual rate: {self.interest_rate*100}%)")
    
    def get_account_info(self):
        super().get_account_info()
        print(f"Interest Rate: {self.interest_rate*100}% per annum")