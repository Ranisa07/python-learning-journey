# Python String
'''
- In Python, a string is a sequence of characters enclosed in quotes. It can include letters, numbers, symbols or spaces.
- Since, Python has no separate character type, even a single character is treated as a string with length one.
- Strings are widely used for text handling and manipulation.
'''
# Creating a String:
s1 = "Ranisa"      # Double quotes
s2 = 'Programmer'     # Single quotes
s3 = '''I am Learning
Python String for text handling..'''  #triple quotes
print(s1)
print(s2)
print(s3)

# Access Characters:
s1 = 'Programmer'
print(s1[0])      # First Character
print(s1[-1])     #  Last Character
print(s1[4])      # 5th Character   

# Accessing Characters in String by Loop:
s1 = 'Programmer'
for char in s1:
    print(char)

# String Slicing:
# Slicing is a way to extract a portion of a string by specifying the 'start' and 'end' indexes..
st = "Data Science"
print(st[1:5])          # Characters from index 1 to 4
print(st[:3])           # Characters from index start to 2
print(st[1:])           # Characters from index 1 to end
print(st[::-1])         # Reversed String
print(st[::2])          # steps forwarded

# Deleting a String
s = "Python"
del s
# print(s)                # Give a NameError Exception

# Common String Methods:
st = " Hello World!! "
print(len(st))                      # length of the string
print(st.upper())                   # convert into uppercase 
print(st.lower())                   # convert into lowercase
print(st.strip())                   # removing leading & trailing whitespaces
print(st.replace("Hello","Hii"))    # replace all occurance of a specified substring with another

# Concatenating & Repeating String;
s1 = "Hello"
s2 = "Python"
print(s1+" "+s2)                   # Concatenation of 2 strings
print(s1 * 2, s2 * 3)              # Repeating string

# Formatting String:
# Using f-strings:
name = "Ranisa"
age = 23
print(f"Name:{name}, Age:{age}")

# Using format():
st = "My name is {} and I am {} years old.".format("Ranisa",23)
print(st)

# String Membership Testing:
st = "Developer"
print("Dev" in st)
print("DV" in st)

# Practice Programs
# 1. Count Vowels
st = input("Enter string: ")
count = 0
for char in st:
    if char in "aeiouAEIOU":
        count += 1
print("Vowels",count)

# 2. Count Consonant
st = input("Enter string: ")
count = 0
for char in st:
    if char not in "aeiouAEIOU":
        count += 1
print("Consonant",count)

# 3. Reverse String
st = input("Enter string: ")
rev_st = ""
for char in st:
    rev_st = char + rev_st
print(rev_st)

# 4. Palindrome Check:
word = input("Enter Word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("not a Palindrome")

# 5. Count words in sentence:
sentence = input("Write a sentence: ")
count = 0
in_word = False
for char in sentence:
    if char != " " and in_word == False:
        count += 1
        in_word = True
    elif char == " ":
        in_word = False
print(count)

# 6. Remove Space from string
# i) Simple Method (replace())
s = input("Enter a string: ")

result = s.replace(" ", "")

print("After removing spaces:", result)

# ii) Using Loop:
s = input("Enter a string: ")

result = ""
for char in s:
    if char != " ":
        result += char
print("After removing spaces:", result)

# iii) Using join() method:
s = input("Enter a string: ")

result = "".join(s.split())
print("After removing spaces:", result)

# iv) Only extra spaces remove
s = input("Enter a string: ")

result = " ".join(s.split())
print("After removing spaces:", result)

