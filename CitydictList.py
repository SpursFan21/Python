# Define a larger list of dictionaries
people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "David", "age": 40, "city": "Houston"},
    {"name": "Eva", "age": 28, "city": "Miami"}
]

# Function to display information from the list of dictionaries
def display_people(people_list):
    print("People Information:")
    for person in people_list:
        print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")

while True:
    # Display the list of dictionaries
    display_people(people)
    
    run_again = input("Do you want to run the program again? (yes/no): ")
    if run_again.lower() != 'yes':
        print("Exiting the program...")
        break
