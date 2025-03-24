string = "monkey"
blank = ""
guessedltrs = ""
for i in(string):
    blank = blank + "_"
lives = 7
hangmanstages =[
"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
"""
,
"""
 +---+
 |   |
 O   |
/|\  |
/    |
"""
,
"""
 +---+
 |   |
 O   |
/|\  |
     |
"""
,
"""
 +---+
 |   |
 O   |
/|   |
     |
"""
,
"""
 +---+
 |   |
 O   |
/    |
     |
"""
,
"""
 +---+
 |   |
 O   |
     |
     |
"""
,
"""
 +---+
 |   |
     |
     |
     |

"""
]
print(blank)
while "_" in blank and lives>0:
    print(hangmanstages[lives-1])
    string = "monkey"
    guess = input("enter a random letter :")
    print(guessedltrs)
    if guess in guessedltrs:
        print("you have already guessed this letter, guess again!:")
    #if guess not in guessedltrs:
        #guessedltrs = guessedltrs + guess +","
        print("CURRENT GUESSED LETTERS ARE:", guessedltrs)
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
        if guess not in string:
            guessedltrs = guessedltrs + guess + ","
            lives = lives -1
            print("incorrect you now have", lives, "lives left")
            print("Current word is", blank)
    if lives == 0:
        print("INCORRECT! GAME OVER")
        break
if "_" not in string and lives>=1:
    print("Congrats! you guessed", string)
       # blank = blank[0:2]+userLetter+blank[3:]

