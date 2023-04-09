class Game:
    def __init__(self):
        # a list that represents 9 slots for 3x3 game board
        self.board = [' ' for _ in range(9)]
        # if there's a current winner, who is it?
        self.current_winner = None

    def print_board(self):
        # list_name[2:] = returns all items starting from index 2
        # list_name[2:4] = returns all items from index 2 upto index 4 (meaning excluding 4)
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            #   [
            #     0 1 2
            #     3 4 5
            #     6 7 8
            #   ] a 2D list
            print('| ' + '| '.join(row) + '|')

    @staticmethod
    # is not possessed by any instances of a certain class
    def print_board_nums():
        numbers = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numbers:
            print('| ' + '| '.join(row) + '|')


    print_board_nums()