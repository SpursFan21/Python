class ATM:
    balance = 0.0
    
    @staticmethod
    def deposit(balance):
        deposit = float(input("Enter a deposit amount: "))
        balance += deposit
        print(f"Deposit successful, your current balance is now {balance}")
        return balance
    
    @staticmethod
    def withdraw(balance):
        withdraw = float(input("Enter an amount you want to withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
            print(f"Withdrawal successful, your current balance is {balance}")
            return balance
        else:
            print("Insufficient funds!")

if __name__ == "__main__":
    balance = 0.0
    while True:
        print("\n ATM Options:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            balance = ATM.deposit(balance)
        elif choice == "2":
            balance = ATM.withdraw(balance)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
