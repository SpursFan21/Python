class Function:
    
    @staticmethod
    def celsiusToFahreneit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahreneitToCelsius(fahreneit):
        return (fahreneit -32) * 5/9

class Calculate:
    
    def main():
        choice = input("Enter C to convert from Celsius to Fahreneit, or F to convert from Fahreneit to Celsius: ").upper()
        
        if choice == "C":
            celsius = float(input("Enter the temperture in Celsius: "))
            fahreneit = Function.celsiusToFahreneit(celsius)
            print(f"The temperature in Fahreneit is {fahreneit}")
        elif choice == "F":
            fahreneit = float(input("Enter the temperture in Fahreneit: "))
            celsius = Function.fahreneitToCelsius(fahreneit)
            print(f"The temperature in Celsius is {celsius}")
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    Calculate.main()