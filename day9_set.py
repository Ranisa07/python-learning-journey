# Python Set
# What is a Set ?
# Unordered, mutable, unindexed, unique, heterogenuous
# Union, intersection, difference
# Should have immutable items
# Fast membership testing

# Creating a Set:
# A. Set literals {}
# B. set() constructor

num = {1,2,3,4,5}
names = {"Rani", "Prachi", "Liku", "Priti"}
mixed = {"rani",1,33.4,True}
print(num)

# Creating an Empty Set:
e = {}  #This creates an empty dictionary, not a set
# NOTE: We can't use {} for empty set, we can use set() constructor for empty set

e = set()
# s = {1, "hello", True, (1,2,3), [1,2,3]}    gives "cannot use 'list' as a set element (unhashable type: 'list')"
# print(s)

# The set() function creates a set from an iterable (like a list, tuple, or string)
# Set From List
list_data = [1,2,4,5,6,6,3]
set_from_list = set(list_data)
print(type(set_from_list))

# Set from String:
st = "hello"
set_from_st = set(st)
print(set_from_st)

# Set from Tuple:
tp = (1,2,4,4,5,7,7)
set_from_tp = set(tp)
print(set_from_tp)

# Set Operations:
my_set = {1, 2, 3}
print("Original:",my_set)
my_set.add(4)
print("After adding 4:",my_set)
my_set.add("abc")
print(my_set)
# Using update() to add multiple elements 
# my_set.update(5,6,7)      --> TypeError: 'int' object is not iterable
my_set.update([5,6,7])
print("After update with list:",my_set)
my_set.update("xyz")
print(my_set)