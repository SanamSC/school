direction = input("do you want to count up and down?: ")
if direction == "up" :
    num7 = int(input("enter a top number "))
    for orange in range(1 , num7 +1 , 1):
        if direction == "up":
            print(orange)
elif direction == "down":
    num8 = int(input(" enter a number below 20 "))
    for banana in range(20 , num8 - 1 , -1):
            print(banana)
if direction != "up" and direction != "down":
    print("I dont understand")

party = int(input("how many people would you like at your party?: "))
if party < 10:
    for orange in range(party):
        name = input("enter their name ")
        print(f"{name} has been invited ")
if party > 10:
    print("too many people! ")
    
