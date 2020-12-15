numbers = [12, 1, 16, 3, 11, 0]

def solve(numbers, max_turn):
    seen = {previous: i+1 for i, previous in enumerate(numbers)}
    last = numbers[-1]
    for turn in range(len(numbers) + 1, max_turn + 1):
        current = 0
        if last in seen:
            current = turn - 1 - seen[last]
        seen[last] = turn - 1
        last = current
    return current

print(f'The 2020th number spoken is {solve([12, 1, 16, 3, 11, 0], 2020)}')
print(f'The 30000000th number spoken is {solve([12, 1, 16, 3, 11, 0], 30000000)}')
