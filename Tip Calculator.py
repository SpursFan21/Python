print("Welcome to Duncan's Tip Calculator\n")

while True:
    try:
        numPeopleInParty = int(input("Enter total number of people in your party that will be splitting the bill: "))
        break
    except ValueError:
        print("Please enter a valid integer for the number of people. Try again.")

while True:
    try:
        billTotal = float(input("Enter Bill total: "))
        break
    except ValueError:
        print("Please enter a valid number for the bill total. Try again.")

totalPerPerson = billTotal / numPeopleInParty
print(f"The total per person before tipping is {totalPerPerson:.2f}")

while True:
    try:
        tipPercent = float(input("Enter the tip percent for the party members: "))
        break
    except ValueError:
        print("Please enter a valid number for the tip percent. Try again.")

tipMultiplier = 1 + (tipPercent / 100)
totalPerPersonWithTip = totalPerPerson * tipMultiplier

print(f"The total each person will pay is {totalPerPersonWithTip:.2f}")


