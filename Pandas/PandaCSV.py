import pandas

class CSVFileManager:
    def read():
        data = pandas.read_csv("./CSV/weather_data.csv")
        print(data)
    
    def getColumn():# this is how easy it is to get just get one column extracted from csv with pandas
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
    
    def average():
        data = pandas.read_csv("./CSV/weather_data.csv")
        print(data["temp"].mean())
        
    def maxValRow():
        data = pandas.read_csv("./CSV/weather_data.csv")
        print(data[data.temp == (data.temp.max())])# this finds the max temp and then prints the row it is in
        
    def getRow():
        data = pandas.read_csv("./CSV/weather_data.csv")
        print("\n")
        print(data[data.day == "Tuesday"])#this method allows me to pull the data from a single row
    
    def getElementForRow():
         data = pandas.read_csv("./CSV/weather_data.csv")
         monday = data[data.day == "Monday"]# this allows me to find a specific data element for a row
         print("\nOn Monday it will be ", monday.condition)
         
    def getDayTempConvertToCelsius():
        data = pandas.read_csv("./CSV/weather_data.csv")
        monday = data[data.day == "Monday"]
        monday_temp = monday.temp[0]# this gets the temp for the monday row
        monday_temp_fahrenheit = ((monday_temp * 9) / 5) + 32 #celsius to fahrenheit conversion
        print("\n The temp on monday will be ", monday_temp, " degrees in Celsius\n and in Fahrenheit it will be ", monday_temp_fahrenheit, " degrees")
    
if __name__ == "__main__":
    while True:
        choice = int(input("\nEnter 1 to read, 2 to view temp column, 3 to check data type, 4 to convert the data to a dictionary, 5 to convert data column to list,\n 6 to find the average of the list, 7 to find the maximum value of list, 8 to view an induvidual row, 9 to get element for row, 10 to convert monday temp to fahrenhiet, and 11 to exit: "))
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
            CSVFileManager.maxValRow()
        elif choice == 8:
            CSVFileManager.getRow()
        elif choice == 9:
            CSVFileManager.getElementForRow()
        elif choice == 10:
            CSVFileManager.getDayTempConvertToCelsius()
        elif choice == 11:
            print("program shutting down.......")
            break
        else:
            print("Invalid input try again!")