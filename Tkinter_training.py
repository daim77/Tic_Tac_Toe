import tkinter as tk
import numpy as np


def create_board():
    board = np.full((5, 5), 'X')
    return board


def game_gui(board):
    window = tk.Tk()

    for i in range(5):
        for j in range(5):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=board[i][j])
            label.pack()

    window.mainloop()


board = create_board()
game_gui(board)
