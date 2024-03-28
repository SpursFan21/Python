import datetime

class Function:
    
    def dateTime():
        now = datetime.datetime.now()
        print("Current date and time: ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        
    def yesterdaysDate():
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        print("Yesterday's date: ", yesterday)
        
    def tomorrowsDate():
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        print("Tomorrow's date: ", tomorrow)

if __name__ == "__main__":
    Function.dateTime()
    Function.yesterdaysDate()
    Function.tomorrowsDate()
