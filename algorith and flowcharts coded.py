"""
#1 - calculate roots:
A = int(input("enter a value for A"))
B = int(input("enter a value for B"))
C=  int(input("enter a value of B"))
divide = 2*A
root1 = -B+(B**2 - 4*A*C)**0.5
root1 = root1/divide
print(root1)
root2=-B-(B**2 - 4*A*C)**0.5
root2 = root2/divide
print(root2)

#2 - read 3 numbers
num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
num3 = int(input("enter 3rd number"))
if num1>num2 and num1>num3:
    print(num1, "is largest number")
elif num2>num1 and num2>num3:
    print(num2,"is greatest number")
else:
    print(num3, "is greatest number")

#3 - print all num 1-50
num = 50
for i in range(50):
    if i%2 ==0:
        print(i)

#4 - find sum of series 1+2+3...N, n is input
N= int(input("enter a valur for N"))
total = 0
for a in range(1, N+1):
    total +=a
print("sum of series is", total)

#5 - find sum and average of series of inputed numbers, stop if input is -1
sum = 0
count = 0
numba = int(input("enter a number"))
while numba != -1:
    sum = sum + numba
    count = count+1
    numba = int(input("enter a number"))
    if numba == -1:
        average = sum/count
print(average)
print(sum)
"""
#6 - find factorial of N, n is inputed
N2 = int(input("enter a number"))
total = 1
for a in range(1, N2+1):
    total *=a
print("factorial of N2 is", total)