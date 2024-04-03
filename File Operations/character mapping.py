# Create the dictionary mapping characters to text
char_to_text = {"0": "zero", "1" : "one", "2" : "two", "3" : "three", "4" : "four", "5" : "five", "6" : "six", "7" : "seven", "8" : "eight", "9" : "nine"}

#input from user
user_input = input("Enter a string: ")

#convert user input to text using dictionary
convert_text = ""
for char in user_input:
    if char.isdigit():
        #the condition checks if the curret character char is a digit using the isdigit() method.
        #if it is a digit, it looks up the corresponding textual representaion from the char _to_text dictionary usiing the get() method
        # and append it to the converted_text string, followed by a space
        convert_text += char_to_text.get(char) + " "
    else:
        convert_text +=char + " "
        
print(f"The converted input {user_input} is {convert_text}")
    