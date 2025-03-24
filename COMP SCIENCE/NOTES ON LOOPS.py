#we use for loops to
#run code for a fixed number of times

#if you wish to print the characters in a string

my_string = "hello"
#for variable in <list>
for character in my_string:
    print(character)
    
#if you wish to loop through numbers
#for <variable> in range(start, stop , step
#upto but not including the "stop" value
#start defaults to 0
#step defaults to 1
for number in range (10,1,-1):
    print(number, end = " ")

run_again = "yes"
while run_again == "yes":
    print("Hello world")
    run_again = input("do you want the loop to run again? Type \"yes\" to run")
    
total = 0
while total < 100:
    num = int(input("Enter a number"))
    total = total + num
print("the total is" , total)