# List comprehension is a short way to create a list
# It uses one line instead of loop
# It makes code short and easy to read
# we can also add conditions inside it

nums = []

for i in range(1, 6):
    nums.append(i)

print(nums)

nums = [i for i in range(1, 11)]
print(nums)

nums = []

for i in range(1, 16):
    if i % 2 == 0:
        nums.append(i)

print(nums)

nums = [i for i in range(1, 21) if i % 2 == 0]
print(nums)