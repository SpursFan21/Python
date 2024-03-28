class Commands:
    @staticmethod
    def DisplayStudents(students):
        for student in students:
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Major:", student["major"])
            print()

    @staticmethod
    def DisplayAvgAge(students):
        totalAge = 0
        numStudents = len(students)

        for student in students:
            totalAge += student["age"]

        if numStudents > 0:
            avgAge = totalAge / numStudents
            print("Average age of students:", avgAge, "\n")
        else:
            print("No students in the list")
    
    @staticmethod
    def DisplayTotalStudents(students):
        totalStudents = len(students)
        print(f"The total number of students in the registry is: {totalStudents}\n")


class StudentRegistry:
    def __init__(self, students):
        self.students = students

    def DisplayStudents(self):
        Commands.DisplayStudents(self.students)


# List of Dictionaries
students = [
    {"name": "Alice", "age": 20, "major": "Computer Science"},
    {"name": "Bob", "age": 22, "major": "Engineering"},
    {"name": "Charlie", "age": 21, "major": "Mathematics"}
]

# Instance of StudentRegistry
registry = StudentRegistry(students)

if __name__ == "__main__":
    print("Welcome to Duncan's List of Dictionary Reader\n")
    while True:
        try:
            command = int(input("Enter 1 to view the Registry, Enter 2 to view average age of students, Enter 3 to view total number of enrolled students, or Enter 4 to exit: \n"))
            if command == 1:
                registry.DisplayStudents()
            elif command == 2:
                Commands.DisplayAvgAge(students)
            elif command == 3:
                Commands.DisplayTotalStudents(students)
            elif command == 4:
                print("Exiting the program...")
                break
            else:
                print("Incorrect Command Value, Try Again")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
