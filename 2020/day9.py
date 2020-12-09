from collections import deque
from itertools import permutations

with open('day9.txt', 'r') as f:
    numbers = list(map(int, f.readlines()))

def valid(number, preamble):
    valid_numbers = set([sum(pair) for pair in permutations(preamble, 2)])
    if number in valid_numbers:
        return True
    return False

preamble = deque(numbers[:25])
for number in numbers[25:]:
    if not valid(number, preamble):
        print(f'{number} is not valid!')
        break
    preamble.popleft()
    preamble.append(number)

for i in range(len(numbers)):
    j = i + 2
    while sum(numbers[i:j]) < number:
        j += 1
    if sum(numbers[i:j]) == number:
        print(f'The encryption weakness is {max(numbers[i:j]) + min(numbers[i:j])}')
        break
