def main():
    
    # List of Dictionaries
    students = [
        {"name": "Alice", "age": 20, "major": "Computer Science"},
        {"name": "Bob", "age": 22, "major": "Engineering"},
        {"name": "Charlie", "age": 21, "major": "Mathematics"}
    ]

    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Major:", student["major"])
        print()


if __name__ == "__main__":
    print("Welcome to Duncan's List of Dictionary Reader\n")
    main()
