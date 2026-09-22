# File Handling
# File handling is used to store data permanently in Files.
# open() is used to open a file
# "w" mode is used to write data
# "r" mode is used to read data
# "a" mode is used to add data to the file
# close() is used to close the file

""" file = open("data.txt", "w")
file.write("Hello Python")
file.close() """

""" file = open("data.txt", "r")
print(file.read())
file.close() """

""" file = open("data.txt", "a")
file.write("\n I am learning")
file.close() """

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes extra newlines

with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # Output: ['Line 1\n', 'Line 2\n']

with open("example.txt", "w") as file:
    file.write("This will overwrite everything.\n")

with open("example.txt", "a") as file:
    file.write("This line is safely added to the end.\n")

with open("data.txt", "r") as source, open("example.txt", "w") as dest:
    for line in source:
        dest.write(line)

try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: The requested file could not be found.")
except IOError:
    print("Error: An issue occurred while reading the file.")