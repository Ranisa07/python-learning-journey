# Python Function: is a reusable block of code..
# Example: without parameter
def msg():
    print("hello")
msg()

# Function With Prameter
def add(a, b):
    print(a+b)
add(3,4)

# Function with return
def square(num):
    return num * num
result = square(4)
print(result)

# Practice Function Programs
# 1. Sum of numbers
def sum():
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print(num1 + num2)
sum()

# 2. Check Even or Odd number
def evenOrOdd():
    n = int(input("Enter number to check even or odd: "))
    if n % 2 == 0:
        print(n, "is a even number")
    else:
        print(n, "is a odd number")
evenOrOdd()

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

# 5. Permutation:
# Formula: nPr= n!/(n-r)!
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact
n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))
n_fact = factorial(n)
nmr_fact = factorial(n-r)
nPr = n_fact//nmr_fact
print("nPr: ", nPr)

# 6. Digit Frequency
# Input: 657386
# count 6, Output: 2
num = int(input("Enter the Number: "))
digit = int(input("Enter the digit for count: "))

def get_digit_frequency(num,digit):
    count = 0
    
    while num > 0:
        dig = num % 10
        num = num // 10
        if dig == digit:
            count += 1
    return count
frequency = get_digit_frequency(num,digit)
print("Result:",frequency)


