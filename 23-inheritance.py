# Inheritance in Python
# Inheritance allows us to define a class that inherits all the methods and properties from another class

class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def code(self):
        print("Developer is coding")

class Tester(Developer):
    def test(self):
        print("Tester is testing")

# Creating objects of the classes
employee = Employee()
developer = Developer()
developer.code()
developer.work()
tester = Tester()