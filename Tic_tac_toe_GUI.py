import tkinter as tk
import numpy as np


def create_board():
    global board, order
    order = 1
    board = np.full((5, 5), ' ')
    return board


def movement(board_row, board_column):
    global board, order
    if board[board_row][board_column]['text'] == ' ' and order == 1:
        board[board_row][board_column].config(text='1')
        order *= -1
    if board[board_row][board_column]['text'] == ' ' and order == -1:
        board[board_row][board_column]['text'] = '0'
        order *= -1
    return board


def diagonal_test():
    global board
    board = np.array(board)
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
window.geometry('600x600')
window.title('Tic Tac Toe')

board = board.tolist()

for i in range(5):
    for j in range(5):
        board[i][j] = tk.Button(
            text=board[i][j],
            font=('normal', 40, 'normal'),
            height=2, width=4,
            command=lambda r=i, c=j: movement(r, c)
        )
        board[i][j].grid(row=i, column=j)


player_turn = tk.Label(text=f"Player {order} turn", font=('normal', 22, 'bold'))
player_turn.grid(row=6, column=1, columnspan=3)

reset_button = tk.Button(text='RESTART', command=create_board, fg='red')
reset_button.grid(row=7, column=0)

reset_button = tk.Button(text='STOP', command=exit, fg='red')
reset_button.grid(row=7, column=4)

# diagonal_test()
# horizontal_test()

window.mainloop()
