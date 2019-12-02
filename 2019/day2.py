def intcode(program):
    i = 0
    while i < len(program):
        if program[i] == 99:
            break
        elif program[i] == 1:
            val = program[program[i+1]] + program[program[i+2]]
        elif program[i] == 2:
            val = program[program[i+1]] * program[program[i+2]]
        else:
            print(f'Something went wrong: opcode {program[i]}')
            break
        program[program[i+3]] = val
        i += 4
    return program

if __name__ == '__main__':
    with open('day2.txt', 'r') as f:
        data = f.read().split(',')
    program = list(map(int, data))
    program[1] = 12
    program[2] = 2
    print(f'Part 1: {intcode(program)[0]}')

    # bruteforce all the things
    for i in range(0, 100):
        for j in range(0, 100):
            # reset
            program = list(map(int, data))
            program[1] = i
            program[2] = j
            if intcode(program)[0] == 19690720:
                print(f'Part 2: {100 * i + j}')
