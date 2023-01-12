"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_c = 0
    o_c = 0
    for i in board:
        x_c += i.count(X)
        o_c += i.count(O)
    if o_c >= x_c:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                t = (i, j)
                moves.add(t)
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    p = player(board)
    new = deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            t = i, j
            if t == action:
                new[i][j] = p
    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Horizontal check
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]

    # Vertical
    elif board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]

    # Diagonal
    elif board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if len(actions(board)) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # We'll use X as the maximizing player and O as minimizing
    best_action = None
    if player(board) == X:
        value = -float("inf")
        for action in actions(board):
            maxi = maximizer(result(board, action))
            if maxi > value:
                best_action = action
                value = maxi
    else:
        value = float("inf")
        for action in actions(board):
            mini = minimizer(result(board, action))
            if mini < value:
                best_action = action
                value = mini
    return best_action


def minimizer(board):
    if terminal(board):
        return utility(board)
    u = float("inf")
    for action in actions(board):
        u = min(u, maximizer(result(board, action)))
    return u


def maximizer(board):
    if terminal(board):
        return utility(board)
    u = -float("inf")
    for action in actions(board):
        u = max(u, minimizer(result(board, action)))
    return u
