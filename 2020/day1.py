from functools import reduce
from itertools import permutations

with open('day1.txt', 'r') as f:
    expenses = list(map(int, f.readlines()))

def solve(expenses, r=2):
    for pair in permutations(expenses, r):
        if sum(pair) == 2020:
            return f'{pair} sums to 2020: {reduce(lambda x, y: x * y, pair)}'

print(f'Solution 1: {solve(expenses, 2)}')
print(f'Solution 1: {solve(expenses, 3)}')
