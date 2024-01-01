import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Duncan's Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

randomLetters = ''.join(random.choice(letters) for _ in range(nr_letters))
randomSymbols = ''.join(random.choice(symbols) for _ in range(nr_symbols))
randomNumbers = ''.join(random.choice(numbers) for _ in range(nr_numbers))

# Combine the generated strings
password = randomLetters + randomSymbols + randomNumbers

# Shuffle the characters in the password randomly
password_list = list(password)
random.shuffle(password_list)
shuffled_password = ''.join(password_list)

print(f"Your password is {shuffled_password}")
