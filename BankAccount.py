class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposite ${amount}. New Balance is ${self.balance}")
        else:
            print("Invalid deposite amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount}. New Balance is ${self.balance}")
        else: 
            print("Insufficient funds or invalid withrawal amount.")
    
    def get_balance(self):
        return self.balance

def main():
    account_name = input("Enter account holder's name: ")
    account = BankAccount(account_name)

    while True:
        print("\nSelect an option")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter Your Choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposite: "))
            account.deposite(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            print(f"Your current balance is ${account.get_balance}")
        elif choice == '4':
            print("Thank you for using our bank system. Goodbye!!!")
        else : 
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()