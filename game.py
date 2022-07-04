class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # we have sign each space in rage to rep 3x3 board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + ' |')

    @staticmethod
    def print_board_number(self):
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + ' |')

    def available_moves(self):
        moves = []
        for i, x in enumerate(self.board):
            # ['x', 'y', 'c'] => [(0, 'x'), (1, 'y') ... ]
            return [i for i, spot in enumerate(self.board) if spot == " "]
