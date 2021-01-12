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
import time


def create_board():
    board = np.full((5, 5), ' ')
    return board


def print_board(board):
    print(board)


def player_turn_order(order):
    start_time_turn = time.time()

    if order == 1:
        print('Player ONE')
    else:
        print('Player TWO')
    try:
        player_row = int(input('row: '))
        player_column = int(input('column: '))
    except (TypeError, ValueError):
        print('Coordinates are whole positive numbers!')
        exit()
        return

    if time.time() - start_time_turn > 100:
        print('time is over')
        exit()

    if player_row > 4 or player_column > 4:
        exit()
    return player_row, player_column


def movement(order, player_row, player_column, board):
    if board[player_row][player_column] == ' ' and order == 1:
        board[player_row][player_column] = '1'
        order *= -1
    if board[player_row][player_column] == ' ' and order == -1:
        board[player_row][player_column] = '0'
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
    # play time measurement
    # welcome and rules
    print('Player one is beginning and he has ONE symbol')

    # game_gui()

    print_board(board)

    while True:
        coordinates = player_turn_order(order)
        player_row = coordinates[0]
        player_column = coordinates[1]

        board_after_mov = movement(order, player_row, player_column, board)
        order = board_after_mov[0]
        board = board_after_mov[1]

        print_board(board)

        diagonal_test(board)
        horizontal_test(board)


tic_tac_toe()
