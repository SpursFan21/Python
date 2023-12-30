import random
print("Welcome to Duncan's random lunch picker, that will choose a random member from your group to pay ")
names_string = input("Enter names separated by comma: ")
names = names_string.split(", ")
pick = random.choice(names)
print(f"{pick} is going to buy lunch today")