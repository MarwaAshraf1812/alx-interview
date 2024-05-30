#!/usr/bin/python3
'''
Module 0-nqueens
A program that solves the N queens problem
'''
import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    sys.exit(1)
if N < 4:
    print('N must be at least 4')
    sys.exit(1)


def solveNQueens(n):
    """Solution for n queens"""
    col = set()
    pos = set()
    neg = set()

    final_results = []

    board = [[] for n in range(n)]  # create empy board

    def solve(row):
        """function for recursion"""
        # means we've reached the last row
        if row == n:
            # get copy of current solution(current board)
            final_results.append(board.copy())
            return

        # for every column
        for i in range(n):
            # if we find that the column or diagonals are used, then skip
            if i in col or (row + i) in pos or (row - i) in neg:
                continue

            # register found columns and diagonals
            col.add(i)
            pos.add(row + i)
            neg.add(row - i)

            board[row] = [row, i]

            # move to next row
            solve(row + 1)

            # finally undo
            col.remove(i)
            pos.remove(row + i)
            neg.remove(row - i)
            board[row] = []

    solve(0)

    return final_results


if __name__ == '__main__':
    result_boards = solveNQueens(N)
    for board in result_boards:
        print(board)
