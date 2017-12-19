class Packet(object):
    def __init__(self, diagram):
        self.diagram = diagram

        self.x = self.diagram[0].index('|')
        self.y = 0
        self.direction = 'D'
        self.steps = {
            'D': self.down,
            'U': self.up,
            'L': self.left,
            'R': self.right
        }

        self.letters = []
        self.done = False

    def step(self):
        self.steps[self.direction]()
        val = self.diagram[self.y][self.x]
        if val == ' ':
            self.done = True
        if val == '+':
            self.change_direction()
        if val not in ['|', '-', '+', ' ']:
            self.letters.append(val)

    def change_direction(self):
        if self.direction in ['L', 'R']:
            # look up or down
            self.direction = 'U'
            if self.diagram[self.y + 1][self.x] == '|':
                self.direction = 'D'
        elif self.direction in ['U', 'D']:
            # look left or right
            self.direction = 'L'
            if self.diagram[self.y][self.x + 1] == '-':
                self.direction = 'R'

    def down(self):
        self.y += 1

    def up(self):
        self.y -= 1

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

    def __repr__(self):
        return 'Packet <{}, {}>'.format(self.x, self.y)

if __name__ == '__main__':
    with open('day19.txt', 'r') as f:
        diagram = f.read().split('\n')[:-1]

    packet = Packet(diagram)
    counter = 0
    while packet.done == False:
        packet.step()
    print 'Part 1:', ''.join(packet.letters)
