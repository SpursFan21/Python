class Vehicle:
    def type(self):
        return "Vehicle"
    
    def fuelEfficiency(self):
        pass
    
class Car(Vehicle):
    def type(self):
        return "Car"
    
    def fuelEfficiency(self):
        return 20

class Bike(Vehicle):
    def type(self):
        return "Bike"
    
    def fuelEfficiency(self):
        return 90

class Truck(Vehicle):
    def type(self):
        return "Truck"
    
    def fuelEfficiency(self):
        return 12
    
if __name__ == "__main__":
    while True:
        print("Choose a vehicle to see details:")
        print("1. Vehicle")
        print("2. Car")
        print("3. Bike")
        print("4. Truck")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle = Vehicle()
            print("Type:", vehicle.type())
            print("Fuel Efficiency:", vehicle.fuelEfficiency())
        elif choice == "2":
            car = Car()
            print("Type:", car.type())
            print("Fuel Efficiency:", car.fuelEfficiency())
        elif choice == "3":
            bike = Bike()
            print("Type:", bike.type())
            print("Fuel Efficiency:", bike.fuelEfficiency())
        elif choice == "4":
            truck = Truck()
            print("Type:", truck.type())
            print("Fuel Efficiency:", truck.fuelEfficiency())
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

