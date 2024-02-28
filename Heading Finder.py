import random

class Weather:
    @staticmethod
    def generate_random_wind_speed():
        windSpeed = random.randint(0, 50)
        return windSpeed
        

while True:
    print("Welcome to Duncan's first day back in python!")

    try:
        directionNS = input("Are you traveling North or South: ").lower()
        directionEW = input(f"Great your heading {directionNS}! Are you also heading East or West ?: ").lower()
    except ValueError as e:
        print(f"\nError {e} Try Again!\n ")
        continue

    windSpeed = Weather.generate_random_wind_speed()

    def Calculate(directionNS, directionEW, windSpeed):
        Heading = directionNS + " " + directionEW
        print(f"Your heading is {Heading} and the wind is {windSpeed} knots")

    Calculate(directionNS, directionEW, windSpeed)

    user_choice = input("Do you want to try again (yes/no): ").lower()
    if user_choice != 'yes':
        break
