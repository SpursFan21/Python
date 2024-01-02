import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def choose_word():
    words = ["berry", "cheese", "ball", "tree", "quartermaster", "computer", "sword", "scientist", "nerd", "skunk", "lion", "battleship", "spaceship", "hotdogs", "hamburger", "pizza"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def displayStage(word, guessed_letters, incorrect_guesses, stages):
    display_stage = stages[::-1][incorrect_guesses].strip()

    for letter in word:
        if letter in guessed_letters:
            display_stage += letter
        else:
            display_stage += '_'

    return display_stage



def hangman():
    while True:
        print("Welcome to Duncan's Hangman Game!")
        word_to_guess = choose_word()
        max_attempts = 6
        guessed_letters = []
        attempts = 0

        while '_' in display_word(word_to_guess, guessed_letters) and attempts < max_attempts:
            print(display_word(word_to_guess, guessed_letters))
            print(displayStage(word_to_guess, guessed_letters, attempts, stages))

            guess = input("Guess a letter: ").lower()

            try:
                if len(guess) == 1 and guess.isalpha():
                    if guess in guessed_letters:
                        print("You already guessed that letter.")
                    elif guess in word_to_guess:
                        guessed_letters.append(guess)
                        print("Good guess!")
                    else:
                        attempts += 1
                        print(f"Wrong guess! Attempts left: {max_attempts - attempts}")
                else:
                    raise ValueError("Invalid input. Please enter a single letter.")
            except ValueError as e:
                print(e)

        if '_' not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word.")
        else:
            print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    hangman()
