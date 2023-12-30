import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

while True:
    print("Welcome to Duncan's Rock, Paper, Scissors game")

    try:
        # Get user's choice
        user_choice = int(input("Enter your choice! 0 for Rock, 1 for Paper, or 2 for Scissors: "))
        if user_choice not in [0, 1, 2]:
            raise ValueError("Invalid input! Please enter 0, 1, or 2.")
        
        user_hand = choices[user_choice]
        print(f"\nYou picked:\n{user_hand}")

        # Get computer's choice
        computer_choice = random.choice(choices)
        print(f"\nComputer picked:\n{computer_choice}")

        # Determine the winner
        if user_choice == 0 and computer_choice == paper:
            result = "Computer wins!"
        elif user_choice == 1 and computer_choice == scissors:
            result = "Computer wins!"
        elif user_choice == 2 and computer_choice == rock:
            result = "Computer wins!"
        elif user_choice == 0 and computer_choice == scissors:
            result = "You win!"
        elif user_choice == 1 and computer_choice == rock:
            result = "You win!"
        elif user_choice == 2 and computer_choice == paper:
            result = "You win!"
        else:
            result = "It's a stalemate!"

        print(f"\n{result}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    except ValueError as ve:
        print(f"Error: {ve}")
