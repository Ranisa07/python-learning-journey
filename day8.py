# Introduction to Python Dictionary:
'''A Dictionary is a data structure that stores data in key-value pairs.
Example: data = {"name":"Rani","age":23}
- name,age --> Keys
- Rani,23 --> Values
=> values are accessed using keys(not index like lists)
'''
# Features:
'''=> Key must be unique
=> Keys must be immutable(string, numbers, tuples)
=> Values can be of any datatypes
=> Dictionary is ordered
=> Provide fast access using hashing'''

# Creating Dictionary(Multiple Methods):
# 1) Using {}
data = {"name": "Rani", "age":23}
print(data)

# 2) Using dict()
d = dict(a="A",b="B")
print(d)
fruits = dict([("apple","red"),("banana","yellow"),("strawberry","pink")])
print(fruits)

# Accessing Dictionary Elements:
student ={
    "name" : "Ranisa",
    "age" : 23,
    "marks" : 90
}
print(student["name"])        # Direct Access (may give error if key not found)
print(student.get("name"))    # Safe Access (returns None or default instead of error)
print(student.get("subject","NA")) 
print(student.get("subject") is None)

# Modifying Dictionary(Adding/Updating):
student ={
    "name" : "Ranisa",
    "age" : 23,
    "marks" : 90
}
student["age"]=22      # Update
student["city"] = "Cuttack"   # Add
print(student)

# Deleting Items:
del student["city"]
print(student)                # Deletes key and donot returns value, gives error if key not found
print(student.pop("age"))     # Deletes key and return value, give error if key not found or use fallback
print(student.pop("age","NA"))
student.clear()                 # removes all items
student ={
    "name" : "Ranisa",
    "age" : 23,
    "marks" : 90
}
print(student.popitem())      # removes last items
print(student)

# Iterating Dictionary:
student ={
    "name" : "Ranisa",
    "age" : 23,
    "marks" : 90
}
for key in student:
    print(key)
for value in student.values():
    print(value)
for key,value in student.items():
    print(key, value)

# Dictionary Operaations:
student ={
    "name" : "Ranisa",
    "age" : 23,
    "marks" : 90
}
print("name" in student)
print("city" not in student)
print(len(student))

# Creating a Nested Dictionary: A dictionary inside the another dictionary
d = {
    "week":"7days",
    "day":{"day1":"Mon",
           "day2":"Tue",
           "day3":"wed",
           "day4":"Thur",
           "day5":"Fri",
           "day6":"Sat",
           "day7":"Sun"}
}
print(len(d))
print(d["day"]["day5"])

# Dictionary Methods: keys(), values(), items()
student ={
    "name" : "Ranisa",
    "age" : 23,
    "marks" : 90
}
key = student.keys()
# Returns a view object containing all the keys of the dictionary.
student["city"]="Bbsr"
print(key)         # Live rfeflection of dictionary changes
print(student.values())
print(student.items())

# Merge Dictionary Python 3.9+ versions:
a = {"a":1}
b = {"b":2,"a":11}
a = a | b
print(a)
b |= a 
print(b)
a = a|b|a
print(a)
print(a.get("c","NA"))
print(a.setdefault("c",23))
print(a)

# Dictionary Comprehension
# Syntax:
# {key_expression:value_expression for item in iterable if condition}
# Example:
# Traditional way....
res = {}
for i in range(1,11):
    if i % 2 == 0:
        res[i] = i ** 2
    else:
        res[i] = i ** 3
print(res)

#  Using Dictionary Comprehension Way..
res = {i:i ** 2 if i % 2 == 0 else i ** 3 for i in range(1,11) }
print(res)
res = {i:i ** 2 for i in range(1,11) if i % 2 == 0}
print(res)

# Create Dictionary From Tuple
student = [("Alice",65),("Bob",78),("Charlie",85)]
res = {i:j for i,j in student}
print(res)
res = {j:i for i,j in student}
print(res)

