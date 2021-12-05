class Board(object):
    def __init__(self, data):
        self.init_board(data)
        self.has_won = False

    def init_board(self, data):
        self.board = []
        for row in data.strip().split('\n'):
            self.board.append([int(x) for x in row.split()])

    def __repr__(self):
        matrix = '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board])
        return f'Board: \n{matrix}'

    def check_value(self, number):
        for i, row in enumerate(self.board):
            if number in row:
                self.board[i][row.index(number)] = -1

    def is_winning(self):
        for row in self.board:
            if all(n == -1 for n in row):
                self.has_won = True
                return True
        for i in range(len(self.board[0])):
            if all(n == -1 for n in [row[i] for row in self.board]):
                self.has_won = True
                return True
        return False

    def board_value(self):
        return sum([num for row in self.board for num in row if num != -1])

if __name__ == '__main__':
    with open('day4.txt', 'r') as f:
        data = f.read().split('\n\n')

    numbers, boards = data[0], data[1:]

    numbers = [int(x) for x in numbers.split(',')]
    boards = [Board(board) for board in boards]

    rank = 0
    for number in numbers:
        for board in boards:
            if not board.has_won:
                board.check_value(number)
                if board.is_winning():
                    rank += 1
                    if rank == 1:
                        print(f'Part 1: {number} x {board.board_value()} = {number * board.board_value()}')
                    if rank == 100:
                        print(f'Part 2: {number} x {board.board_value()} = {number * board.board_value()}')
