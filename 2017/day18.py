from collections import defaultdict

class Registry(object):
    def __init__(self, instructions):
        self.current_instruction = 0
        self.instructions = instructions
        self.registers = defaultdict(lambda: 0)
        self.sound_last_played = 0

        self.operations = {
            'snd': self.snd,
            'set': self.set,
            'add': self.add,
            'mul': self.mul,
            'mod': self.mod,
            'rcv': self.rcv,
            'jgz': self.jgz
        }

    def run(self):
        while True:
            if self.current_instruction < 0 or self.current_instruction > len(self.instructions):
                break
            instruction = self.instructions[self.current_instruction].split()
            if len(instruction) == 3:
                try:
                    value = int(instruction[2])
                except ValueError:
                    value = self.registers[instruction[2]]
            operation = instruction[0]
            registry = instruction[1]
            self.operations[operation](registry, value)
            self.current_instruction += 1

    def snd(self, x, _):
        self.sound_last_played = self.registers[x]

    def set(self, x, y):
        self.registers[x] = y

    def add(self, x, y):
        self.registers[x] += y

    def mul(self, x, y):
        self.registers[x] *= y

    def mod(self, x, y):
        self.registers[x] %= y

    def rcv(self, x, _):
        if self.registers[x] != 0:
            self.current_instruction = len(self.instructions) + 1

    def jgz(self, x, y):
        # import ipdb; ipdb.set_trace()
        if self.registers[x] > 0:
            self.current_instruction += (y - 1)


if __name__ == '__main__':
    with open('day18.txt', 'r') as f:
        data = f.read().strip().split('\n')
    registry = Registry(data)
    registry.run()
    print 'Part 1:', registry.sound_last_played
