import re

def addr(register, a, b, c):
    register[c] = register[a] + register[b]

def addi(register, a, b, c):
    register[c] = register[a] + b

def mulr(register, a, b, c):
    register[c] = register[a] * register[b]

def muli(register, a, b, c):
    register[c] = register[a] * b

def banr(register, a, b, c):
    register[c] = register[a] & register[b]

def bani(register, a, b, c):
    register[c] = register[a] & b

def borr(register, a, b, c):
    register[c] = register[a] | register[b]

def bori(register, a, b, c):
    register[c] = register[a] | b

def setr(register, a, b, c):
    register[c] = register[a]

def seti(register, a, b, c):
    register[c] = a

def gtir(register, a, b, c):
    register[c] = int(a > register[b])

def gtri(register, a, b, c):
    register[c] = int(register[a] > b)

def gtrr(register, a, b, c):
    register[c] = int(register[a] > register[b])

def eqir(register, a, b, c):
    register[c] = int(a == register[b])

def eqri(register, a, b, c):
    register[c] = int(register[a] == b)

def eqrr(register, a, b, c):
    register[c] = int(register[a] == register[b])

FUNCTIONS = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir,
             gtri, gtrr, eqir, eqri, eqrr]

def parse(line):
    return list(map(int, re.findall(r'\d+', line)))


def behaves_like(instruction, before, after):
    c = 0
    for f in FUNCTIONS:
        # before is already a list, but we want to forcibly create a new
        # object
        register = list(before)
        f(register, *instruction[1:])
        if register == after:
            # this could be the operation you're looking for
            c += 1
    return c


def discard_candidates(instruction, before, after, candidates):
    for f in FUNCTIONS:
        register = list(before)
        f(register, *instruction[1:])
        if register != after:
            candidates[instruction[0]].discard(f)


if __name__ == '__main__':
    with open('day16.txt', 'r') as f:
        instructions = f.read().splitlines()

    c = 0
    for line in instructions:
        if line.startswith('Before'):
            before = parse(line)
        elif line.startswith('After'):
            after = parse(line)
            if behaves_like(instruction, before, after) >= 3:
                c += 1
        else:
            instruction = parse(line)

    print(f'{c} samples behave like three or more opcodes')

    opcodes = {}
    known = set()
    i = 0

    while len(known) < len(FUNCTIONS):
        # candidates are the set of all functions minus the set of functions
        # we already know
        candidates = {}
        for i in range(len(FUNCTIONS)):
            candidates[i] = set(FUNCTIONS) - set(known)

        for line in instructions:
            if line.startswith('Before'):
                before = parse(line)
            elif line.startswith('After'):
                after = parse(line)
                discard_candidates(instruction, before, after, candidates)
            else:
                instruction = parse(line)

        for i in range(len(FUNCTIONS)):
            if len(candidates[i]) == 1:
                f = candidates[i].pop()
                opcodes[i] = f
                known.add(f)
        i += 1
    print(f'Needed {i} iterations to find all opcodes')

    register = [0, 0, 0, 0]
    # found line 3237 manually
    for line in instructions[3237:]:
        if line:
            opcode, a, b, c = parse(line)
            f = opcodes[opcode]
            f(register, a, b, c)
    print(f'Value of register 0: {register[0]}')
