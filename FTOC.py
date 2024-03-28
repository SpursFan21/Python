def FTOC(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = FTOC(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")
