class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def speak(self):
        return f"{self.species} speaks: {self.sound}"

# Creating an instance of Animal with specific attributes
my_animal = Animal("Dog", "Woof")
print(my_animal.speak())  # Output: "Dog speaks: Woof"
