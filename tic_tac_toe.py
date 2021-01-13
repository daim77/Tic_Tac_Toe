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


def rules():
    print('*' * 100)
    print('{:^100}'.format('TIC TAC TOE'))
    print('*' * 100)
    print('''
    Welcome in complex Tic-tac-toe game 5-by-5 grid difficulty.
    Each player trying to get three same symbols in a row. 
    Doesn‘t matter if diagonally, horizontally or vertically.
    If no winner after 25 turns - It‘s a tie.
    Each player is called for his/her turn one by one. If you are called:
    Insert row number and column number afterwards.
    The first player is beginning with symbol "X. The second one goes with symbol "O" and so on...
    
    GOOD LUCK!!!
    ''')
    print('*' * 100)


def create_board():
    board = np.full((5, 5), ' ')
    return board


def print_board(board):

    print(board)


def player_turn_order(order):
    start_time_turn = time.time()

    if order == 'X':
        print('Player X')
    else:
        print('Player O')
    try:
        player_row = int(input('row: ')) - 1
        player_column = int(input('column: ')) - 1
    except (TypeError, ValueError):
        print('Coordinates are whole positive numbers!')
        exit()
        return

    if time.time() - start_time_turn > 100:
        print('time is over')
        exit()

    if player_row > 5 or player_column > 5:
        exit()
    return player_row, player_column


def movement(order, player_row, player_column, board):
    if board[player_row][player_column] == ' ' and order == 'X':
        board[player_row][player_column] = 'X'
        order = 'O'
    if board[player_row][player_column] == ' ' and order == 'O':
        board[player_row][player_column] = 'O'
        order = 'X'
    return order, board


def diagonal_test(board):
    board_rot = np.rot90(board)
    for k_diag in range(-2, 3):

        diagonal_line = np.diag(board, k=k_diag)
        diagonal_string = ''.join(diagonal_line)

        diagonal_line_rot = np.diag(board_rot, k=k_diag)
        diagonal_string_rot = ''.join(diagonal_line_rot)

        if diagonal_string.partition('XXX')[1] == 'XXX' or diagonal_string_rot.partition('XXX')[1] == 'XXX':
            print('Winner is player X')
            exit()
        if diagonal_string.partition('OOO')[1] == 'OOO' or diagonal_string_rot.partition('OOO')[1] == 'OOO':
            print('Winner is player O')
            exit()


def line_test(board):
    for line in board:
        horizontal_string = ''.join(line)
        if horizontal_string.partition('XXX')[1] == 'XXX':
            print('Winner is player X')
            exit()
        if horizontal_string.partition('OOO')[1] == 'OOO':
            print('Winner is player O')
            exit()
    board_rot = np.rot90(board)
    for line in board_rot:
        vertical_string = ''.join(line)
        if vertical_string.partition('XXX')[1] == 'XXX':
            print('Winner is player X')
            exit()
        if vertical_string.partition('OOO')[1] == 'OOO':
            print('Winner is player O')
            exit()


def tie_test(board):
    player_x = np.count_nonzero(board == 'X')
    player_o = np.count_nonzero(board == 'O')
    if player_x + player_o == 25:
        print('*' * 100)
        print('{:^100}'.format('This is a tie'))
    return


def tic_tac_toe():
    rules()
    order = 'X'
    board = create_board()
    # play time measurement
    # welcome and rules
    print('Player X is beginning and he has X symbol')


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
        line_test(board)
        tie_test(board)


tic_tac_toe()
