class Dog:
    #class attribute
    attr1 = "mammal"

    #Instance attribute like a constructor
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("My name is {}".format(self.name))
        print(f"My name is {(self.name)}")
        
#Driver Code
#Objective instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

#Acessing the class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is a {}".format(Tommy.__class__.attr1))

#Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

#Accessing class attributes
Rodger.speak()
Tommy.speak()