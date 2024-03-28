class Function:
    def simpleInterest():
        principle = float(input("What is the principle on your loan: "))
        interestRate = float(input("What is the interest rate on your loan: "))
        term = int(input("Enter the term of your loan in years: "))
        simpleInterest = principle * interestRate * term
        print(f"Your simple interest is {simpleInterest}")

    def compoundInterest():
        principle = float(input("What is the principle on your loan: "))
        interestRate = float(input("What is the interest rate on your loan: "))
        term = int(input("Enter the term of your loan in years: "))
        compoundInterest = principle * (1 + interestRate) ** term - principle
        print(f"Your compound interest is {compoundInterest:.2f}")


if __name__ == "__main__":
    Function.simpleInterest()
    Function.compoundInterest()
