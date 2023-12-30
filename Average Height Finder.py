print("Welcome to Duncan's average height finder!")

# Get user input with exception handling
while True:
    heights_input = input("Enter a list of heights separated by spaces: ")
    try:
        # Convert heights to a list of integers
        heights_list = [int(height) for height in heights_input.split()]
        break  # Exit the loop if conversion is successful
    except ValueError:
        print("Invalid input. Please enter numeric values separated by spaces.")

# Initialize variables for total height and number of students
total_height = 0
num_students = 0

# Calculate total height and count the number of students
for height in heights_list:
    total_height += height
    num_students += 1

# Calculate average height
average_height = round(total_height / num_students)

# Print the results
print(f"Total height = {total_height}")
print(f"Number of students = {num_students}")
print(f"Average height = {average_height}")
