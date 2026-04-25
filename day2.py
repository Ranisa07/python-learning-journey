# Arithmetic Operator
a = 28
b = 12
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

# Relational Operators
a = 28
b = 12
print(a<b)
print(a>b)
print(a!=b)
print(a==b)
print(a>=b)
print(a<=b)

# Logical Operator
x = True
y = False
print(x and y)
print(x or y)
print(not x)

# Bitwise Operator
p = 4
q = 6
print(p & q)
print(p | q)
print(p^q)
print(~q)
print(~p)
print(p<<q)
print(p>>q)

# Type Conversion 
a = int(input("Enter Number: "))
b = float(input("Enter Decimal: "))  # Here input() method always takes input as string, So we need to type casting it..

# Prtactice Programs
# 1. Check Even or Odd number
def evenOrOdd():
    n = int(input("Enter number to check even or odd: "))
    if n % 2 == 0:
        print(n, "is a even number")
    else:
        print(n, "is a odd number")
evenOrOdd()

# 2. Find Largest of two numbers
def largestNumber():
    m = int(input("Enter 1st Number: "))
    n = int(input("Enter 2nd number: "))
    if m > n:
        print(m," is the largest number.")
    else:
        print(n," is the largest number.")
largestNumber()

# 3. Find the largest of 3 numbers
def largeNum3():
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    n3 = int(input("Enter 3rd number: "))
    if n1 > n2 and n1 > n3:
        print(n1, " is the largest number..")
    elif n2 > n1 and n2 > n3:
        print(n2, " is the largest number..")
    else:
        print(n3, " is the largest number..")
largeNum3()

# 4. Simple Calculator
def calculator():
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    operator = input("Choose the operators (+, -, *,/,  %): ")
    if operator == '+':
        print(a,"+",b,a+b)
    elif operator == '-':
        print(a,"-",b,a-b)
    elif operator == '*':
        print(a,"*",b,a*b)
    elif operator == '/':
        if a > b and b != 0:
            print(a,"/",b,a/b)
        else:
            print("Invalid numbers")
    elif operator == '%':
        if a > b and b != 0:
            print(a,"%",b,a%b)
        else:
            print("Invalid numbers")
calculator()

# 5. Check Number Positive or Negative
def postive_negative():
    n = int(input("Enter the number: "))
    if n >= 0:
        print(n, " is a positive number..")
    else:
        print(n, " is a negative number")
postive_negative()

# 6. Student result checker

def pass_or_fail():
    marks = int(input("Enter the marks: "))
    if marks > 40:
        print("Passed")
    else:
        print("Failed")
pass_or_fail()
