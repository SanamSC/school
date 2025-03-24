"""
#q1
number = input("enter your 10 digit phone number with 2 dashes")
lenght = len(number)
if number[4] =="-" and number[7] == "-":
    if lenght == 12:
        print(number, "is a valid phone number")
else:
    print(number , "is not a valid number")
    
#q2
string = input("enter you number")
lenghty = len(string)
counter = 0
for a in string:
    if a.isdigit():
        counter = counter + int(a)
        print(a)
    elif string.isalpha:
        print(string, "has no digits")
print("sum of digits is", counter)
print("original input was", string)
"""
#q3
sentence = input("type some sentences")
lenght = len(sentence)
count = 0
for b in sentence:
    if b.isalnum():
        count = count + 1
        print(count)
divide= count / lenght
percent = divide * 100
words = sentence.split()
count2 = 0
for word in words:
    count2 += 1
    print(count2)
print("number of cahracters is", lenght)
print("number of words is" , count2)
print("percentage of alpha numeric is", percent,"%")

#q4

    

                
        
        



    
