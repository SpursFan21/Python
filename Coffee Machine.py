logo = """"
   ______      ________             __  ___           __    _          
  / ____/___  / __/ __/__  ___     /  |/  /___ ______/ /_  (_)___  ___ 
 / /   / __ \/ /_/ /_/ _ \/ _ \   / /|_/ / __ `/ ___/ __ \/ / __ \/ _ \
/ /___/ /_/ / __/ __/  __/  __/  / /  / / /_/ / /__/ / / / / / / /  __/
\____/\____/_/ /_/  \___/\___/  /_/  /_/\__,_/\___/_/ /_/_/_/ /_/\___/ 
                                                                       
"""
water = 300
milk = 200
coffee = 100
selection = 0
exitLoop = False
create = False
changeTendered = 0

recipe = [
    {
        "drink": "espresso",
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": .50
    },
    {
        "drink": "latte",
        "water": 200,
        "milk": 150,
        "coffee": 24, 
        "cost": .85        
    },
    {
        "drink": "cappuccino",
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 1.10       
    }
]

def printReport(water, milk, coffee):
    print(f"There is {water} ml of water")
    print(f"There is {milk} ml of milk")
    print(f"There is {coffee} g of coffee")

def order(water, milk, coffee):
    selection = int(input("Press 1 for Espresso, 2 for Latte, or 3 for Cappuccino: "))
    if 1 <= selection <= 3:
        selection -= 1
        return selection
    else:
        printReport(water, milk, coffee)
        exitLoop = True
        return exitLoop

def checkResources(selection):
    if selection == 0:
        if recipe[selection]["water"] >= 50 and recipe[selection]["milk"] >= 0 and recipe[selection]["coffee"] >= 18:
            print(f"Your selection of {recipe[selection]['drink']} is available")
        else:
            print(f"Your selection of {recipe[selection]['drink']} is not available due to a lack of resources")
    elif selection == 1:
        if recipe[selection]["water"] >= 200 and recipe[selection]["milk"] >= 150 and recipe[selection]["coffee"] >= 24:
            print(f"Your selection of {recipe[selection]['drink']} is available")
        else:
            print(f"Your selection of {recipe[selection]['drink']} is not available due to a lack of resources")
    elif selection == 2:
        if recipe[selection]["water"] >= 250 and recipe[selection]["milk"] >= 100 and recipe[selection]["coffee"] >= 24:
            print(f"Your selection of {recipe[selection]['drink']} is available")
        else:
            print(f"Your selection of {recipe[selection]['drink']} is not available due to a lack of resources")

def getCost(selection):
    print("Coffee Type:", recipe[selection]["drink"])
    print("Cost:", recipe[selection]["cost"])

def processCoins():
    global changeTendered  # Declare as global to modify its value
    quarters = int(input("Enter Quarters: "))
    dimes = int(input("Enter Dimes: "))
    nickles = int(input("Enter Nickles: "))
    pennys = int(input("Enter Pennys: "))
    changeTendered = float((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + pennys)

def processPayment(selection, changeTendered):
    global exitLoop  # Declare as global to modify its value
    cost = recipe[selection]["cost"]
    change = changeTendered - cost
    if change >= 0:
        print("Payment successful!")
        print(f"Change: {change}")
        create = True
    elif change < 0:
        print("Payment incomplete")
        print(f"Remaining balance: {change}")
        cost = change
        processCoins()
        processPayment(selection, changeTendered)
    else:
        print("A payment error has occurred")
        exitLoop = True
    
def makeCoffee(create, selection):
    global exitLoop  # Declare as global to modify its value
    if create:
        print(f"Please take your {recipe[selection]['drink']}")
    else:
        print("Something went wrong, here is your change back")
    exitLoop = True  # Add this line to modify the global exitLoop variable

while True:
    print(logo)
    try:
        order(water, milk, coffee)
        checkResources(selection)
        getCost(selection)
        processCoins(selection, changeTendered)
        makeCoffee(create, selection)

        if exitLoop:
            break  # exit the while opTwo loop

    except ValueError as e:
            print(f"Error: {e} try again")
            continue

    user_choice = input("Do you want to order again? (yes/no): ").lower()
    if user_choice == 'yes':
        break

