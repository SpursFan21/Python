import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
deck = {"Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" : 7, "Eight" : 8, "Nine" : 9, "Ten" : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : 11, }
def drawCard(deck):
    card = random.choice(list(deck.items()))
    return card

def userPlay(userCards):
    userCards.append(drawCard(deck))
    userCards.append(drawCard(deck))
    values = [card[1] for card in userCards]
    score = sum(values)
    print(f"Your total is {score}")

def computerPlay(computerCards):
    computerCards.append(drawCard(deck))
    computerCards.append(drawCard(deck))
    values = [card[1] for card in computerCards]
    score = sum(values)
    print(f"Dealer score is {score}")

def calculateWinner(userCards, computerCards):
    if userCards <= 21 and computerCards >= 21:
        print("You win!")
    elif userCards > 21 and computerCards <= 21:
        print("Dealer wins!")
    elif userCards == computerCards:
        print("It's a tie")
    else:
        print("calculation error")


while True:
    userCards = []
    computerCards = []
    
    print(logo)
    print("Welcome to Duncan's Python Black Jack!")
    userPlay(userCards)

    score = sum([card[1] for card in userCards])
    while score < 21:
        try:
            hit = str(input("Would you like to Hit or Stay? ")).lower()
        except ValueError as e:
            print(f"Invalid input: {e} try again: ")
            continue

        if hit == "hit":
            userCards.append(drawCard(deck))
            score = sum([card[1] for card in userCards])
            print(f"Your score is {score}")
        else:
            break

    print(f"You are holding at {score}")

    if score > 21:
        print("You busted, dealer wins")

    computerPlay(computerCards)

    while sum([card[1] for card in computerCards]) <= 17:
        computerCards.append(drawCard(deck))

    computerScore = sum([card[1] for card in computerCards])
    print(f"Dealer scored a {computerScore}")

    calculateWinner(userCards, computerCards)

    user_choice = input("Do you want to play again? (yes/no): ").lower()
    if user_choice != 'yes':
        break