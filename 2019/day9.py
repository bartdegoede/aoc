from time import time

class Computer:
    def __init__(self, instructions, input=input, print=print):
        if isinstance(instructions, str):
            instructions = list(map(int, instructions.strip().split(",")))
        self.memory = instructions + [0] * 1024
        self.ip = 0
        self.baseptr = 0
        self.input = input
        self.print = print
        self.halted = True
        self.steps = 0

    def __getitem__(self, item) -> int:
        return self.memory[item]

    def __setitem__(self, key, value):
        self.memory[key] = value

    def get_pointer(self, mode, value) -> int:
        if mode == 0:
            return self[value]
        elif mode == 1:
            return value
        elif mode == 2:
            return self.baseptr + self[value]

    @staticmethod
    def get_modes(modes):
        return [int(x) for x in reversed(str(modes).zfill(3))]

    def read_opcode(self):
        code = self[self.ip]
        modes, op = divmod(code, 100)
        parameter_pointers = [self.get_pointer(mode, self.ip+x) for x, mode in enumerate(self.get_modes(modes), 1)]
        return op, parameter_pointers

    def step(self):
        self.steps += 1
        opcode, parameters = self.read_opcode()
        p1, p2, p3 = parameters
        if opcode == 1:  # Add
            self[p3] = self[p1] + self[p2]
            self.ip += 4
        elif opcode == 2:  # Multiply
            self[p3] = self[p1] * self[p2]
            self.ip += 4
        elif opcode == 3:  # Input
            self[p1] = int(self.input())
            self.ip += 2
        elif opcode == 4:  # Output
            self.print(self[p1])
            self.ip += 2
        elif opcode == 5:  # Jump if True
            if self[p1]:
                self.ip = self[p2]
            else:
                self.ip += 3
        elif opcode == 6:  # Jump if True
            if not self[p1]:
                self.ip = self[p2]
            else:
                self.ip += 3
        elif opcode == 7:  # Less than
            self[p3] = int(self[p1] < self[p2])
            self.ip += 4
        elif opcode == 8:  # Equal
            self[p3] = int(self[p1] == self[p2])
            self.ip += 4
        elif opcode == 9:
            self.baseptr += self[p1]
            self.ip += 2
        elif opcode == 99:
            self.halted = True
        else:
            raise RuntimeError(f"Unknown opcode {opcode}")

    def run(self):
        self.halted = False
        while not self.halted:
            self.step()


if __name__ == '__main__':
    with open('day9.txt', 'r') as f:
        data = f.read().strip().split(',')

    program = list(map(int, data))
    for part in range(1,3):
        start = time()
        computer = Computer(program, input=[part].pop)
        computer.run()
        end = time()
        print((end-start))
