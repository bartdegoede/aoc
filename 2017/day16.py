def spin(programs, size):
    partition = len(programs) - size
    spinning_programs = programs[partition:]
    non_spinning_programs = programs[:partition]
    return spinning_programs + non_spinning_programs


def exchange(programs, a, b):
    program_a = programs[a]
    program_b = programs[b]
    programs = programs[:a] + program_b + programs[a + 1:]
    programs = programs[:b] + program_a + programs[b + 1:]
    return programs


def partner(programs, a, b):
    position_a = programs.index(a)
    position_b = programs.index(b)
    return exchange(programs, position_a, position_b)


def dance(programs, instructions, repetitions=1):
    seen = []
    for i in xrange(repetitions):
        if programs in seen:
            return seen[repetitions % i]
        seen.append(programs)
        for instruction in instructions:
            if instruction.startswith('s'):
                programs = spin(programs, int(instruction[1:]))
            elif instruction.startswith('x'):
                a, b = instruction[1:].split('/')
                programs = exchange(programs, int(a), int(b))
            elif instruction.startswith('p'):
                a, b = instruction[1:].split('/')
                programs = partner(programs, a, b)

    return programs


if __name__ == '__main__':
    with open('day16.txt', 'r') as f:
        instructions = f.read().split(',')
    print 'Part 1:', dance('abcdefghijklmnop', instructions)
    print 'Part 2:', dance('abcdefghijklmnop', instructions, repetitions=1000000000)
