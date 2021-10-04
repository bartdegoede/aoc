# from collections import deque
# import itertools

# def add(i, memory, mode0, mode1):
#     a, b, c = memory[i+1:i+4]
#     result = (a if mode0 else memory[a]) + (b if mode1 else memory[b])
#     return i+4, memory[:c] + (result,) + memory[c + 1:]

# def multiply(i, memory, mode0, mode1):
#     a, b, c = memory[i+1:i+4]
#     result = (a if mode0 else memory[a]) + (b if mode1 else memory[b])
#     return i+4, memory[:c] + (result,) + memory[c + 1:]

# def jump_if_true(i, memory, mode0, mode1):
#     a, b = memory[i+1:i+3]
#     a = a if mode0 else memory[a]
#     b = b if mode1 else memory[b]
#     return b if a != 0 else (i+3), memory

# def jump_if_false(i, memory, mode0, mode1):
#     a, b = memory[i+1:i+3]
#     a = a if mode0 else memory[a]
#     b = b if mode1 else memory[b]
#     return b if a == 0 else (i+3), memory

# def less_than(i, memory, mode0, mode1):
#     a, b, c = memory[i+1:i+4]
#     a = a if mode0 else memory[a]
#     b = b if mode1 else memory[b]
#     return i+4, memory[:c] + (1 if a < b else 0,) + memory[c+1:]

# def equals(i, memory, mode0, mode1):
#     a, b, c = memory[i+1:i+4]
#     a = a if mode0 else memory[a]
#     b = b if mode1 else memory[b]
#     return i+4, memory[:c] + (1 if a == b else 0,) + memory[c+1:]

# def intcode_operation(i, memory, inp, outp):
#     opcode = memory[i]
#     mode0 = opcode // 100 % 10 == 1
#     mode1 = opcode // 1000 % 10 == 1
#     opcode = opcode % 100

#     if opcode == 99:
#         # exit
#         return i, None
#     elif opcode == 1:
#         return add(i, memory, mode0, mode1)
#     elif opcode == 2:
#         return multiply(i, memory, mode0, mode1)
#     elif opcode == 3:
#         a = memory[i+1]
#         _inp = inp.popleft()
#         return i+2, memory[:a] + (_inp,) + memory[a+1:]
#     elif opcode == 4:
#         outp.append(memory[i+1])
#         return i+2, memory
#     elif opcode == 5:
#         return jump_if_true(i, memory, mode0, mode1)
#     elif opcode == 6:
#         return jump_if_false(i, memory, mode0, mode1)
#     elif opcode == 7:
#         return less_than(i, memory, mode0, mode1)
#     elif opcode == 8:
#         return equals(i, memory, mode0, mode1)
#     else:
#         raise Exception(f'Something went wrong: opcode {opcode}')

# def run_intcode(memory, phases):
#     program = memory
#     signal = 0
#     inp = deque()
#     outp = deque()
#     for phase in phases:
#         inp.append(phase)
#         inp.append(signal)
#         i = 0
#         while True:
#             i, program = intcode_operation(i, program, inp, outp)
#             if not program:
#                 break
#             signal = outp.popleft()
#     print(f'Thruster signal: {signal}')
#     return signal

# if __name__ == '__main__':
#     with open('day7.txt', 'r') as f:
#         data = f.read().strip().split(',')

#     memory = tuple(map(int, data))

#     outputs = []
#     for phases in itertools.permutations(range(5)):
#         amplification = 0
#         signal = run_intcode(memory, phases)
#         outputs.append(signal)

#     print(f'Part 1: {max(signal)}')
from itertools import permutations

from collections import deque


def step(idx, mem, input, output):
    op = mem[idx]
    if op == 99:
        # print('halt')
        return None

    im0 = op // 100 % 10 == 1
    im1 = op // 1000 % 10 == 1
    op = op % 100

    if op == 1:
        a, b, c = mem[idx + 1:idx + 4]
        r = (a if im0 else mem[a]) + (b if im1 else mem[b])
        return idx + 4, mem[:c] + (r,) + mem[c + 1:]
    elif op == 2:
        a, b, c = mem[idx + 1:idx + 4]
        r = (a if im0 else mem[a]) * (b if im1 else mem[b])
        return idx + 4, mem[:c] + (r,) + mem[c + 1:]
    elif op == 3:  # input
        a = mem[idx + 1]
        inp = input.popleft()
        # print('input', inp)
        return idx + 2, mem[:a] + (inp,) + mem[a + 1:]
    elif op == 4:
        a = mem[idx + 1]
        # print(f'out:{mem[a]}')
        output.append(mem[a])
        return idx + 2, mem
    elif op == 5:
        a, b = mem[idx + 1:idx + 3]
        a = a if im0 else mem[a]
        b = b if im1 else mem[b]
        return b if a != 0 else (idx + 3), mem
    elif op == 6:
        a, b = mem[idx + 1:idx + 3]
        a = a if im0 else mem[a]
        b = b if im1 else mem[b]
        return b if a == 0 else (idx + 3), mem
    elif op == 7:
        a, b, c = mem[idx + 1:idx + 4]
        a = a if im0 else mem[a]
        b = b if im1 else mem[b]
        return idx + 4, mem[:c] + (1 if a < b else 0,) + mem[c + 1:]
    elif op == 8:
        a, b, c = mem[idx + 1:idx + 4]
        a = a if im0 else mem[a]
        b = b if im1 else mem[b]
        return idx + 4, mem[:c] + (1 if a == b else 0,) + mem[c + 1:]
    else:
        raise Exception(f"invalid op: {op}")


def run(memory, phases):
    program = memory
    sig = 0
    input = deque()
    output = deque()
    for phase in phases:
        input.append(phase)
        input.append(sig)
        idx = 0
        while next := step(idx, program, input, output):
            idx, program = next

        sig = output.popleft()

    print(f'thruster signal: {sig}')
    return sig


# data = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
with open('day7.txt', 'r') as f:
    data = f.read().strip().split(',')
memory = tuple(int(m) for m in data)
mx = 0
for phases in permutations([0, 1, 2, 3, 4], 5):
    sig = run(memory, phases)
    mx = max(mx, sig)

print(f'part1 {mx}')
