import tkinter as tk


def available_spots():
    h = []
    for i in range(3):
        for j in range(3):
            if board[i][j]['text'] == '':
                h.append((i, j))
    return h


def check_win():
    for i in range(3):
        if board[i][0]['text'] == board[i][1]['text'] == board[i][2]['text'] != '':
            return 1
    for j in range(3):
        if board[0][j]['text'] == board[1][j]['text'] == board[2][j]['text'] != '':
            return 1
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != '':
        return 1
    elif board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != '':
        return 1
    elif available_spots() == []:
        return 0
    else:
        return -1

player = 'O'


def main_gameflow(r,c):
    global player
    print(r, c)
    if board[r][c]['text'] == '' and check_win() == -1:
        if player == 'O':
            board[r][c].config(text='O')
            if check_win() == -1:
                player = 'X'
                label_1.config(text=("It's X's turn"))
            elif check_win() == 1:
                label_1.config(text=("O win"))
            elif check_win() == 0:
                label_1.config(text="Draw!")
        elif player == 'X':
            board[r][c].config(text='X')
            if check_win() == -1:
                player = 'O'
                label_1.config(text=("It's O's turn"))
            elif check_win() == 1:
                label_1.config(text=("X win"))
            elif check_win() == 0:
                label_1.config(text="Draw!")


window_1 = tk.Tk()
window_1.title('Tic Tac Toe')

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        board[i][j] = tk.Button(
            text='',
            font=('normal', 60, 'normal'),
            width=5, height=3,
            command=lambda r=i, c=j: main_gameflow(r, c)
        )
        board[i][j].grid(row=i, column=j)

label_1=tk.Label(text="It's O's turn", font=('normal',22,'bold'))
label_1.grid(row=3, column=1)

window_1.mainloop()
