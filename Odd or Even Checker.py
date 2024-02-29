def check_odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print("Welcome To Duncan's Odd or Even checker")
try:
    number = int(input("Enter a number: "))
except ValueError as e:
    print(f"Error {e}")
    
result = check_odd_or_even(number)

print(f"The number {number} is {result}.")
