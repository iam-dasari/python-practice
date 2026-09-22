#Lists  -Ordered and changeable collection using []
#List Operations - change, append, remove, pop, clear

numbers=[1,2,3,4,5,6]

for i, number in enumerate(numbers):
    print(f"numbers[{i}] = {number} where i= {i}")

numbers[0] = 100
print(numbers)

numbers.append(7)
numbers.append(8)
print(numbers)

numbers.remove(2)
print(numbers)

numbers.pop(1)
print(numbers)

numbers.pop() #Last element will be popped up
print(numbers)

numbers.clear()
print(numbers)