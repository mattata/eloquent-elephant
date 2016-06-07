# Author:   Matty T.
# Date:     05 June 2016

import random

print("Welcome to Iceberg! Let's get started.\n")

board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

number_of_icebergs = random.randint(8, 11)

print("Number of icebergs: " + str(number_of_icebergs))


"""def make_blank_board():
    blank_board = []
    horizontal = []
    for y in range(0, 8):
        for x in range(0, 8):
            horizontal.append(' ')
        blank_board.append(horizontal)
    return blank_board"""


def assign_icebergs(icebergs, board):
    for i in range(icebergs):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if board[x][y] == ' ':
            board[x][y] = '*'
        else:
            icebergs += 1
    return board

icebergs_board = assign_icebergs(number_of_icebergs, board)


def place_enemy_ship(board):
    enemy_present = False
    while not enemy_present:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if board[x][y] == ' ':
            board[x][y] = 'Z'
            enemy_present = True
        else:
            continue
    return board


def place_my_ship(board):
    me_present = False
    while not me_present:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if board[x][y] == ' ':
            board[x][y] = 'Y'
            me_present = True
        else:
            continue
    return board

enemy_board = place_enemy_ship(icebergs_board)
game_board = place_my_ship(enemy_board)

for line in game_board:
    print(line)
    [[0,1], [1,1], [1,0], [-1,-1], [1,-1], [0,-1], [-1,0], [-1,1]]
