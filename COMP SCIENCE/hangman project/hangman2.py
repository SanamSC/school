string = "monkey"
blank = ""
for i in(string):
    blank = blank + "_"
lives = 7
print(blank)
while "_" in blank:
    string = "monkey"
    guess = input("enter a random letter")
    if guess in string:
        print("Correct! you still have", lives,"lives left")
        pos= string.find(guess)
       # print(guess, "appears in word in", pos,"th postion")
        amount = string.count(guess)
        #print(guess , "appears in word", amount,"time(s)")
        for i in range(len(string)):
            if string[i] == guess:
                blank = blank[:i] + guess + blank[i + 1:]
                print("current word is", blank) 
    else:
        lives = lives -1
        print("incorrect you now have", lives, "lives left")
        print("Current word is", blank)
if "_" not in string:
    print("Congrats! word is", string)
                
       # blank = blank[0:2]+userLetter+blank[3:]



   guessedltrs = guessedltrs + guess +","
    print("CURRENT GUESSED LETTERS ARE:", guessedltrs)