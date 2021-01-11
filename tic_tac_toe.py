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


def player_turn_order():
    player_row = int(input('row: '))
    player_colomn = int(input('colomn: '))
    if player_row > 4 or player_colomn > 4:
        exit()
    return player_row, player_colomn


def free_position_test(order, player_row, player_colomn, board):
    if board[player_row][player_colomn] == ' ' and order == 1:
        board[player_row][player_colomn] = '0'
    if board[player_row][player_colomn] == ' ' and order == -1:
        board[player_row][player_colomn] = '1'
        order *= -1
    return board, order


def diagonal_test(board):
    board_rot = np.rot90(board)
    for k_diag in range(-2, 3):

        diagonal_line = np.diag(board, k=k_diag)
        diagonal_string = ''.join(diagonal_line)

        diagonal_line_rot = np.diag(board_rot, k=k_diag)
        diagonal_string_rot = ''.join(diagonal_line_rot)

        if diagonal_string.partition('111')[1] == '111' or diagonal_string_rot.partition('111')[1] == '111':
            print('Winner is player TWO')
        if diagonal_string.partition('000')[1] == '000' or diagonal_string_rot.partition('000')[1] == '000':
            print('Winner is player ONE')


def tic_tac_toe():
    order = 1
    board = create_board()

    # welcome and rules

    print_board(board)

    player_turn_order()

    free_position_test(order, player_row, player_colomn, board)

    print_board(board)

    diagonal_test(board)


tic_tac_toe()
