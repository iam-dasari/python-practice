# Exception Handling (try-except)
# Exception handling is used to handle runtime errors gracefully in Python.

try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result is:", result)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
