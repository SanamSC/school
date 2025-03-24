"""
#1
x = int(input("enter a number"))
y = int(input("enter a number"))
z = int(input("enter a number"))
xyz = x * y * z
xy = x + y
yz = y + z
xz = x + z
bracket = xy + yz + xz
answer = (xyz/bracket)
print(answer)


#2
num1= int(input("enter any number"))
num2= int(input("enter any other number"))
add = num1 + num2
sub = num1 - num2
divide = num1/num2
multi = num1 * num2
modu = num1 % num2
floor = num1 // num2
expo = num1**num2

#3
a=1
b=2
c=a
a=b
b=c

#4
d=4
e=5
d,e=e,d

#5
num3 = int(input("enter a number"))
num4 = int(input("enter a number"))
num5 = int(input("enter a number"))
alltg = num3 * num4 * num5
avg = alltg / 3
print ("avg is",avg)

#6
pi = 3.14
pi = int(pi)
rad = int(input("ENTER A RADIUS VALUE: "))
vol = 4/3*pi*rad**3
print(vol)

#7
name = input("enter your name")
age = int(input("enter your age"))
bleh = 100 - age
year = 2024 + bleh
print(year)

#8
c = 3*10**8
mass = int(input("enter a mass value"))
answer = mass*c**2
print(answer)
"""
#9
school = input("enter school name")
name1 =input("enter your name")
classr = input("enter class name")
rollno = int(input("enter roll number"))
section = input("enter your section")
address = int(input("enter adress line1 and 2"))
city = input("enter your city name")
pin = int(input("enter your pin code"))
parent_number = int(input("enter parent/guardian contact number"))
print(	school)
print("studentname:",name1,		"roll no.:", rollno)
print("class:", classr,		"section:", section)
print("Address:" ,address)
print()
print("CITY:", city,			"PIN CODE:", pin)
print("PARENTS/ GUARDIAN CONTACT NO:" , parent_number)