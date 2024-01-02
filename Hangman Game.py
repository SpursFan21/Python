import random

def choose_word():
    # Function to choose a random word from a predefined list
    words = ["berry", "cheese", "ball", "tree", "quartermaster", "computer", "sword", "scientist", "nerd", "skunk", "lion", "battleship", "spaceship", "hotdogs", "hamburger", "pizza"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Function to display the word with underscores for unguessed letters
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display


def hangman():
    while True:
        # Start a new game
        print("Welcome to Duncan's Hangman Game!")
        word_to_guess = choose_word()
        max_attempts = 6
        guessed_letters = []
        attempts = 0

        print(display_word(word_to_guess, guessed_letters))

        while '_' in display_word(word_to_guess, guessed_letters) and attempts < max_attempts:
            # Main game loop
            guess = input("Guess a letter: ").lower()

            try:
                if len(guess) == 1 and guess.isalpha():
                    # Check if the input is a valid single letter
                    if guess in guessed_letters:
                        print("You already guessed that letter.")
                    elif guess in word_to_guess:
                        # If the guessed letter is in the word, update guessed_letters
                        guessed_letters.append(guess)
                        print("Good guess!")
                    else:
                        # If the guessed letter is not in the word, increment attempts
                        attempts += 1
                        print(f"Wrong guess! Attempts left: {max_attempts - attempts}")
                else:
                    raise ValueError("Invalid input. Please enter a single letter.")
            except ValueError as e:
                print(e)

            print(display_word(word_to_guess, guessed_letters))

        # Display the game result
        if '_' not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word.")
        else:
            print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    # Run the Hangman game if the script is executed directly
    hangman()
