# Exception Handling (try-except)
# Exception handling is used to handle runtime errors gracefully in Python.
# else block will be executed if there is no exception in the try block.
# finally block will always be executed, regardless of whether an exception occurred or not.

try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result is:", result)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
else:
    print("else: No exceptions occurred.")
finally:
    print("finally: will always be executed.")
