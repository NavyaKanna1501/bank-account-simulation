from bank_account import BankAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount

def display_menu():
    """Display menu options"""
    print("\n" + "="*50)
    print("BANK ACCOUNT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Create Savings Account")
    print("2. Create Checking Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. View Account Info")
    print("6. Add Interest (Savings Only)")
    print("7. View Transaction History")
    print("8. Exit")
    print("="*50)

def main():
    """Main application logic"""
    accounts = {}
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        try:
            if choice == "1":
                name = input("Enter account holder name: ").strip()
                initial = float(input("Enter initial balance: "))
                rate = float(input("Enter annual interest rate (e.g., 0.03 for 3%): "))
                accounts[name] = SavingsAccount(name, initial, rate)
                print(f"✓ Savings account created for {name}")
            
            elif choice == "2":
                name = input("Enter account holder name: ").strip()
                initial = float(input("Enter initial balance: "))
                limit = float(input("Enter overdraft limit: "))
                accounts[name] = CheckingAccount(name, initial, limit)
                print(f"✓ Checking account created for {name}")
            
            elif choice == "3":
                name = input("Enter account holder name: ").strip()
                if name in accounts:
                    amount = float(input("Enter deposit amount: "))
                    accounts[name].deposit(amount)
                else:
                    print("Account not found!")
            
            elif choice == "4":
                name = input("Enter account holder name: ").strip()
                if name in accounts:
                    amount = float(input("Enter withdrawal amount: "))
                    accounts[name].withdraw(amount)
                else:
                    print("Account not found!")
            
            elif choice == "5":
                name = input("Enter account holder name: ").strip()
                if name in accounts:
                    accounts[name].get_account_info()
                else:
                    print("Account not found!")
            
            elif choice == "6":
                name = input("Enter account holder name: ").strip()
                if name in accounts:
                    if isinstance(accounts[name], SavingsAccount):
                        accounts[name].add_interest()
                    else:
                        print("Interest is only available for Savings Accounts!")
                else:
                    print("Account not found!")
            
            elif choice == "7":
                name = input("Enter account holder name: ").strip()
                if name in accounts:
                    accounts[name].print_transaction_history()
                else:
                    print("Account not found!")
            
            elif choice == "8":
                print("Thank you for using Bank Account Management System!")
                break
            
            else:
                print("Invalid choice! Please enter a number between 1-8.")
        
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()