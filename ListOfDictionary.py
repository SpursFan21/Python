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
    registry.DisplayStudents()
    Commands.DisplayAvgAge(students)
    Commands.DisplayTotalStudents(students)
