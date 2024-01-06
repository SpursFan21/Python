import random

logo  = """ 
 ______     __  __     ______     ______     ______     __     __   __     ______        __  __        ______     ______     __    __     ______    
/\  ___\   /\ \/\ \   /\  ___\   /\  ___\   /\  ___\   /\ \   /\ "-.\ \   /\  ___\      /\_\_\_\      /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   
\ \ \__ \  \ \ \_\ \  \ \  __\   \ \___  \  \ \___  \  \ \ \  \ \ \-.  \  \ \ \__ \     \/_/\_\/_     \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\   
 \ \_____\  \ \_____\  \ \_____\  \/\_____\  \/\_____\  \ \_\  \ \_\ \"\_\  \ \_____\      /\_\/\_\     \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\ 
  \/_____/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/   \/_/ \/_/   \/_____/      \/_/\/_/      \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/

"""

def num():
    wNum = random.randint(1, 100)
    return wNum
    
while True:
    guessCount = 6
    print(logo)
    won = False
    wNum = num()
    try:
        while guessCount > 0:
            currentGuess = int(input("Guess the number between 1 and 100: "))
            if currentGuess == wNum:
                print("You got it!")
                won = True
                break
            elif currentGuess > wNum:
                print(f"The number is less than {currentGuess}")
                guessCount -= 1
                print(f"{guessCount} remaning guesses")
            else:
                print(f"The number is greater than {currentGuess}")
                guessCount -= 1
                print(f"{guessCount} remaning guesses")

        if not won:
            print("You lose!")


    except ValueError as e:
        print(f"Error: {e} try again")
        continue

    user_choice = input("Do you want to play again? (yes/no): ").lower()
    if user_choice != 'yes':
        break
