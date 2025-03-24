p1 = input("click enter to play:")
p2=input("click enter to play")
print("GAME STARTED!")
line1 = [1,2,3]
line2 = [4,5,6]
line3 = [7,8,9]
print(line1)
print(line2)
print(line3)
winning_combos = [
        [line1[0], line1[1], line1[2]],  
        [line2[0], line2[1], line2[2]],  
        [line3[0], line3[1], line3[2]], 
        [line1[0], line2[0], line3[0]],  
        [line1[1], line2[1], line3[1]],  
        [line1[2], line2[2], line3[2]],  
        [line1[0], line2[1], line3[2]],  
        [line1[2], line2[1], line3[0]],  
    ]

turns = 9
entered = " "
while turns>0:
    move = int(input("PLAYER ONE: what postion on grid?"))
    entered = entered + move
    turns= turns-1
    if move <4:
        line1[move-1]="X"
        print(line1)
        print(line2)
        print(line3)
    elif move<7 and move>=4:
        line2[move-4] = "X"
        print(line1)
        print(line2)
        print(line3)
    elif move>=7 and move<=9:
        line3[move-7]="X"
        print(line1)
        print(line2)
        print(line3)
    move2 = int(input("PLAYER TWO: what position on grid?"))
    turns = turns - 1
    if move2 <4:
        line1[move2-1]="O"
        print(line1)
        print(line2)
        print(line3)
    elif move2<7 and move2>=4:
        line2[move2-4]="O"
        print(line1)
        print(line2)
        print(line3)
    elif move2>=7 and move2<=9:
        line3[move2-7]="O"
        print(line1)
        print(line2)
        print(line3)
    if turns == 0:
        print("GAME OVER")
        break
    

    

    

    
    