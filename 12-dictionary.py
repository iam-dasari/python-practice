# Dictionary in Python - key-value pairs, mutable, unordered
# Example: { "name": "Coders"}, key is the name and value is Coders

dic1 = {
    "name": "Coders",
    "age": 20,
    "city": "Hyderabad"
}

print(dic1.keys())
print(dic1.values())
print(dic1.items())

print(dic1)
print(dic1["name"])

dic1["name"] = "Pavan"
print(dic1)

dic1["phno"] = 12345
print(dic1)

dic1.pop("name")
print(dic1)

dic1.popitem()
print(dic1)

dic1.clear()
print(dic1)