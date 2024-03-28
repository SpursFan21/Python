import math

class Calculator:
    @staticmethod
    def add(first, second):
        return first + second
    
    @staticmethod
    def subtract(first, second):
        return first - second
    
    @staticmethod
    def multiply(first, second):
        return first * second
    
    @staticmethod
    def divide(first, second):
        if second == 0:
            raise ValueError("Cannot divide by zero")
        return first / second
    
    @staticmethod
    def triangle_area(base, height):
        return (base * height) / 2
    
    @staticmethod
    def square_root(number):
        if number < 0:
            raise ValueError("Square root is not defined for negative numbers")
        return math.sqrt(number)
    
    @staticmethod
    def swap(first, second):
        return second, first

while True:
    print("Welcome to Duncan's Calculator!")
    try:
        command = input("Enter your command (add, subtract, multiply, divide, triangle, squared, swap): ").lower()
        if command == "triangle":
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            result = Calculator.triangle_area(base, height)
        elif command == "squared":
            number = float(input("Enter a number to find the square root: "))
            result = Calculator.square_root(number)
        elif command == "swap":
            first = float(input("Enter the first number: "))
            second = float(input("Enter the second number: "))
            result = Calculator.swap(first, second)
        else:
            first = float(input("Enter the first number: "))
            second = float(input("Enter the second number: "))
            if command == "add":
                result = Calculator.add(first, second)
            elif command == "subtract":
                result = Calculator.subtract(first, second)
            elif command == "multiply":
                result = Calculator.multiply(first, second)
            elif command == "divide":
                result = Calculator.divide(first, second)
    except ValueError as e:
        print(f"Invalid input: {e}")
        continue
    
    print(f"Result: {result}")
    
    user_choice = input("Do you want to calculate again? (yes/no): ").lower()
    if user_choice != 'yes':
        break
