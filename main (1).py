import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # single list to represent 3x3 board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # top-left to bottom-right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # top-right to bottom-left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def minimax(position, depth, max_player, game):
    if max_player:
        max_eval = -math.inf
        best_move = None
        for move in game.available_moves():
            game.make_move(move, 'O')
            eval = minimax(position - 1, depth + 1, False, game)
            game.board[move] = ' '
            max_eval = max(max_eval, eval)
            if max_eval == eval:
                best_move = move
        return max_eval if depth == 0 else best_move
    else:
        min_eval = math.inf
        for move in game.available_moves():
            game.make_move(move, 'X')
            eval = minimax(position - 1, depth + 1, True, game)
            game.board[move] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def get_computer_move(game):
    if len(game.available_moves()) == 9:
        return random.choice(game.available_moves())
    else:
        return minimax(game.num_empty_squares(), 0, True, game)

def play():
    game = TicTacToe()
    print("Welcome to Tic Tac Toe!")
    game.print_board_nums()
    print("To make a move, enter a number from 0-8, corresponding to the board position as shown.")

    while game.empty_squares():
        if game.current_winner is None:
            if game.num_empty_squares() == 1:
                move = game.available_moves()[0]
            else:
                move = get_computer_move(game)

            game.make_move(move, 'O')

            if game.current_winner:
                break
            game.print_board()
            print()

            player_move = None
            while player_move not in game.available_moves():
                try:
                    player_move = int(input("Enter your move (0-8): "))
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 8.")
                    continue

            game.make_move(player_move, 'X')

    game.print_board()
    if game.current_winner == 'O':
        print("Sorry, you lose!")
    elif game.current_winner == 'X':
        print("Congratulations, you win!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play()
