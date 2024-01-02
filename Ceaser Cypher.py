while True:
    print("Welcome to Duncan's Ceaser Cypher Program!")
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    try:
        direction = str(input("Enter (encrypt or decrypt): ")).lower()
        text = str(input("Enter your message: ")).lower()
        shift = int(input("Enter a shift for the cypher: "))
    except ValueError as e:
        print(f"Invalid input: {e}")
        continue  # Restart the loop if there's an invalid input
    shift = shift % 26

    def ceaser(startText, shiftAmount, cypherDirection):
        endText = ""
        if cypherDirection == "decrypt":
            shiftAmount *= -1
        for char in startText:
            if char in alphabet:
                position = alphabet.index(char)
                newPosition = position + shiftAmount
                endText += alphabet[newPosition]
            else:
                endText += char
        print(f"{cypherDirection}d text is: {endText}")

            

    ceaser(startText=text, shiftAmount=shift, cypherDirection=direction)

    user_choice = input("Do you want to encrypt or decrypt again? (yes/no): ").lower()
    if user_choice != 'yes':
        break