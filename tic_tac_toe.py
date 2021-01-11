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

test_board = [
    [1, 0, 4, 0, 0],
    [0, 1, 0, 4, 0],
    [3, 5, 1, 0, 10],
    [0, 3, 5, 2, 0],
    [0, 0, 3, 5, 2]
]

board = np.zeros(25)
board = board.reshape(5, 5)

print(board)
print(np.diag(test_board, k=2))
print(np.rot90(test_board))
