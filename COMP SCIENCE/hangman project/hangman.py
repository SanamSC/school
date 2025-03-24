string = "monkey"
blank = ""
lives = 7
for i in (string):
    blank = blank +" _"
print(blank)
while "_" in blank:
    string = "monkey"
    guess = input("enter a random letter")
  
    print("you have", lives,"lives left")
    if guess in string:
        pos= string.find(guess)
        print(guess, "appears in word in", pos ,"postion")
        amount = string.count(guess)
        print(guess , "appears in word", amount,"times")
    else:
        lives = lives -1
        print("incorrect you now have", lives, "lives left")
                
       # blank = blank[0:2]+userLetter+blank[3:]