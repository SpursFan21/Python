import random

def coin_toss():
    # Generate a random number (0 or 1) to represent heads or tails
    result = random.randint(0, 1)

    # Map the random number to heads or tails
    if result == 0:
        return "Heads"
    else:
        return "Tails"

if __name__ == "__main__":
    # Call the coin_toss function and print the result
    outcome = coin_toss()
    print("The coin landed on:", outcome)
