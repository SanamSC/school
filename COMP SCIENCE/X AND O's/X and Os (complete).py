p1 = input("Click enter to play: ")
p2 = input("Click enter to play")
print("GAME STARTED!")

# Initialize the board
line1 = [1, 2, 3]
line2 = [4, 5, 6]
line3 = [7, 8, 9]

print(line1)
print(line2)
print(line3)

# Track remaining turns
turns = 9

# Function to check if someone won
def check_winner():
    winning_combinations = [
        [line1[0], line1[1], line1[2]],  # Row 1
        [line2[0], line2[1], line2[2]],  # Row 2
        [line3[0], line3[1], line3[2]],  # Row 3
        [line1[0], line2[0], line3[0]],  # Column 1
        [line1[1], line2[1], line3[1]],  # Column 2
        [line1[2], line2[2], line3[2]],  # Column 3
        [line1[0], line2[1], line3[2]],  # Diagonal \
        [line1[2], line2[1], line3[0]],  # Diagonal /
    ]
    
    for combo in winning_combinations:
        if combo[0] == combo[1] == combo[2]:  # All three are the same
            return combo[0]  # Return the winning symbol ('X' or 'O')
    return None  # No winner yet

# Function to check if a move is valid
def is_valid_move(move):
    return move in range(1, 10) and str(move) in str(line1 + line2 + line3)

# Game loop
while turns > 0:
    # Player One's Turn
    while True:
        move = int(input("PLAYER ONE: What position on grid? "))
        if is_valid_move(move):
            break
        print("Invalid move! Try again.")

    turns -= 1
    if move < 4:
        line1[move - 1] = "X"
    elif move < 7:
        line2[move - 4] = "X"
    else:
        line3[move - 7] = "X"
    
    print(line1)
    print(line2)
    print(line3)

    winner = check_winner()
    if winner:
        print(f"🎉 PLAYER ONE WINS! ({winner}) 🎉")
        break

    if turns == 0:
        print("GAME OVER! It's a tie.")
        break

    # Player Two's Turn
    while True:
        move2 = int(input("PLAYER TWO: What position on grid? "))
        if is_valid_move(move2):
            break
        print("Invalid move! Try again.")

    turns -= 1
    if move2 < 4:
        line1[move2 - 1] = "O"
    elif move2 < 7:
        line2[move2 - 4] = "O"
    else:
        line3[move2 - 7] = "O"

    print(line1)
    print(line2)
    print(line3)

    winner = check_winner()
    if winner:
        print(f" PLAYER TWO WINS! ({winner}) ")
        break

    if turns == 0:
        print("GAME OVER! It's a tie.")
        break
