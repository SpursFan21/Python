print("Welcome to Duncan's BMI calculator!")

try:
    height = float(input("Enter your Height in Meters: "))
    weight = float(input("Enter your Weight in Kg: "))
except ValueError:
    print("Invalid input. Please enter numeric values for height and weight.")
    exit()
try:
    BMI = weight / (height ** 2)
    rounded_BMI = round(BMI, 3)
    print("Your BMI is: ", rounded_BMI)
except ZeroDivisionError:
    print("Error: Height should be greater than zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
