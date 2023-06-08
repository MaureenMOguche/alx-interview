#!/usr/bin/python3
from sys import argv, exit
"""Tis the the documentation for core algorithm solution on NQueen"""


def solveNQueens(n):
    """Program that solves the N queens problem"""
    res = []
    queens = [-1] * n

    def dfs(index):
        """Recursively resolves the N queens problem"""
        if index == len(queens):
            res.append(queens[:])
            return
        for i in range(len(queens)):
            queens[index] = i
            if valid(index):
                dfs(index + 1)

    def valid(n):
        """Method that checks if a position in the board is valid"""
        for i in range(n):
            if abs(queens[i] - queens[n]) == n - i:  # same diagonal
                return False
            if queens[i] == queens[n]:  # same column
                return False
        return True

    def make_all_boards(res):
        """Method that builts the List that be returned"""
        actual_boards = []
        for queens in res:
            board = []
            for row, col in enumerate(queens):
                board.append([row, col])
            actual_boards.append(board)
        return actual_boards

    dfs(0)
    return make_all_boards(res)


if __name__ == "__main__":
    if len(argv) < 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)
    else:
        result = solveNQueens(n)
        for row in result:
            print(row)
