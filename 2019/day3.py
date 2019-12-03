DIRECTIONS = {
    'U': lambda x, y: (x, y+1),
    'R': lambda x, y: (x+1, y),
    'D': lambda x, y: (x, y-1),
    'L': lambda x, y: (x-1, y)
}

def coordinates(wire):
    coords = {}
    position = (0, 0)
    length = 0

    for instruction in wire:
        direction = instruction[0]
        distance = int(instruction[1:])
        for _ in range(distance):
            position = DIRECTIONS[direction](*position)
            length += 1
            if position not in coords:
                coords[position] = length
    return coords


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == '__main__':
    with open('day3.txt', 'r') as f:
        instructions = f.readlines()
        wire1 = instructions[0].strip().split(',')
        wire2 = instructions[1].strip().split(',')

    wire1_coords = coordinates(wire1)
    wire2_coords = coordinates(wire2)

    distances = []
    steps = []
    for shared_coordinates in set(wire1_coords.keys()).intersection(set(wire2_coords.keys())):
        distances.append(manhattan_distance((0, 0), shared_coordinates))
        steps.append(wire1_coords[shared_coordinates] + wire2_coords[shared_coordinates])

    print(f'Part 1: {min(distances)}')
    print(f'Part 2: {min(steps)}')
