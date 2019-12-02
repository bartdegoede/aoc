import math

def fuel(mass):
    return math.floor(int(mass) / 3) - 2


if __name__ == '__main__':
    with open('day1.txt', 'r') as f:
        total = sum([fuel(line) for line in f])
        print(f'Part 1: {total}')

        f.seek(0)
        total = 0
        for line in f:
            fuel_for_component = fuel(line)
            total += fuel_for_component
            fuel_for_component = fuel(fuel_for_component)
            while fuel_for_component > 0:
                total += fuel_for_component
                fuel_for_component = fuel(fuel_for_component)
        print(f'Part 2: {total}')
