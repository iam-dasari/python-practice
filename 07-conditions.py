#Conditional Statements - if, elif, else for decision making
age = int(input("ENter age:: "))

if age>60:
    print("You are a senior citizen!")
elif age >=18:
    print("You are an adult!")
elif age<1:
    print("You are not yet born!")
else:
    print("You are a Child!")

