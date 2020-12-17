from collections import defaultdict

with open('day17.txt', 'r') as f:
    rows = [line.strip() for line in f.readlines()]

cubes = defaultdict(bool)
cubes4d = defaultdict(bool)

for row_idx, row in enumerate(rows):
    for column_idx, state in enumerate(row):
        if state == '#':
            cubes[(row_idx, column_idx, 0)] = True

for row_idx, row in enumerate(rows):
    for column_idx, state in enumerate(row):
        if state == '#':
            cubes4d[(row_idx, column_idx, 0, 0)] = True


def find_neighbors(cube):
    x, y, z = cube
    neighbors = []
    for dx in range(x-1, x+2):
        for dy in range(y-1, y+2):
            for dz in range(z-1, z+2):
                # the cube itself is not a neighbor, you dumbass
                if not (dx == x and dy == y and dz == z):
                    neighbors.append((dx, dy, dz))
    return neighbors


def find_4d_neighbors(cube):
    x, y, z, w = cube
    neighbors = []
    for dx in range(x-1, x+2):
        for dy in range(y-1, y+2):
            for dz in range(z-1, z+2):
                for dw in range(w-1, w+2):
                    if not (dx == x and dy == y and dz == z and dw == w):
                        neighbors.append((dx, dy, dz, dw))
    return neighbors


def active_neighbors(cube, cubes, cubes_are_4d=False):
    if cubes_are_4d:
        neighbors = find_4d_neighbors(cube)
    else:
        neighbors = find_neighbors(cube)
    return sum([cubes.get(neighbor, False) for neighbor in neighbors])


def simulate(cubes, cubes_are_4d=False):
    new_cubes = defaultdict(bool)
    for cube in cubes:
        active_neighbor_count = active_neighbors(cube, cubes, cubes_are_4d)
        if cubes[cube]:
            if active_neighbor_count == 2 or active_neighbor_count == 3:
                new_cubes[cube] = True
            if cubes_are_4d:
                neighbors = find_4d_neighbors(cube)
            else:
                neighbors = find_neighbors(cube)
            for neighbor in neighbors:
                if not cubes.get(neighbor, False) and active_neighbors(neighbor, cubes, cubes_are_4d) == 3:
                    new_cubes[neighbor] = True
        else:
            if active_neighbor_count == 3:
                new_cubes[cube] = True
    return new_cubes

for _ in range(6):
    cubes = simulate(cubes)
    cubes4d = simulate(cubes4d, True)

print(f'There are {sum([v for v in cubes.values()])} active cubes')
print(f'There are {sum([v for v in cubes4d.values()])} 4d active cubes')
