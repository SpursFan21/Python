line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]
treasure_map = [line1, line2, line3]

print("Hiding your treasure! Enter the position (e.g., A2):")
position = input().upper()  # Convert input to uppercase for case insensitivity
letter = position[0]
abc = ["A", "B", "C"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
treasure_map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")
