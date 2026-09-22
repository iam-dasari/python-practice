#Loops - for, while

for i in range(10):
    print(i)

#range(10) - 0,1,2,3,4,5,6,7,8,9

for i in range(1,11): # 1,2,3,4,5,6,7,8,9,10
    print(i)

for i in range(1,11,2): # 1, 1+2, 3+2 ...
    print(i)


i = 2
for i in range(10):
    if i == 2:  
        print(f"True when i = {i}")
        break #continue means leave when i=2 and then continue from 3
    else:
        print(f"False when i = {i}")

name = "Rohith"

for l in name:
    print(l, end=" ")

i = 1
while i<=5:
    print(i)
    i = i + 1