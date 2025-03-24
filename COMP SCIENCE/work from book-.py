#1
temp = int(input("enter a temp value"))
if temp <32:
    print("ice")
elif temp <212:
    print("water")
else:
    print("steam")

#2
x=1
if x>3:
    if x>4:
        print("A", end="")
    else:
        print("B", end = "")
elif x<2:
        if(x!=0):
            print("C", end = "")
        print("D")
        
#3
weather = "raining"
if weather == "sunny":
    print("wear sunblock")
elif weather == "snow":
    print("going skiiing")
else:
    print(weather)
    
#4
if int("zero") == 0:
    print("zero")
elif str(0) == "zero":
    print(0)
elif str(0) =="0":
    print(str(0))
else:
    print("none of the above")
    
#5
N = int(input("enter a number"))
if n == 0:
    print("zero")
elif n ==1:
    print("one")
elif n==2:
    print("two")
elif n ==3:
    print("three")
    
#6
n = int(input("enter an integer"))
if n<1:
    print("invalid value")
else:
    for i in range (1, n+1):
        print(i*i)
#7     
n = int(input("enter a integer:"))
if n >0:
    for a in range(1,n+n):
        print(a/(n/2))
    else:
        print("now quitting")
        
#8