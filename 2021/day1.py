def part1(data):
    i = 0
    j = 1
    increases = 0

    while j < len(data):
        if data[j] > data[i]:
            increases += 1
        i += 1
        j += 1

    return increases

def part2(data):
    i = 1
    j = 4

    current_sum = sum(data[0:3])
    increases = 0

    while j < len(data) + 1:
        if sum(data[i:j]) > current_sum:
            increases += 1
        current_sum = sum(data[i:j])
        i += 1
        j += 1

    return increases

if __name__ == '__main__':
    with open('day1.txt', 'r') as f:
        data = [int(d.strip()) for d in f.readlines()]

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
