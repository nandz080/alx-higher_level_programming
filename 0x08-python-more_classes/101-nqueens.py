#!/usr/bin/python3

import sys

def is_safe(board, row, col):
    # Check if it is safe to place a queen at the given position
    # in the current board configuration
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, n, solutions):
    # Base case: If all queens are placed, add the solution to the list
    if row == n:
        solutions.append(list(board))
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

def nqueens(N):
    # Check if N is a valid integer
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty board
    board = [-1] * N

    # Solve the N queens problem
    solutions = []
    solve_nqueens(board, 0, N, solutions)

    # Print the solutions
    print_solutions(solutions)

# Main program
if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command-line argument
    N = sys.argv[1]

    # Solve the N queens problem
    nqueens(N)
