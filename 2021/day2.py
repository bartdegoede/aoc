def part1(data):
    horizontal = 0
    vertical = 0

    for instruction, distance in data:
        if instruction == 'forward':
            horizontal += distance
        elif instruction == 'down':
            vertical += distance
        elif instruction == 'up':
            vertical -= distance

    return horizontal * vertical

def part2(data):
    aim = 0
    horizontal = 0
    depth = 0

    for instruction, distance in data:
        if instruction == 'forward':
            horizontal += distance
            depth += aim * distance
        elif instruction == 'down':
            aim += distance
        elif instruction == 'up':
            aim -= distance

    return horizontal * depth

if __name__ == '__main__':
    with open('day2.txt') as f:
        data = []
        for d in f.readlines():
            instruction, distance = d.strip().split()
            data.append((instruction, int(distance)))

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
