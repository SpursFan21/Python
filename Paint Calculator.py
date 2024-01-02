import math # Used for round up 

while True:
    print("Welcome to Duncan's Paint Calculator!")

    try:
        height = int(input("Enter the height of the area you need to paint: "))
        width = int(input("Enter the width of the area you need to paint: "))
        coverage = int(input("Enter the coverage area one can of paint will get you: "))
    except ValueError as e:
        print(f"Invalid input: {e}")
        continue  # Restart the loop if there's an invalid input

    def Calculator(height, width, coverage):
        cans = height * width / coverage
        rCans = math.ceil(cans)
        print(f"You need {rCans} cans of paint to paint your area")

    Calculator(height, width, coverage)

    user_choice = input("Do you want to calculate again? (yes/no): ").lower()
    if user_choice != 'yes':
        break
