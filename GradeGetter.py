def getGrade(average):
    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"
    print(f"Your average grade is a {average}% {letter}")
    
def averages():
    attendance = float(input("Enter attendance grade: "))
    assignment = float(input("Enter assignment grade: "))
    midterm = float(input("Enter midterm grade: "))
    final = float(input("Enter Final grade: "))
    wAttendance = attendance * 1.01
    wAssignment = assignment * 1.03
    wMidterm = midterm * 1.03
    wFinal =  final * 1.03
    average = (wAttendance + wAssignment + wMidterm + wFinal) / 4
    return average

if __name__ == "__main__":
    average = averages()
    getGrade(average)