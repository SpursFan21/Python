while True:
    print("Welcome to Duncan's Ceaser Cypher Program!")
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    try:
        direction = str(input("Enter (encrypt or decrypt): ")).lower()
        text = str(input("Enter your text: ")).lower()
        shift = int(input("Enter a shift for the cypher(1-25): "))
    except ValueError as e:
        print(f"Invalid input: {e}")
        continue  # Restart the loop if there's an invalid input

    def ceaser(startText, shiftAmount, cypherDirection):
        endText = ""
        for letter in startText:
            position = alphabet.index(letter)
            if cypherDirection == "decrypt":
                shiftAmount *= -1
            newPosition = position + shiftAmount
            endText += alphabet[newPosition]
        print(f"{cypherDirection}d text is: {endText}")

    ceaser(startText=text, shiftAmount=shift, cypherDirection=direction)

    user_choice = input("Do you want to encrypt or decrypt again? (yes/no): ").lower()
    if user_choice != 'yes':
        break