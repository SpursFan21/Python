class ATM:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self):
        try:
            deposit = float(input("Enter a deposit amount: "))
            if deposit <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.balance += deposit
            print(f"Deposit successful, your current balance is now {self.balance}")
        except ValueError as ve:
            print(f"Error: {ve}")

    def withdraw(self):
        try:
            withdraw = float(input("Enter an amount you want to withdraw: "))
            if withdraw <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if withdraw > self.balance:
                raise ValueError("Insufficient funds.")
            self.balance -= withdraw
            print(f"Withdrawal successful, your current balance is {self.balance}")
        except ValueError as ve:
            print(f"Error: {ve}")

if __name__ == "__main__":
    atm = ATM()
    while True:
        print("Options:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            atm.deposit()
        elif choice == "2":
            atm.withdraw()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
