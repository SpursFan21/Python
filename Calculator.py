while True:
    print("Welcome to Duncan's Calculator!")
    try:
        firstNumber = float(input("Enter your number: "))
        command = str(input("Enter your command\n add, subtract, multiply, divide: ")).lower()
        secondNumber = float(input(f"Enter the number you want to {command} : "))
    except ValueError as e:
        print(f"Invalid input: {e}")
        continue  # Restart the loop if there's an invalid input
    
    result = 0
    
    def Add(firstNumber, secondNumber):
        return firstNumber + secondNumber
    
    def Subtract(firstNumber, secondNumber):
        return firstNumber - secondNumber
    
    def Multiply(firstNumber, secondNumber):
        return firstNumber * secondNumber
    
    def Divide(firstNumber, secondNumber):
        return firstNumber / secondNumber
    
    if command == "add":
        result = Add(firstNumber, secondNumber)
    elif command == "subtract":
        result = Subtract(firstNumber, secondNumber)
    elif command == "multiply":
        result = Multiply(firstNumber, secondNumber)
    elif command == "divide":
        result = Divide(firstNumber, secondNumber)
    else:
        print("You made an input error. Please try again.")
        continue  # Restart the loop if there's an invalid input
    
    print(f"Result: {result}")
    
    user_choice = input("Do you want to calculate again? (yes/no): ").lower()
    if user_choice != 'yes':
        break
