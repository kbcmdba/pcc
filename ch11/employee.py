# Employee: Write a class called Employee. The __init__() method should take a
# first name, a last name, and an annual salary, and store each of these as
# attributes. Write a method called give_raise() that adds $5000 to the annual
# salary by default but also accepts a diferent raise amount.

class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        self.annual_salary += amount

