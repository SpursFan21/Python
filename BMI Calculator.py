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
if rounded_BMI < 18.5:
    print("You are under weight")
elif rounded_BMI < 25:
    print("You have a normal weight")
elif rounded_BMI < 30:
    print("You are slightly overweight")
elif rounded_BMI < 35:
    print("You are are obese")
else:
    print("You are clinicaly obese")