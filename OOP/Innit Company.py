class Company:
    def __init__(self, operating_capital, total_employees):
        """
        This is the constructor method (__init__) for the Company class.
        It initializes the object's attributes when a new Company object is created.
        
        Parameters:
        - operating_capital: The amount of capital the company has for its operations.
        - total_employees: The total number of employees working for the company.
        """
        self.operating_capital = operating_capital
        self.total_employees = total_employees

class TechCompany(Company):  # Inheriting from the Company class
    def __init__(self, operating_capital, total_employees, software_engineers, technologies):
        """
        This is the constructor method (__init__) for the TechCompany class.
        It initializes the object's attributes when a new TechCompany object is created.
        
        Parameters:
        - operating_capital: The amount of capital the company has for its operations.
        - total_employees: The total number of employees working for the company.
        - software_engineers: The number of software engineers employed by the tech company.
        - technologies: A list of technologies used by the tech company.
        """
        # Calling the parent class constructor to initialize common attributes
        super().__init__(operating_capital, total_employees)
        self.software_engineers = software_engineers
        self.technologies = technologies

# Creating an instance of the TechCompany class
tech_company = TechCompany(2000000, 50, 20, ["Python", "JavaScript", "Java"])

# Accessing and printing the attributes of the tech_company object
print("Operating Capital:", tech_company.operating_capital)
print("Total Employees:", tech_company.total_employees)
print("Software Engineers:", tech_company.software_engineers)
print("Technologies:", tech_company.technologies)


