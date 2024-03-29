class CSVFileManage:
    @staticmethod
    def readFile():
        with open("CSV/weather_data.csv", "r") as data_file:
            data = data_file.read()
            print(data)
    
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
        choice = int(input("\nEnter 1 to Read file, 2 to Append file, 3 to Write file, or 4 to exit: "))
        if choice == 1:
            CSVFileManage.readFile()
        elif choice == 2:        
            CSVFileManage.appendFile()
            CSVFileManage.readFile()  # Call readFile again to display the updated content
        elif choice == 3:
            CSVFileManage.writeFile()
            CSVFileManage.readFile()  # Call readFile again to display the content after writing
        elif choice == 4:
            break
        else:
            print("Invalid input. try again")
