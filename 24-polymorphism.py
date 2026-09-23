# Polymorphism in Python
# Polymorphism allows us to define methods in the child class with the same name as defined in their
# parent class. It allows us to perform a single action in different ways.

class Developer:
    def work(self):
        print("Developer is coding")

class Tester:
    def work(self):
        print("Tester is testing")

