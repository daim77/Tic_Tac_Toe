import tkinter as tk
import numpy as np


def create_board():
    board = np.full((5, 5), 'Y')
    return board


def game_gui(board):
    window = tk.Tk()

    window.title('Tic Tac Toe')

    for i in range(5):
        for j in range(5):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1,
                height=500,
                width=500
            )
            frame.grid(row=i, column=j)
            button = tk.Button(master=frame, text=board[i][j])
            button.pack()

    window.mainloop()


board = create_board()
game_gui(board)
