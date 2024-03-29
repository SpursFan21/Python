import csv

class CSVFileManage:
    @staticmethod
    def readFile():
        with open("CSV/weather_data.csv", "r") as data_file:
            data = data_file.read()
            print(data)
            
    @staticmethod
    def csvReader():
        with open("CSV/weather_data.csv") as data_file:
            data = csv.reader(data_file)
            for row in data:
                print(row)
    
    @staticmethod
    def csvTemp():
        with open("CSV/weather_data.csv") as data_file:
            data = csv.reader(data_file)
            temperatures = []#this is a new list to hold the temps i will extract from the CSV file
            for row in data:
                if row[1] != "temp": #this allows me to only display on data element from all the rows
                    temperatures.append(int(row[1]))
            print(temperatures)
    
    @staticmethod
    def appendFile():
        userInput = input("\nEnter your input to append to file: ")
        with open("CSV/weather_data.csv", "a") as data_file:
            data_file.write("\n" + userInput)
    
    @staticmethod
    def writeFile():
        userInput = input("\nEnter your input to write to file: ")
        with open("CSV/weather_data.csv", "w") as data_file:
            data_file.write(userInput)

if __name__ == "__main__":
    while True:
        choice = int(input("\nEnter 1 to Read file, 2 to read file as formated data, 3 to read tempatures as int,\n 4 to Append file, 5 to Write file, or 6 to exit: "))
        if choice == 1:
            CSVFileManage.readFile()
        elif choice == 2:
            CSVFileManage.csvReader()
        elif choice == 3:
            CSVFileManage.csvTemp()
        elif choice == 4:        
            CSVFileManage.appendFile()
            CSVFileManage.readFile()
        elif choice == 5:
            CSVFileManage.writeFile()
            CSVFileManage.readFile()
        elif choice == 6:
            break
        else:
            print("Invalid input. try again")
