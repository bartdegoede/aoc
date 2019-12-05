def parameter(program, i, pos, modes):
    if modes[pos-1] == 1:
        return program[i+pos]
    return program[program[i+pos]]

def intcode(program, inp):
    i = 0
    outputs = []
    while i < len(program):
        opcode = program[i]
        modes = []

        if opcode > 100:
            opcode_mode = int(opcode / 100)
            opcode = opcode % 100
            while opcode_mode > 0:
                modes.append(opcode_mode % 10)
                opcode_mode //= 10
        # pad with zeroes for ease of use
        while len(modes) < 4:
            modes.append(0)

        if opcode == 99:
            return outputs[-1]
        elif opcode == 1:
            first = parameter(program, i, 1, modes)
            second = parameter(program, i, 2, modes)
            program[program[i+3]] = first + second
            i += 4
        elif opcode == 2:
            first = parameter(program, i, 1, modes)
            second = parameter(program, i, 2, modes)
            program[program[i+3]] = first * second
            i += 4
        elif opcode == 3:
            program[program[i+1]] = inp
            i += 2
        elif opcode == 4:
            outputs.append(parameter(program, i, 1, modes))
            i += 2
        elif opcode == 5:
            param = parameter(program, i, 1, modes)
            address = parameter(program, i, 2, modes)
            if param != 0:
                i = address
            else:
                i += 3
        elif opcode == 6:
            param = parameter(program, i, 1, modes)
            address = parameter(program, i, 2, modes)
            if param == 0:
                i = address
            else:
                i += 3
        elif opcode == 7:
            first = parameter(program, i, 1, modes)
            second = parameter(program, i, 2, modes)
            program[program[i+3]] = int(first < second)
            i += 4
        elif opcode == 8:
            first = parameter(program, i, 1, modes)
            second = parameter(program, i, 2, modes)
            program[program[i+3]] = int(first == second)
            i += 4
        else:
            print(f'Something went wrong: opcode {opcode}')
            break

if __name__ == '__main__':
    with open('day5.txt', 'r') as f:
        data = f.read().strip().split(',')
    program = list(map(int, data))
    print(f'Part 1: {intcode(program, 1)}')
    program = list(map(int, data))
    print(f'Part 2: {intcode(program, 5)}')
