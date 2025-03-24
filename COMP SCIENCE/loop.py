#1
side1 = int(input("enter the first side lenght"))
side2 = int(input("enter the second side value"))
side3 = int(input("enter last side value"))
if side1 == side2 == side3:
    print("equillateral")
elif side1 != side2 !=side3:
    print("scalene")
else:
    print("isosceles")
    

#2
num = int(input("enter a integer"))
if num%10 == 4:
    print("ends with 4")
elif num%10 == 8:
    print("ends with 8")
else:
    print("ends with neither")
    
#3
N = int(input("enter a number for N>20"))
for number in range(11,N+1,1):
    print(number)
    if N%3 == 0 and N%7 == 0:
        print("Tipsy Topsy")
    elif N%3 == 0:
        print("Tipsy")
    elif N%7 == 0:
        print("topsy")

 
#4
m = int(input("enter a M value: "))
n = int(input("enter a N value: "))
for i in range(1,m):
    if i%n == 0:
        print(i)
    


    





    