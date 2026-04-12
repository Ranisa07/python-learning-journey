# Python Tuple: is a`ordered, immutable collection of items.
# Creating Tuple:
my_tuple = (1,2,3)      # tuple
other_tuple = 1,2,3     # tuple
print(type(other_tuple))           # Check is it tuple or not
a = (3,)               # tuple
b = 1      # Not a tuple
print(type(a))
print(type(b))

# Using tuple():
tuple_from_string = tuple("Hello")
print(tuple_from_string)
tuple_from_list = tuple([1,2,3,4,5])
print(tuple_from_list)

# Note:
'''
- Tuples are created using commas, not parenthesis.
- Parentheses improve readability but are not required.
- Trailing commas in multi-element tuples are optimal.
'''
# t = tuple(5)      TypeError: 'int' object is not iterable
t = tuple([5])      # Right way to add single element in tuple

# Creating Empty Tuple:
empty = ()           # Empty tuple by using parenthese
print(type(empty))     
empty = tuple()      # Empty tupkke by using tuple() constructor
print(type(empty))

# Key Difference between Tuple and List:
'''
=> Tuples are immutable.
=> Tuples use parentheses and Lists use square brackets.
=> Tuples are generally smaller and faster than List.
'''
t = (1,2,3)
# t[0] = 11     TypeError: 'tuple' object does not support item assignment

# Immutability:
t = (1,2,3)
# t.append(4)    Raises AttributeError
# t.remove(1)    Raises AttributeError
# del t[1]       Raises TypeError
del t       # whole tuple is deleted
# print(t)    Raises NameError

# => Immutability applies to the tuple container, not to the objects inside
t = (1,[2,3])
t[1].append(4)
print(t)
# => Immutable tuples can be used as keys in dictionaries or stored in sets

# Concatenate:
original_tuple = (1,2,3)
new_tuple = original_tuple + (4,5)
print(new_tuple)
original_tuple = original_tuple + (6,7)
print(original_tuple)

# Accessing tuple elements:
fruits = ("apple","banana","cherry","date","elderbery")
print(fruits[0])
print(fruits[-2])
# Slicing - [start:end:step]
print(fruits[1:4])
print(fruits[::-1])
nested_tuple = ((1,2),(3,4),(5,6))
print(nested_tuple[0][1])
t = (32,"hello",[2,3,4],{"key":"value"})
print(t[3]["key"])

# Unpacking tuples:
# - Tuple unpacking allows you to assign tuple elements to individual variables in single operation.
t = 1,2,3
print(type(t))
a,b,c = t
print(a,b,c)
# Python does this by matching the structure(number of items) on both sides of the assignment.
# a,b = 1,2,3         ValueError: too many values to unpack (expected 2, got 3)
a, *b = 1, 2, 3
print(a)
print(b)
a, *b = "hello"
print(a,b)

data = ("John", 30, "Manager", 50000, "BBSR")
name, age, designation, salary, city = data
print(name, age, designation, salary, city)

# Iterating Tuples:
fruits = ('apple',"banana","cherry")
for fruit in fruits:
    print(fruit)

colors = ('red', 'yellow', 'orange', 'pink')
for index,color in enumerate(colors):
    print(index,color)

for index,color in enumerate(colors, start=10):   # start index from 10
    print(index,color)

pairs = [(1,'a'),(2,'b'),(3,'c')]
for number,letter in pairs:
    print(number,letter)

# Methods: count and index
num = (1,2,3,4,5,6,6)
print(num.count(6))
print(num.index(5))

