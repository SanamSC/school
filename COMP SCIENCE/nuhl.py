number = int(input("enter an account number"))
runningTotal = 0
track_number_position = 0
while number > 0:
    track_number_position += 1  #
    digit=number%10
    number = number//10
    if track_number_position%2 == 0:# even number position
        even_number = digit*2
        print(even_number)
        if even_number > 9:
            eventotal = even_number%10 + even_number//10
            print('--->',eventotal)
            runningTotal = runningTotal + eventotal
        else:
            runningTotal = runningTotal + even_number
            print(runningTotal)
    else:
        runningTotal = runningTotal + digit
print(runningTotal)
        