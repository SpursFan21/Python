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
    print("First Movie:")
    print("Title:", data[opTwo]["title"])
    print("Box Office:", data[opTwo]["boxOffice"])
    print("Year:", data[opTwo]["year"])

def increment(opOne, opTwo):
    opOne += 1
    opTwo += 1
    return opOne, opTwo

def displayOps():
    print("Which movie do you think had higher box office sales?\n")
    option1()
    print("\n")
    option2()

def getWinner(opOne, opTwo):
    if opOne > opTwo:
        winner = opOne
    else:
        winner = opTwo
    return winner

def displayAns(winner):
    print{f"{winner} had the higher box office\n"}
    answer1()
    print("\n")
    answer2()




