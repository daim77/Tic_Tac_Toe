import tkinter as tk
import numpy as np


def create_board():
    global board
    board = np.full((5, 5), ' ')
    return board


def movement():
    global board_row, board_colomn, order
    if board[board_row][board_colomn] == ' ' and order == 1:
        board[board_row][board_colomn] = '1'
        order *= -1
    if board[board_row][board_colomn] == ' ' and order == -1:
        board[board_row][board_colomn] = '0'
        order *= -1
    return


def diagonal_test():
    global board
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


def horizontal_test():
    global board
    for line in board:
        horizonal_string = ''.join(line)
        if horizonal_string.partition('111')[1] == '111':
            print('Winner is player ONE')
            exit()
        if horizonal_string.partition('000')[1] == '000':
            print('Winner is player TWO')
            exit()


order = 1
board = create_board()

window = tk.Tk()

window.geometry('500x500')
window.title('Tic Tac Toe')


for board_row in range(5):
    for board_colomn in range(5):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1,
        )
        frame.grid(row=board_row, column=board_colomn)
        board_position = tk.Button(
            master=frame,
            text=board[board_row][board_colomn],
            height=4,
            width=8,
            command=movement
        )
        board_position.pack(side='top')


diagonal_test()
horizontal_test()

window.mainloop()
