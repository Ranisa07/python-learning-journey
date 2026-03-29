# Loops Concepts
# For Loop Programs      

for i in range(1,8,2):   # 1st position is start position(1), 2nd is end position(8), last positon for steps(2)
    print(i)

# Print 1 to 10
for i in range(1,11):
    print(i)

# Sum of numbers
n = int(input("Enter number: "))
res = 0
for i in range(1,n+1):
    res += i
print(res)

# Multiplication Table
number = int(input("Enter the number: "))
res = 1
for i in range(1,11):
    res = number * i
    print(number,"*",i,"=",res)

# Count Even Numbers(1-50)
count = 0
print("Even numbers are: ")
for i in range(1,51):
    if i % 2 == 0:
        print(i)
        count += 1
print("The total even numbers from 1 to 50: ",count)

# Find Factorial of the number
num = int(input("Enter the number: "))
res = 1
for i in range(1, num+1):
    res =  res * i
    print(res)
print("The total factorial of the ",num,"is: ",res)


#While Loop Programs
# Count numbers
num = 1
count=0
while(num <= 10):
    print(num)
    num+=1
    count+=1
print("Total numbers: ", count)
# Reverse counting (10 - 1)
num = int(input("Enter the number: "))
while(num >= 1):
    print(num)
    num -=1
