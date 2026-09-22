#Set in Python - Unordered collection, without duplicates using {}
#Set Operations - add, remove, discard, clear, union, intersection, difference

my_set = {10,20,30,10,20,30}
print(my_set)

my_set.add(50)
print(my_set)

my_set.remove(20) #If the key is not present then Python will throw KeyError
print(my_set)

my_set.discard(80) #If 80 is not present then python will not throw error
print(my_set)

my_set.clear()
print(my_set)

a = {1,2}
b = {2,3}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))