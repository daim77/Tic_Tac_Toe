import tkinter as tk
import numpy as np


def create_board():
    global board, order
    order = 1
    board = np.full((5, 5), ' ')
    for i in range(5):
        for j in range(5):
            board_field = tk.Button(
                text=board[i][j],
                font=('normal', 40, 'normal'),
                height=2, width=4,
            )
            board_field.grid(row=i, column=j)
    player_turn = tk.Label(text=f"Player {order} turn", font=('normal', 18, 'bold'))
    player_turn.grid(row=7, column=1, columnspan=3)
    return board


def mouse_click(event):
    # x, y = event.x, event.y
    x = root.winfo_pointerx() - root.winfo_rootx()
    y = root.winfo_pointery() - root.winfo_rooty()
    board_row = y // 100
    board_column = x // 100
    if board_row > 4 or board_column > 4:
        return

    movement(board_row, board_column)


def movement(board_row, board_column):
    global board, order
    if board[board_row][board_column] == ' ' and order == 1:
        board[board_row][board_column] = 'X'
        order *= -1
    if board[board_row][board_column] == ' ' and order == -1:
        board[board_row][board_column] = 'O'
        order *= -1
    for i in range(5):
        for j in range(5):
            board_field = tk.Button(
                text=board[i][j],
                font=('normal', 40, 'normal'),
                height=2, width=4,
            )
            board_field.grid(row=i, column=j)

    diagonal_test()
    line_test()

    player_turn = tk.Label(text=f"Player {order} turn", font=('normal', 22, 'bold'))
    player_turn.grid(row=7, column=1, columnspan=3)
    return board


def diagonal_test():
    global board
    board_rot = np.rot90(board)
    for k_diag in range(-2, 3):

        diagonal_line = np.diag(board, k=k_diag)
        diagonal_string = ''.join(diagonal_line)

        diagonal_line_rot = np.diag(board_rot, k=k_diag)
        diagonal_string_rot = ''.join(diagonal_line_rot)

        if diagonal_string.partition('XXX')[1] == 'XXX' or diagonal_string_rot.partition('XXX')[1] == 'XXX':
            print('Winner is player ONE')
            exit()
        if diagonal_string.partition('OOO')[1] == 'OOO' or diagonal_string_rot.partition('OOO')[1] == 'OOO':
            print('Winner is player TWO')
            exit()


def line_test():
    global board
    for line in board:
        horizontal_string = ''.join(line)
        if horizontal_string.partition('XXX')[1] == 'XXX':
            print('Winner is player ONE')
            exit()
        elif horizontal_string.partition('OOO')[1] == 'OOO':
            print('Winner is player TWO')
            exit()

    board_rot = np.rot90(board)
    for line in board_rot:
        horizontal_string = ''.join(line)
        if horizontal_string.partition('XXX')[1] == 'XXX':
            print('Winner is player ONE')
            exit()
        elif horizontal_string.partition('OOO')[1] == 'OOO':
            print('Winner is player TWO')
            exit()


root = tk.Tk()
root.geometry('600x600')
root.title('Tic Tac Toe')

order = 1
board = create_board()

root.bind('<Button-1>', mouse_click)

reset_button = tk.Button(text='RESTART', font=('normal', 18, 'bold'), command=create_board, fg='red')
reset_button.grid(row=8, column=1)

reset_button = tk.Button(text='STOP', font=('normal', 18, 'bold'), command=exit, fg='red')
reset_button.grid(row=8, column=3)


root.mainloop()
