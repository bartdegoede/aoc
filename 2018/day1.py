import itertools

if __name__ == '__main__':
    with open('day1.txt', 'r') as f:
        instructions = f.read().strip().split('\n')

    frequency = sum([int(instruction) for instruction in instructions])
    print(f'Frequency is {frequency}')

    frequency = 0
    seen = set([0])
    for num in itertools.cycle(instructions):
        frequency += int(num)
        if frequency in seen:
            break
        seen.add(frequency)

    print(f'First frequency reached twice is {frequency}')
