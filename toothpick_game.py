"""
print("WELCOME TO THE TOOTHPICK GAME!")
print("*" * 50)

num_left = 13
player1_name = input("Enter Player 1's Name: ")
player2_name = input("Enter Player 2's Name: ")

while True:
    print("| " * num_left)
    print(f"There are {num_left} toothpicks left")
    p1_choice = int(input(f"{player1_name}, how many toothpicks do you take? "))
    num_left -= p1_choice
    if num_left <= 0:
        print(f"{player1_name} wins the game!")
        break

    print("| " * num_left)
    print(f"There are {num_left} toothpicks left")
    p2_choice = int(input(f"{player2_name}, how many toothpicks do you take? "))
    num_left -= p2_choice
    if num_left <= 0:
        print(f"{player2_name} wins the game!")
        break
print("GAME OVER!")
"""

# REFACTORED GAME
print("WELCOME TO THE TOOTHPICK GAME!")
print("*" * 50)

num_left = 13
player1_name = input("Enter Player 1's Name: ")
player2_name = input("Enter Player 2's Name: ")
current_player = player1_name

while True:
    print("| " * num_left)
    print(f"There are {num_left} toothpicks left")
    choice = int(input(f"{current_player}, how many toothpicks do you take? "))
    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input(f"You can only chose 1, 2, or 3: "))
    num_left -= choice
    if num_left <= 0:
        print(f"{current_player} wins the game!")
        break
    if current_player == player1_name:
        current_player = player2_name
    else:
        current_player = player1_name

print("GAME OVER!")