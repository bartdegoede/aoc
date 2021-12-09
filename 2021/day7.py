import functools
from statistics import median

@functools.cache
def fuel(distance):
    return distance * (distance + 1) // 2

if __name__ == '__main__':
    with open('day7.txt', 'r') as f:
        data = list(map(int, f.read().strip().split(',')))

    sorted_positions = sorted(data)
    positions_median = median(sorted_positions)
    print(f'Part 1: {int(sum(abs(pos - positions_median) for pos in sorted_positions))}')

    max_position = sorted_positions[-1]
    results = []
    for i in range(max_position):
        total_fuel = sum(fuel(abs(position - i)) for position in sorted_positions)
        results.append(total_fuel)

    print(f'Part 2: {min(results)}')
