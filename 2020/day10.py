from collections import defaultdict

with open('day10.txt', 'r') as f:
    adapters = sorted(list(map(int, f.readlines())))

joltage = 0
# add one 3 joltage built-in adapter
differences = defaultdict(int, {3: 1})
for adapter in adapters:
    differences[adapter - joltage] += 1
    joltage = adapter
print(f'The joltage difference is {differences[1] * differences[3]}')

combinations = defaultdict(int, {0: 1})
for adapter in adapters:
    combinations[adapter] = combinations[adapter-1] + combinations[adapter-2] + combinations[adapter-3]
print(f'There are {combinations[adapters[-1]]} different ways to arrange the adapters')
