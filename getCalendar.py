import calendar

class Calendar:
    
    def getCalendar():
        y = int(input("Input the year: "))
        m = int(input("Input the month: "))
        print(calendar.month(y, m))
        
if __name__ == "__main__":
    Calendar.getCalendar()
        