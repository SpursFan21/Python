import datetime

class Function:
    
    def dateTime():
        now = datetime.datetime.now()
        print("Current date and time: ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        
if __name__ == "__main__":
    Function.dateTime()