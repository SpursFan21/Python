class Calculate:
    def getInfo(self):
        print("Welcome to Duncan's BMI calculator!")

        try:
            self.height = float(input("Enter your Height in Meters: "))
            self.weight = float(input("Enter your Weight in Kg: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for height and weight.")
            exit()

    def calc(self):
        try:
            BMI = self.weight / (self.height ** 2)
            self.rounded_BMI = round(BMI, 3)
            print("Your BMI is:", self.rounded_BMI)
        except ZeroDivisionError:
            print("Error: Height should be greater than zero.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def result(self):
        if self.rounded_BMI < 18.5:
            print("You are underweight")
        elif self.rounded_BMI < 25:
            print("You have a normal weight")
        elif self.rounded_BMI < 30:
            print("You are slightly overweight")
        elif self.rounded_BMI < 35:
            print("You are obese")
        else:
            print("You are clinically obese")

if __name__ == "__main__":
    while True:
        choice = input("enter 1 for BMI calculation or 2 to exit")
        #not finished stopped right here
        calc = Calculate()
        calc.getInfo()
        calc.calc()
        calc.result()
