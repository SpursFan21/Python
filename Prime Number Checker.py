import math # Used for round up 

while True:
    print("Welcome to Duncan's Prime Number Checker!")

    try:
        num = int(input("Enter a number to see if its prime: "))
    except ValueError as e:
        print(f"Invalid input: {e}")
        continue  # Restart the loop if there's an invalid input

    def Check(num):
        if num <= 0:
            return False
        for i in range(2, int(num** .5) + 1):
            if num % i == 0:
                return False
        return True
    
    if Check(num):
        print(f"{num} is prime!")
    else:
        print(f"{num} is not prime.")

    user_choice = input("Do you want to check another number ? (yes/no): ").lower()
    if user_choice != 'yes':
        break