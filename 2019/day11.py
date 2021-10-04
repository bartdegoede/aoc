from day9 import Computer

class Robot(object):
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)

    LEFT_TURN = {
        UP: LEFT,
        LEFT: DOWN,
        DOWN: RIGHT,
        RIGHT: UP
    }

    RIGHT_TURN = {
        UP: RIGHT,
        RIGHT: DOWN,
        DOWN: LEFT,
        LEFT: UP
    }

    def __init__(self, computer):
        self.program = program
        self.position = (0, 0)
        self.direction = self.UP

    def step(self):
        pass


if __name__ == '__main__':
    with open('day11.txt', 'r') as f:
        data = f.read().strip().split(',')

    program = list(map(int, data))
    computer = Computer(program, input=lambda: 0)
