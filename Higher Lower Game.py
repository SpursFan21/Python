import random
logo = """
 __    __   __    _______  __    __   _______ .______          __        ______   ____    __    ____  _______ .______      
|  |  |  | |  |  /  _____||  |  |  | |   ____||   _  \        |  |      /  __  \  \   \  /  \  /   / |   ____||   _  \     
|  |__|  | |  | |  |  __  |  |__|  | |  |__   |  |_)  |       |  |     |  |  |  |  \   \/    \/   /  |  |__   |  |_)  |    
|   __   | |  | |  | |_ | |   __   | |   __|  |      /        |  |     |  |  |  |   \            /   |   __|  |      /     
|  |  |  | |  | |  |__| | |  |  |  | |  |____ |  |\  \----.   |  `----.|  `--'  |    \    /\    /    |  |____ |  |\  \----.
|__|  |__| |__|  \______| |__|  |__| |_______|| _| `._____|   |_______| \______/      \__/  \__/     |_______|| _| `._____|

"""
data = [
    {
        "title": "Avatar",
        "boxOffice": 2799439100,
        "year": 2019
    },
    {
        "title": "Titanic",
        "boxOffice": 2264743305,
        "year": 1997
    },
    {
        "title": "Barbie",
        "boxOffice": 1441828022,
        "year": 2023
    },
    {
        "title": "Frozen II",
        "boxOffice": 1453683476,
        "year": 2019
    },
    {
        "title": "Aquaman",
        "boxOffice": 1152028393,
        "year": 2018
    },
    {
        "title": "Black Panther",
        "boxOffice": 1349926083,
        "year": 2018
    },
    ]

opOne = 0
opTwo = 1
victory = True
score = 0
winner = ""
answer = ""
box_office_op_one = ""
box_office_op_two = ""
opAnswer = 0
ansIncrement = 0

def option1(opOne):
    print("First Movie:")
    print("Title:", data[opOne]["title"])
    print("Year:", data[opOne]["year"])

def option2(opTwo):
    print("Second Movie:")
    print("Title:", data[opTwo]["title"])
    print("Year:", data[opTwo]["year"])

def answer1(opOne):
    print("First Movie:")
    print("Title:", data[opOne]["title"])
    print("Box Office:", data[opOne]["boxOffice"])
    print("Year:", data[opOne]["year"])

def answer2(opTwo):
    print("Second Movie:")
    print("Title:", data[opTwo]["title"])
    print("Box Office:", data[opTwo]["boxOffice"])
    print("Year:", data[opTwo]["year"])

def increment(opOne, opTwo, ansIncrement):
    opOne += 1
    opTwo += 1
    ansIncrement += 1
    return opOne, opTwo, ansIncrement

def displayOps(opOne, opTwo):
    print("Which movie do you think had higher box office sales?\n")
    option1(opOne)
    print("\n")
    option2(opTwo)
    print("\n")

def takeAnswer(ansIncrement):
    answer = int(input("Enter 1 for first movie and 2 for second movie: "))
    answer += ansIncrement
    return answer

def getWinner(opOne, opTwo):
    box_office_op_one = data[opOne]["boxOffice"]
    box_office_op_two = data[opTwo]["boxOffice"]

    if box_office_op_one > box_office_op_two:
        winner = opOne
    else:
        winner = opTwo

    return winner, box_office_op_one, box_office_op_two

def calcAnswer(answer, winner, victory, score):
    if answer == (winner + 1):
        victory = True
        score += 1
        print("You guessed correct! It was movie A")
    else:
        victory = False
        print("You guessed incorrect, better luck next time!")

    return victory, score, not victory  # indicate that the loop should continue if the answer is incorrect



def displayAns(winner):
    print(f"\n{winner} had the higher box office\n")
    answer1(opOne)
    print("\n")
    answer2(opTwo)
    print("\n")

while True:
    print(logo)
    while opTwo < 6:
        try:
            displayOps(opOne, opTwo)
            answer = takeAnswer(ansIncrement)
            winner, _, _ = getWinner(opOne, opTwo)
            displayAns(data[winner]["title"])
            victory, score, exit_loop = calcAnswer(answer, winner, victory, score)
            print(f"Your score is {score}")
            opOne, opTwo, ansIncrement = increment(opOne, opTwo, ansIncrement)

            if exit_loop:
                break  # exit the while opTwo loop

        except ValueError as e:
            print(f"Error: {e} try again")
            continue

    user_choice = input("Do you want to play again? (yes/no): ").lower()
    if user_choice == 'yes':
        opOne = 0 # reset variables if user wants to play again
        opTwo = 1
        victory = True
        score = 0
        ansIncrement = 0 
        break
    # Check if the user answered all questions correctly
    if score == opTwo:
        print("Congratulations! You answered all questions correctly. You won the game!")
        break
