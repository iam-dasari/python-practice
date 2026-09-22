# OOP - Object Oriented Programming
# Example of a class and object in Python
# Create a design for Person - Class (Blue print) and Object (Real Person)
# To create a real person we need to create an object of the class Person
# self is a reference to the current instance of the class and is used 
# to access variables that belong to the class. 
# self is always the first parameter of any method in the class.
# self stores the instance of the class and is used to access the attributes and methods of the class.
# __init__ is a special method that is called when an object is created. (Constructor)
# It is used to initialize the object's attributes.
# default constructor is a constructor that takes no arguments. 
# It is used to create an object of the class without any initial values.
# Parameterized constructor is a constructor that takes arguments. 
# It is used to create an object of the class with initial values.
# When we create an object of the class with parameters, 
# the __init__ method is called with the parameters passed to it.
# And default constructor is automatically called when we create an object of the class with any parameters.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an object of the Person class
person1 = Person("Alice", 30)
print(person1.introduce())