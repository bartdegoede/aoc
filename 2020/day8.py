with open('day8.txt', 'r') as f:
    instructions = [line.strip() for line in f.readlines()]

def run_program(instructions):
    accumulator = 0
    position = 0
    seen_instructions = set([])

    while position < len(instructions):
        if position in seen_instructions:
            # the program never finishes, because we're running a previous instruction
            return accumulator, position
        seen_instructions.add(position)
        instruction, value = instructions[position].split()
        value = int(value)

        if instruction == 'acc':
            accumulator += value
        elif instruction == 'jmp':
            position += value
            continue
        position += 1
    # it ran to completion!
    return accumulator, None

print(f'The value of the accumulator is {run_program(instructions)[0]}')

for i in range(len(instructions)):
    # make a copy so we can modify the program and test it
    program = instructions.copy()
    end = 0
    if 'nop' in instructions[i]:
        program[i] = instructions[i].replace('nop', 'jmp')
        result, end = run_program(program)
    elif 'jmp' in instructions[i]:
        program[i] = instructions[i].replace('jmp', 'nop')
        result, end = run_program(program)
    if end is None:
        break

print(f'The value of the accumulator is {result}')
