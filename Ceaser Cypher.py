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

    def encrypt(plainText, shiftAmount):
        cypherText = ""
        for letter in plainText:
            position = alphabet.index(letter)
            newPosition = position + shiftAmount
            newLetter = alphabet[newPosition]
            cypherText += newLetter
        print(f"The encrypted text is: {cypherText}")

    def decrypt(encryptedText, shiftAmount):
        plainText = ""
        for letter in encryptedText:
            position = alphabet.index(letter)
            newPosition = position - shiftAmount
            plainText += alphabet[newPosition]
        print(f"The encrypted text is: {plainText}")

    if direction == "encrypt":
        encrypt(plainText = text, shiftAmount = shift)
    else:
        decrypt(encryptedText = text, shiftAmount = shift)
    

    user_choice = input("Do you want to encrypt or decrypt again? (yes/no): ").lower()
    if user_choice != 'yes':
        break