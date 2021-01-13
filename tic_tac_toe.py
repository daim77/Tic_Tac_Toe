# =====Martin Danek™=====
# Project Engeto number 2

import numpy as np
import time


def rules():
    print('*' * 100)
    print('{:^100}'.format('TIC TAC TOE'))
    print('*' * 100)
    print('''
    Welcome in complex Tic-tac-toe game 5-by-5 grid difficulty.
    Each player trying to get four same symbols in a row. 
    Doesn‘t matter if diagonally, horizontally or vertically.
    If no winner after 25 turns - It‘s a tie.
    Each player is called for his/her turn one by one. If you are called:
    Insert row number and column number afterwards within 1 and 5.
    Higher number means STOP!
    The first player is beginning with symbol "X. The second one goes with symbol "O" and so on...
    
    GOOD LUCK!!!
    ''')
    print('*' * 100)


def create_board():
    board = np.full((5, 5), ' ')
    return board


def print_board(board):
    print()
    print('=' * 50)
    print('      |  1  |  2  |  3  |  4  |  5  |')
    for i in range(5):
        line_string = ''
        for j in range(5):
            line_string += '  ' + board[i][j] + '  ' + '.'
        print('.' * 37)
        print('|' + '  ' + str(i + 1) + '  ' + '|' + line_string)
    print('.' * 37)
    print('=' * 50)


def player_turn_order(order):
    while True:
        if order == 'X':
            print('Player X')
        else:
            print('Player O')
        try:
            player_row = int(input('row: ')) - 1
            player_column = int(input('column: ')) - 1
        except (TypeError, ValueError):
            print('Place your turn within five rows or five columns')
            continue

        if player_row > 4 or player_column > 4:
            print('STOP')
            print()
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


def diagonal_test(board, start_time_turn):
    board_rot = np.rot90(board)
    total_time = time.time() - start_time_turn

    for k_diag in range(-1, 2):

        diagonal_line = np.diag(board, k=k_diag)
        diagonal_string = ''.join(diagonal_line)

        diagonal_line_rot = np.diag(board_rot, k=k_diag)
        diagonal_string_rot = ''.join(diagonal_line_rot)

        if diagonal_string.partition('XXXX')[1] == 'XXXX' or diagonal_string_rot.partition('XXXX')[1] == 'XXXX':
            print('*' * 50)
            print('Winner is player X. Total game time was: ', int(total_time), 's')
            exit()
        if diagonal_string.partition('OOOO')[1] == 'OOOO' or diagonal_string_rot.partition('OOOO')[1] == 'OOOO':
            print('*' * 50)
            print('Winner is player O. Total game time was: ', int(total_time), 's')
            exit()


def line_test(board, start_time_turn):
    total_time = time.time() - start_time_turn
    for line in board:
        horizontal_string = ''.join(line)
        if horizontal_string.partition('XXXX')[1] == 'XXXX':
            print('*' * 50)
            print('Winner is player X. Total playing time was: ', int(total_time), 's')
            exit()
        if horizontal_string.partition('OOOO')[1] == 'OOOO':
            print('*' * 50)
            print('Winner is player O. Total playing time was: ', int(total_time), 's')
            exit()
    board_rot = np.rot90(board)
    for line in board_rot:
        vertical_string = ''.join(line)
        if vertical_string.partition('XXXX')[1] == 'XXXX':
            print('*' * 50)
            print('Winner is player X. Total playing time was: ', int(total_time), 's')
            exit()
        if vertical_string.partition('OOOO')[1] == 'OOOO':
            print('*' * 50)
            print('Winner is player O. Total playing time was: ', int(total_time), 's')
            exit()


def tie_test(board, start_time_turn):
    total_time = time.time() - start_time_turn
    player_x = np.count_nonzero(board == 'X')
    player_o = np.count_nonzero(board == 'O')
    if player_x + player_o == 25:
        print('*' * 50)
        print('{:^100}'.format(f'This is a tie. Total playing time was: {total_time}s.'))
    return


def tic_tac_toe():
    start_time_turn = time.time()
    rules()
    order = 'X'
    board = create_board()

    print_board(board)

    while True:
        coordinates = player_turn_order(order)
        player_row = coordinates[0]
        player_column = coordinates[1]

        board_after_mov = movement(order, player_row, player_column, board)
        order = board_after_mov[0]
        board = board_after_mov[1]

        print_board(board)

        diagonal_test(board, start_time_turn)
        line_test(board, start_time_turn)
        tie_test(board, start_time_turn)


tic_tac_toe()
