import tkinter as tk
import numpy as np


def create_board():
    global board, order
    order = 1
    board = np.full((5, 5), ' ')
    return board


def movement():
    global board_row, board_column, order
    if board[board_row][board_column] == ' ' and order == 1:
        board[board_row][board_column] = '1'
        order *= -1
    if board[board_row][board_column] == ' ' and order == -1:
        board[board_row][board_column] = '0'
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
    for board_column in range(5):
        frame_grid = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1,
            bg='blue',
        )
        frame_grid.grid(row=board_row, column=board_column)
        board_position = tk.Button(
            master=frame_grid,
            text=board[board_row][board_column],
            height=4,
            width=8,
            command=movement
        )
        board_position.pack()

player_turn = tk.Label(text=f"Player {order} turn", font=('normal', 22, 'bold'))
player_turn.grid(row=6, column=1, columnspan=3)

reset_button = tk.Button(text='RESTART', command=create_board, fg='red')
reset_button.grid(row=7, column=2)
reset_button = tk.Button(text='STOP', command=exit, fg='red')
reset_button.grid(row=7, column=3)

diagonal_test()
horizontal_test()

window.mainloop()
