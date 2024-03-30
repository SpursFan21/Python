import pandas

class CSVFileManager:
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
        
    def convertDataToDictionary():
        data = pandas.read_csv("./CSV/weather_data.csv")
        data_dict = data.to_dict()#Converts dataframe to dictionary
        print("\n")
        print(data_dict)
        
    def convertDataToList():
        data = pandas.read_csv("./CSV/weather_data.csv")
        data_list = data["temp"].to_list()#Converts data column to List
        print("\n")
        print(data_list)
        print("\n")
    
    @staticmethod    
    def average():
        data = pandas.read_csv("./CSV/weather_data.csv")
        print(data["temp"].mean())
    
if __name__ == "__main__":
    while True:
        choice = int(input("Enter 1 to read, 2 to view temp column, 3 to check data type, 4 to convert the data to a dictionary,\n 5 to convert data column to list, 6 to find the average of the list, and 7 to exit: "))
        if choice == 1:
            CSVFileManager.read()
        elif choice == 2:
            CSVFileManager.getColumn()
        elif choice == 3:
            CSVFileManager.checkDataType()
        elif choice == 4:
            CSVFileManager.convertDataToDictionary()
        elif choice == 5:
            CSVFileManager.convertDataToList()
        elif choice == 6:        
            CSVFileManager.average()
        elif choice == 7:
            print("program shutting down.......")
            break
        else:
            print("Invalid input try again!")