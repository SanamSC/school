#1
day1 = int(input("tempature on day one"))
day2 = int(input("tempature on day two"))
day3 = int(input("tempature on day three"))
day4 = int(input("tempature on day four"))
day5 = int(input("tempature on day five"))
day6 = int(input("tempature on day six"))
day7 = int(input("tempature on day seven"))
average = day1 + day2 + day3 + day4 + day5 + day6 + day7
print(average / 7)

#2
PI = 3.14
PI = float(PI)
x = int(input("enter an X value"))
y = int(input("enter a y value"))
z = int(input("enter a Z value"))
print(4*x**4 + 3*y**3 + 9*z + 6*PI)

#3
seconds = int(input("enter an amount of seconds"))
min = seconds // 60
sec = seconds % 60
print ( min , sec)

#4
hour = int(input("enter an hour between 1 and 12"))
ahead = int(input("how many hours ahead would you like to know"))
timeahead = hour + ahead
print( "in", ahead , "hours it will be " , timeahead%12, "oclock")

#5
threedigit = int(input("enter a three digit number"))
firstdigit = threedigit%10
seconddigit = threedigit//10
third = seconddigit//10
fourth = seconddigit%10
print(firstdigit , fourth,third, sep="")

#6
month = int(input("enter a month"))
day = int(input("enter a day"))
month2 = month * 30
days = month2 + day
print("this is day", days , "of the current year")