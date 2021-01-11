# =====Martin Danek™=====
# Project Engeto number 2
# {rules,
#  5x5 array,
#  2 players,
#  time measurement per turn, per game,
#  who is winner,
#  save game after every turn
#  }

import numpy as np


def create_board():
    board = np.full((5, 5), ' ')
    return board


def print_board(board):
    print(board)


def player_turn_order(order):
    if order == 1:
        print('Player ONE')
    else:
        print('Player TWO')
    player_row = int(input('row: '))
    player_colomn = int(input('colomn: '))
    if player_row > 4 or player_colomn > 4:
        exit()
    return player_row, player_colomn


def movement(order, player_row, player_colomn, board):
    if board[player_row][player_colomn] == ' ' and order == 1:
        board[player_row][player_colomn] = '1'
        order *= -1
    if board[player_row][player_colomn] == ' ' and order == -1:
        board[player_row][player_colomn] = '0'
        order *= -1
    return order, board


def diagonal_test(board):
    board_rot = np.rot90(board)
    for k_diag in range(-2, 3):

        diagonal_line = np.diag(board, k=k_diag)
        diagonal_string = ''.join(diagonal_line)

        diagonal_line_rot = np.diag(board_rot, k=k_diag)
        diagonal_string_rot = ''.join(diagonal_line_rot)

        if diagonal_string.partition('111')[1] == '111' or diagonal_string_rot.partition('111')[1] == '111':
            print('Winner is player ONE')
            exit()
        if diagonal_string.partition('000')[1] == '000' or diagonal_string_rot.partition('000')[1] == '000':
            print('Winner is player TWO')
            exit()


def horizontal_test(board):
    for line in board:
        horizonal_string = ''.join(line)
        if horizonal_string.partition('111')[1] == '111':
            print('Winner is player ONE')
            exit()
        if horizonal_string.partition('000')[1] == '000':
            print('Winner is player TWO')
            exit()


def tic_tac_toe():
    order = 1
    board = create_board()
    # welcome and rules
    print('Player one is beginning and he has ONE symbol')

    print_board(board)

    while True:
        coordinates = player_turn_order(order)
        player_row = coordinates[0]
        player_colomn = coordinates[1]

        board_after_mov = movement(order, player_row, player_colomn, board)
        order = board_after_mov[0]
        board = board_after_mov[1]

        print_board(board)

        diagonal_test(board)
        horizontal_test(board)


tic_tac_toe()