#parent class
class Person(object):
    #init/ constructor
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    
    def display(self):
        print(self.name)
        print(self.id_number)
    
    def details(self):
        print(f"My name is: {(self.name)}")
        print(f"ID number is: {(self.id_number)}")
    
#child class
class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post
        
        #invoking the init of the parent class
        Person.__init__(self, name, id_number)
        
    def details(self):
        print(f"My name is: {(self.name)}")
        print(f"ID number is: {(self.id_number)}")
        print(f"Post: {(self.post)}")

#creation of a object variable or an instance
a = Employee("Duncan", 886012, 90000, "Intern")

#calling a function of the class Person using its instance
#launching a Main()
if __name__ == "__main__":
    a.display()
    a.details() 