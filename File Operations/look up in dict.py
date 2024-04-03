#define the jupiter text conversion dictionary
jupiter_dictionary = {
    "LOL" : "Laughing Out Loud",
    "BRB" : "Be Right Back",
    "IDK" : "I Dont Know"
}

#get user input
user_input = input("Enter a keyword: ")

#convert user input using jupiter dictionary
if user_input in jupiter_dictionary:
    converted_text = jupiter_dictionary[user_input]
    print(f"Converted text {converted_text}")
else:
    print("Keyword not found")