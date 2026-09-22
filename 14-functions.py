#Function in Python - Other Types
# Default Arguments
# Keyword Arguments
# Multiple return values
# List as argument
# Lambda Function

# Default Arguments
def wish(name = "Student"): #Default argument and call as wish()
    print("Hello", name)

wish()

# Keyword Arguments
def info(name, age):
    print(name, age)

info(age = 20, name = "Rohith") #Keyword Arguments

# Multiple return values
def calc(a, b):
    return a + b, a - b

add, sub = calc(10, 20)
print(add)
print(sub)

list1 = [10, 20, 30]

def cal(numbers):
    print(sum(numbers))

cal(list1)

# Lambda Function
square = lambda x: x * x # Anonymous function
x = square(6) #Use variable name as function name
print(x)