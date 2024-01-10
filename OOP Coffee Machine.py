class CoffeeMachine:
    def __init__(self, water, milk, coffee, recipes):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.recipes = recipes
        self.selection = 0
        self.exitLoop = False
        self.create = False
        self.changeTendered = 0

    def print_report(self):
        print(f"There is {self.water} ml of water")
        print(f"There is {self.milk} ml of milk")
        print(f"There is {self.coffee} g of coffee")

    def order(self):
        selection = int(input("Press 1 for Espresso, 2 for Latte, 3 for Cappuccino, 4 for report: "))
        if 1 <= selection <= 3:
            self.selection = selection - 1
            self.exitLoop = False
        elif selection == 4:
            self.print_report()
            self.selection = None
            self.exitLoop = True
        else:
            print("Invalid choice")
            self.selection = None
            self.exitLoop = True

    def check_resources(self):
        if (
            self.recipes[self.selection]["water"] >= self.water
            and self.recipes[self.selection]["milk"] >= self.milk
            and self.recipes[self.selection]["coffee"] >= self.coffee
        ):
            print(f"Your selection of {self.recipes[self.selection]['drink']} is available")
        else:
            print(f"Your selection of {self.recipes[self.selection]['drink']} is not available due to a lack of resources")

    def get_cost(self):
        print("Coffee Type:", self.recipes[self.selection]["drink"])
        print("Cost:", self.recipes[self.selection]["cost"])

    def process_coins(self):
        quarters = int(input("Enter Quarters: "))
        dimes = int(input("Enter Dimes: "))
        nickels = int(input("Enter Nickels: "))
        pennies = int(input("Enter Pennies: "))
        self.changeTendered = float((quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + pennies)

    def process_payment(self):
        cost = self.recipes[self.selection]["cost"]
        change = self.changeTendered - cost
        if change >= 0:
            print("Payment successful!")
            print(f"Change: {change}")
            self.create = True
        elif change < 0:
            print("Payment incomplete")
            print(f"Remaining balance: {change}")
            cost = change
            self.process_coins()
            self.process_payment()
        else:
            print("A payment error has occurred")
            self.exitLoop = True

    def make_coffee(self):
        if self.create:
            print(f"Please take your {self.recipes[self.selection]['drink']}")
        else:
            print("Something went wrong, here is your change back")
        self.exitLoop = True


# Define the recipes
recipes = [
    {"drink": "espresso", "water": 50, "milk": 0, "coffee": 18, "cost": 0.50},
    {"drink": "latte", "water": 200, "milk": 150, "coffee": 24, "cost": 0.85},
    {"drink": "cappuccino", "water": 250, "milk": 100, "coffee": 24, "cost": 1.10},
]

# Create an instance of CoffeeMachine
coffee_machine = CoffeeMachine(water=300, milk=200, coffee=100, recipes=recipes)

while True:
    print(logo)
    while not coffee_machine.exitLoop:
        try:
            coffee_machine.order()
            if coffee_machine.exitLoop:
                break
            coffee_machine.check_resources()
            coffee_machine.get_cost()
            coffee_machine.process_coins()
            coffee_machine.process_payment()
            coffee_machine.make_coffee()

        except ValueError as e:
            print(f"Error: {e} try again")
            continue

    user_choice = input("Do you want to order again? (yes/no): ").lower()
    if user_choice != 'yes':
        print("Invalid input. Please enter 'yes' to continue ordering or any other key to exit.")
        break
