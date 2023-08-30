import math
import random


# The Tic-Tac-Toe board is represented as a 2D list (3x3)
# where 'X' represents the AI player, 'O' represents the human player,
# and None represents an empty cell.

# Function to display the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("  | ".join(cell if cell is not None else " " for cell in row))
        print("-" * 13)
    print('===============')
print("Welcome to the Tic Tac Toe Game!")

# Function to check if the board is full
def is_board_full(board):
    return all(all(cell is not None for cell in row) for row in board)

# Function to check if the game is over and return the winner
def evaluate_board(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    # Check if the board is full (draw)
    if is_board_full(board):
        return "DRAW"
    
    # Game is still ongoing
    return None

# Minimax function with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    # Base case: If the game is over or reached the maximum depth, return the evaluation
    result = evaluate_board(board)
    if result is not None:
        if result == "DRAW":
            return 0
        elif result == 'X':
            return 1
        elif result == 'O':
            return -1
    
    if is_maximizing:
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = None
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # Beta Pruning
        return max_eval
    else:
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = None
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # Alpha Pruning
        return min_eval

# Function to find the best move using the minimax algorithm
def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                board[row][col] = 'X'
                eval = minimax(board, 0, False, -math.inf, math.inf)
                board[row][col] = None
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move

# Main game loop
def play_game():
    board = [[None for _ in range(3)] for _ in range(3)]
    while True:
        # AI's turn
        print_board(board)
        if not is_board_full(board):
            ai_row, ai_col = find_best_move(board)
            board[ai_row][ai_col] = 'X'
        else:
            break
        
        # Check if AI wins or it's a draw
        result = evaluate_board(board)
        if result is not None:
            print_board(board)
            if result == "DRAW":
                print("It's a draw!")
            else:
                print("AI wins!")
            break
        
        # Human's turn
        print_board(board)
        if not is_board_full(board):
            while True:
                try:
                    row = int(input("Enter row (0, 1, 2): "))
                    col = int(input("Enter column (0, 1, 2): "))
                    if board[row][col] is None:
                        board[row][col] = 'O'
                        break
                    else:
                        print("Cell is already taken!")
                except (ValueError, IndexError):
                    print("Invalid input. Please try again.")
        else:
            break

        # Check if human wins or it's a draw
        result = evaluate_board(board)
        if result is not None:
            print_board(board)
            if result == "DRAW":
                print("It's a draw!")
            else:
                print("Human wins!")
            break

if __name__ == "__main__":
    play_game()