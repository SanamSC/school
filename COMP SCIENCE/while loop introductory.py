"""
integer = int(input("enter numbers to get on average"))
total = 0
count = 0
print("total is",integer)
if integer >= 0:
    while integer > 0:
        total = total + integer
        integer = int(input("enter numbers to get an average"))
        count = count + 1
        print("total is" , integer + total)
if integer == " ":
    average = total / count
    print("average is", average)
   """
#2
integers = int(input("enter numbers to get on average"))
total1 = 0
count1 = 0
print("total is",integers)
if integers >= 0:
    while integers > 0:
        total1 = total1 + integers
        integers = int(input("enter numbers to get an average"))
        count1 = count1 + 1
        print("total is" , integers + total1)
if integers != 0:
    average1 = total1 / count1
print("average is", average1)

#3
test = int(input("enter your test grades"))
grades = 0
counter = 0
if test >= 0:
    while test >0:
        grades = grades + test
        test = int (input("enter your test grades"))
        counter = counter +1
averages = grades/counter
if grades >0:
    if averages >=90:
        print("your average grade is an A")
    elif averages >=80 and averages <=89:
        print ("your average grade is a B")
    elif averages >=70 and averages <=79:
        print("your average grade is a C")
    elif averages >=60 and averages <=69:
        print("your average grade is a D")
    else:
        print("your average grade is a F")


#4
number = int(input("enter an integer"))
total = 0
while number > 0:
    totalnum = number +total
    print(number)
    number = number-1
    totalnum = number +total
    total=number+number
print("value is", totalnum)

#5
number1 = int(input("Enter a positive integer: "))
current = 0
while current <= number1:
    print(current)
    current += 2 

