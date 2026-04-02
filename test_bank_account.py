import unittest
from bank_account import BankAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount

class TestBankAccount(unittest.TestCase):
    
    def setUp(self):
        self.account = BankAccount("John", 1000)
    
    def test_deposit(self):
        balance = self.account.deposit(500)
        self.assertEqual(balance, 1500)
    
    def test_withdraw(self):
        balance = self.account.withdraw(300)
        self.assertEqual(balance, 700)
    
    def test_insufficient_funds(self):
        with self.assertRaises(Exception):
            self.account.withdraw(2000)
    
    def test_invalid_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

class TestSavingsAccount(unittest.TestCase):
    
    def setUp(self):
        self.account = SavingsAccount("Alice", 1000, 0.06)
    
    def test_add_interest(self):
        initial_balance = self.account.get_balance()
        self.account.add_interest()
        new_balance = self.account.get_balance()
        self.assertGreater(new_balance, initial_balance)

class TestCheckingAccount(unittest.TestCase):
    
    def setUp(self):
        self.account = CheckingAccount("Bob", 500, 200)
    
    def test_overdraft_withdrawal(self):
        balance = self.account.withdraw(600)
        self.assertEqual(balance, -100)
    
    def test_overdraft_limit_exceeded(self):
        with self.assertRaises(Exception):
            self.account.withdraw(1000)

if __name__ == "__main__":
    unittest.main()