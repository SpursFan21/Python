class Animal:
    def speak(self):
        return "Animal Speaks"
    
    def sound(self):
        return "Animal Makes Noise"

class Dog(Animal):
    def barks(self):
        return "Dog Barks"
    
    def sound(self):
        return "Dog Makes Noise"
    
class Bulldog(Dog):
    def attack(self):
        return "Bulldog attacks!"
    
    def sound(self):
        return super().sound()
    
if __name__ == "__main__":
    
    animal = Animal()
    dog = Dog()
    bulldog = Bulldog()
    
    print(animal.speak())
    print(animal.sound())
    print("\n")
    
    print(dog.speak())
    print(dog.barks())
    print(dog.sound())
    print("\n")
    
    print(bulldog.speak())
    print(bulldog.barks())
    print(bulldog.attack())
    print(bulldog.sound())
    