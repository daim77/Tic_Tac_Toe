import tkinter as tk
import numpy as np


def create_board():
    global board, order
    order = 1
    board = np.full((5, 5), ' ')
    return board


def movement(board_row, board_column):
    global board, order
    print(board_row, board_column)
    if board[board_row][board_column]['text'] == ' ' and order == 1:
        board[board_row][board_column]['text'] = '1'
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
window.geometry('500x500')
window.title('Tic Tac Toe')

board = board.tolist()

for r in range(5):
    for c in range(5):
        board[r][c] = tk.Button(text=board[r][c], height=4, width=8, command=lambda: movement(r, c))
        board[r][c].grid(row=r, column=c)


player_turn = tk.Label(text=f"Player {order} turn", font=('normal', 22, 'bold'))
player_turn.grid(row=6, column=1, columnspan=3)

reset_button = tk.Button(text='RESTART', command=create_board, fg='red')
reset_button.grid(row=7, column=0)

reset_button = tk.Button(text='STOP', command=exit, fg='red')
reset_button.grid(row=7, column=4)

# diagonal_test()
# horizontal_test()

window.mainloop()
