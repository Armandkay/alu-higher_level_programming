#!/usr/bin/python3
import sys

def print_solution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def nqueens(n):
    def can_place(pos, board):
        for i in range(pos[0]):
            if board[i][pos[1]] == 1:
                return False
        for i, j in zip(range(pos[0], -1, -1), range(pos[1], -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(pos[0], n, 1), range(pos[1], -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(board, queens):
        if queens == 0:
            print_solution(board)
            print()
            return
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    board[i][j] = 1
                    if can_place((i, j), board):
                        solve(board, queens - 1)
                    board[i][j] = 0

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(N)
