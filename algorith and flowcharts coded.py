#1 calculate roots:
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

#2 read 3 numbers
num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
num3 = int(input("enter 3rd number"))
if num1>num2 and num1>num3:
    print(num1, "is largest number")
elif num2>num1 and num2>num3:
    print(num2,"is greatest number")
else:
    print(num3, "is greatest number")
    
#3print all num 1-50
num = 50
for i in range