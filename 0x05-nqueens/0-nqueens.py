#!/usr/bin/python3
""""
0-nqueens.py
"""

from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except BaseException:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    sol = []

    def queens(row, n, sol):
        if row == n:
            print(sol)
        else:
            for col in range(n):
                place = [row, col]
                if valid_placement(sol, place):
                    sol.append(place)
                    queens(row + 1, n, sol)
                    sol.remove(place)

    def valid_placement(sol, place):
        for queen in sol:
            if queen[1] == place[1]:
                return False
            if queen[0] + queen[1] == place[0] + place[1]:
                return False
            if queen[0] - queen[1] == place[0] - place[1]:
                return False
        return True

    queens(0, n, sol)
