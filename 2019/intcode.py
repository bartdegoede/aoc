class Computer(object):
    def __init__(self, memory, inputs):
        self.position = 0
        self.base = 0
        self.inputs = inputs
        self.outputs = []
        self.memory = {i: v for i, v in enumerate(memory)}
        self.running = True
        self.halt = False

    def run(self):
        p = self.position
        opcode, x, y, k = [self.memory.get(i, 0) for i in range(p, p + 4)]
        print(opcode, x, y, k)
        a, b, c, d, operation = [int(c) for c in str(opcode).rjust(5, '0')]

        m = self.get_param(c, x)
        n = self.get_param(b, y)
        o = self.get_param(a, k)

        if operation == 1:
            self.memory[o] = m + n
            self.position += 4
        if operation == 2:
            self.memory[o] = m * n
            self.position += 4
        if operation == 3:
            self.memory[o] = self.inputs.pop(0)
            self.position += 2
        if operation == 4:
            self.outputs.append(m)
            self.position += 2

            if len(self.outputs) == 2:
                self.running = False
        if operation == 5:
            self.position = n if m != 0 else self.position + 3
        if operation == 6:
            self.position = n if m == 0 else self.position + 3
        if operation == 7:
            self.memory[o] = 1 if m < n else 0
            self.position += 4
        if operation == 8:
            self.memory[o] = 1 if m == n else 0
            self.position += 4
        if operation == 9:
            if d == 9:
                self.halt = True
                self.running = False
            else:
                self.base += self.get_param(c, x)
                self.position += 2

    def get_param(self, mode, value):
        if mode == 0:
            return self.memory.get(value, 0)
        if mode == 1:
            return value
        if mode == 2:
            return self.memory[value + self.base]

    def set_param(self, mode, value):
        if mode == 2:
            return self.base + value
        return value
