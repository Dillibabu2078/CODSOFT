class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] 
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
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
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def minimax(game, maximizing):
    case = game.current_winner
    if case == 'O':
        return 1, None
    elif case == 'X':
        return -1, None
    elif not game.empty_squares():
        return 0, None

    if maximizing:
        max_eval = float('-inf')
        best_move = None
        for move in game.available_moves():
            game.make_move(move, 'O')
            evaluation, _ = minimax(game, False)
            game.board[move] = ' '
            game.current_winner = None
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in game.available_moves():
            game.make_move(move, 'X')
            evaluation, _ = minimax(game, True)
            game.board[move] = ' '
            game.current_winner = None
            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move
        return min_eval, best_move

def play_game():
    game = TicTacToe()
    print("Welcome to Tic-Tac-Toe! The board positions are numbered as follows:")
    game.print_board_nums()
    
    while game.empty_squares():
        if game.num_empty_squares() % 2 == 1: 
            valid_square = False
            while not valid_square:
                square = input("X's turn. Input move (0-8): ")
                try:
                    square = int(square)
                    if square not in game.available_moves():
                        raise ValueError
                    valid_square = True
                except ValueError:
                    print("Invalid square. Try again.")
            
            game.make_move(square, 'X')
        else:  
            print("O's turn (AI)")
            _, move = minimax(game, True)
            game.make_move(move, 'O')
        
        print("\nCurrent board:")
        game.print_board()
        print()  
        
        if game.current_winner:
            print(f"{game.current_winner} wins!")
            return
    
    print("It's a tie!")

if __name__ == '__main__':
    play_game()
