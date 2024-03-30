import pandas

class CSVFileManger:
    def read():
        data = pandas.read_csv("./CSV/weather_data.csv")
        print(data)
    
    def getColumn():# this is how easy it is to get just get one row extracted from csv with pandas
        data = pandas.read_csv("./CSV/weather_data.csv")
        print(data["temp"])
    
    def checkDataType():
        data = pandas.read_csv("./CSV/weather_data.csv")
        print("\n")
        print(type(data))#check the data type 
        print("\n")
        
if __name__ == "__main__":
    while True:
        choice = int(input("Enter 1 to read, 2 to view temp column, 3 to check data type and 4 to exit: "))
        if choice == 1:
            CSVFileManger.read()
        elif choice == 2:
            CSVFileManger.getColumn()
        elif choice == 3:
            CSVFileManger.checkDataType()
        elif choice == 4:
            print("program shutting down.......")
            break
        else:
            print("Invalid input try again!")