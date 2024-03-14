class Function:
    def simpleInterest():
        principle = float(input("What is the principle on your loan"))
        intrestRate = float(input("What is the intrest rat on your loan"))
        term = int(input("Enter the term of your loan in years"))
        simpleInterest = principle * intrestRate * term
        print(f"Your simple intrest is {simpleInterest}")
        
    def compoundInterest():
        
        
if __name__ == "__main__":
    Function.simpleInterest()