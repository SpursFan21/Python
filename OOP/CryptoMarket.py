class CryptoMarket:
    crypto1 = 2250.10  # amount of crypto1 available for purchase in marketplace
    crypto_value1 = 22.70  # current price of crypto1
    crypto2 = 1337.0
    crypto_value2 = 10.14
    crypto3 = 10288.32
    crypto_value3 = 2.41
    crypto4 = 244.77
    crypto_value4 = 77.29
    crypto5 = 55.4
    crypto_value5 = 1.07

    @classmethod
    def getCryptoValues(cls):
        return (
            cls.crypto_value1,
            cls.crypto_value2,
            cls.crypto_value3,
            cls.crypto_value4,
            cls.crypto_value5
        )


class YourWallet(CryptoMarket):
    def __init__(self, u_crypto1=0, u_crypto2=0, u_crypto3=0, u_crypto4=0, u_crypto5=0):
        super().__init__()
        self.u_crypto1 = u_crypto1
        self.u_crypto2 = u_crypto2
        self.u_crypto3 = u_crypto3
        self.u_crypto4 = u_crypto4
        self.u_crypto5 = u_crypto5

    def getValue(self):
        crypto_values = self.getCryptoValues()
        return (
            self.u_crypto1 * crypto_values[0],
            self.u_crypto2 * crypto_values[1],
            self.u_crypto3 * crypto_values[2],
            self.u_crypto4 * crypto_values[3],
            self.u_crypto5 * crypto_values[4]
        )

    def viewWallet(self):
        val1, val2, val3, val4, val5 = self.getValue()
        print(f"crypto1 {self.u_crypto1}")
        print(f"Valued at {val1}")
        print(f"crypto2 {self.u_crypto2}")
        print(f"Valued at {val2}")
        print(f"crypto3 {self.u_crypto3}")
        print(f"Valued at {val3}")
        print(f"crypto4 {self.u_crypto4}")
        print(f"Valued at {val4}")
        print(f"crypto5 {self.u_crypto5}")
        print(f"Valued at {val5}")

    def updateBalance(self, choice, quantity):
        if choice == 1:
            self.u_crypto1 += quantity
        elif choice == 2:
            self.u_crypto2 += quantity
        elif choice == 3:
            self.u_crypto3 += quantity
        elif choice == 4:
            self.u_crypto4 += quantity
        elif choice == 5:
            self.u_crypto5 += quantity
        else:
            print("Invalid choice")


class Transaction(CryptoMarket):
    @staticmethod
    def purchase(wallet):  # Accept wallet instance as argument
        print("Enter which crypto you would like to buy")
        choice = int(input("1 for crypto1, 2 for crypto2, 3 for crypto3, 4 for crypto4, or 5 for crypto5: "))
        if choice in range(1, 6):
            crypto_name = f'crypto{choice}'
            crypto_value = getattr(CryptoMarket, f'crypto_value{choice}')
            print(f"Current price of {crypto_name} is {crypto_value}")
            choice2 = int(input("Enter 1 to continue purchase or 2 to go back: "))
            if choice2 == 1:
                quantity = float(input("Enter the quantity you wish to buy: "))
                print(f"You have purchased {quantity} units of {crypto_name}")
                wallet.updateBalance(choice, quantity)  # Update balance in existing wallet instance
            elif choice2 == 2:
                return
            else:
                print("Invalid input, try again")
        else:
            print("Invalid input, try again")


if __name__ == "__main__":
    wallet = YourWallet()  # Instantiate YourWallet outside the loop
    while True:
        print("Welcome to Duncan's CryptoMarket")
        choice3 = int(input("Enter 1 to make a Purchase, 2 to View Your Wallet, or 3 to Exit: "))
        if choice3 == 1:
            Transaction.purchase(wallet)  # Pass the wallet instance to purchase method
        elif choice3 == 2:
            wallet.viewWallet()  # Use the existing wallet instance to view the wallet
        elif choice3 == 3:
            break
        else:
            print("Invalid input try again!")
