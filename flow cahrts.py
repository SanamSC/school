#1
"""
for a in range(10+1):
    print (a)
    

    
#2
start = input("click enter to start")
for b in range(10,-1,-1):
    print(b)
    
#3
multiple = 0
hash = "#"
for c in range(0,7,1):
    multiple = multiple + 1
    print(hash*multiple)
    
#4
column = int(input("enter a value for the amount of columns"))
row = int(input("enter a value for the amount of rows"))
hashtag = "#"
for d in range(0,row,1):
    print(hashtag*column)
"""
#5
digit1 = -1
digit2 = -1
for e in range(0,10+1,1):
    digit1 = digit1 + 1
    digit2 = digit2 + 1
    answer = digit1*digit2
    print(digit1, "x", digit2, "=", answer )
    
#6
number = 100
for f in range(0,number+1,1):
    if f%2 == 0:
        print(f)
        
#7
numba=100
for g in range(0,numba+1,1):
    if g%2 !=0:
        print(g)
        
#8
total = 0
numba2 = 100
for i in range(0,100+1,1):
    total = total + i
    answer = total
    print(total)
    
#9
numba3 = 100
even_total = 0
odd_total = 0
for g in range(0,100+1,1):
    if g%2 == 0:
        even_total = even_total + g
        even_answer = even_total
for h in range(0,100+1,1):
    if h%2 != 0:
        odd_total = odd_total + h
        odd_answer = odd_total
print("sum of all odd numbers is", odd_answer)
print("sum of all even numbers is", even_answer)