class Date:
    dates = [{"Year": 1999, "Month": 2, "Day": 20},
             {"Year": 2001, "Month": 7, "Day": 4},
             {"Year": 2005, "Month": 10, "Day": 30},
             {"Year": 2011, "Month": 5, "Day": 9},
             {"Year": 2020, "Month": 11, "Day": 27}]

    @staticmethod
    def calculate_date():
        date_one_index = int(input("Enter the index of the first date from the list(0-4): "))
        date_two_index = int(input("Enter the index of the second date from the list to find the amount of days between the two dates: "))

        date_one = Date.dates[date_one_index]
        date_two = Date.dates[date_two_index]

        # Calculating the difference between the dates
        from datetime import datetime
        date_one = datetime(year=date_one["Year"], month=date_one["Month"], day=date_one["Day"])
        date_two = datetime(year=date_two["Year"], month=date_two["Month"], day=date_two["Day"])
        delta = date_two - date_one

        # Extracting only the number of days from the timedelta object
        days_difference = delta.days
        print("Number of days between the two dates:", abs(days_difference))

if __name__ == "__main__":
    Date.calculate_date()
