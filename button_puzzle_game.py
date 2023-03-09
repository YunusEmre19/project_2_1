import numpy as np
import os

# game object types:
# 0 -> empty space
# 1 -> wall
# 2 -> player
# 3 -> box
# 4 -> button
# 5 -> hole

level_test_1 = np.ones((7,7))
level_test_1[1:6,1:6] = 0
level_test_1[4,2] = 3
level_test_1[5,5] = 4
level_test_1[3,4] = 5

player_x = 3
player_y = 3

moves = 20

level_test_1[player_y,player_x] = 2
print(level_test_1)

def movement(y_move,x_move):
    global player_x, player_y, level_test_1, game_loop, is_winning
    moved_pos = level_test_1[player_y + y_move, player_x + x_move]
    next_pos = -1

    if moved_pos == 3:
        next_pos = level_test_1[player_y + 2*y_move, player_x + 2*x_move]
        if next_pos == 0:
            level_test_1[player_y + 2*y_move, player_x + 2*x_move] = 3
        elif next_pos == 4:
            game_loop = False
            is_winning = True
        elif next_pos == 5:
            level_test_1[player_y + 2*y_move, player_x + 2*x_move] = 0

    if moved_pos == 0 or (moved_pos == 3 and next_pos in {0,5}):
        level_test_1[player_y,player_x] = 0
        player_y+=y_move
        player_x+=x_move

    level_test_1[player_y, player_x] = 2

is_winning = False
game_loop = True
while game_loop:
    os.system("cls")
    print(moves,"move(s) left\n")
    moves -=1
    print(level_test_1)

    user_input = input("Move: ")

    if user_input == "kill" or moves == 0:
        game_loop = False

    elif user_input == "w": movement(-1,0)
    elif user_input == "s": movement(1,0)
    elif user_input == "d": movement(0,1)
    elif user_input == "a": movement(0,-1)

if is_winning:
    print("Congrats! You won the game!\nHere is your prize: ", np.random.randint(100000))

else:
    print("Congrats! You somehow managed to lose the game!")
