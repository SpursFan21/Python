class Company:
    def __init__(self, operating_capital, total_employees):
        self.operating_capital = operating_capital
        self.total_employees = total_employees
    
company = Company(1000000, 10)

print(company.operating_capital)
print(company.total_employees)