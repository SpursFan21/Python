class Animal:
    def speak(self):
        return "Animal Speaks"

class Dog(Animal):
    def barks(self):
        return "Dog Barks"
    
class Bulldog(Dog):
    def attack(self):
        return "Bulldog attacks!"
    
if __name__ == "__main__":
    
    animal = Animal()
    dog = Dog()
    bulldog = Bulldog()
    
    print(animal.speak())
    print(dog.speak())
    print(dog.barks())
    print(bulldog.speak())
    print(bulldog.barks())
    print(bulldog.attack())
    