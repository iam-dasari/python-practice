# Encapsulation in Python
# Encapsulation is the process of binding data and functions 
# that operate on that data within a single unit.
# In Python, encapsulation is achieved by using private and public access modifiers.
# Private attributes and methods are denoted by a double underscore prefix (__).
# Public attributes and methods are accessible from outside the class.
# Encapsulation helps to protect the data from being accessed or modified directly from outside the class.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

# Creating an object of the BankAccount class
account = BankAccount("123456789", 1000)
print(account.get_balance())
