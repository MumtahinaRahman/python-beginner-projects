class Game:
    def __init__(self):
        # a list that represents 9 slots for game board
        self.board = [range(9)]
        # if there's a current winner, who is it?
        self.current_winner = None

    def print_board(self):
        pass