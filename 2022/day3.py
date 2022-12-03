with open('day3.txt', 'r') as f:
    backpacks = f.read().strip().split('\n')

priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority_sum = 0

for backpack in backpacks:
    mid = len(backpack) // 2
    compartment1, compartment2 = set(backpack[:mid]), set(backpack[mid:])
    in_common = list(compartment1.intersection(compartment2))[0]
    priority_sum += priorities.index(in_common) + 1

print(f'Part 1: {priority_sum}')

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

priority_sum = 0

for group in chunker(backpacks, 3):
    elves = list(map(set, group))
    in_common = elves[0].intersection(*elves[1:])
    priority_sum += priorities.index(list(in_common)[0]) + 1

print(f'Part 2: {priority_sum}')
