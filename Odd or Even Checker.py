def check(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print("Welcome To Duncan's Odd or Even checker")
try:
    number = int(input("Enter a number: "))
except ValueError as e:
    print(f"Error {e}")
    
result = check(number)

print(f"The number {number} is {result}.")
