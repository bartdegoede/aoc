from collections import deque
import math

def get_neighbours(x, y, grid):
    neighbours = []
    for dx, dy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if (dx, dy) in grid and (dx, dy) != (x, y):
            neighbours.append((dx, dy))
    return neighbours

def bfs(grid, point):
    queue = deque([point])
    visited = set([point])
    while queue:
        x, y = queue.popleft()
        for dx, dy in get_neighbours(x, y, grid):
            if (dx, dy) not in visited and grid[(dx, dy)] < 9:
                visited.add((dx, dy))
                queue.append((dx, dy))
    return visited

if __name__ == '__main__':
    with open('day9.txt', 'r') as f:
        data = f.read().strip().split('\n')

    grid = {}

    for y, row in enumerate(data):
        for x, height in enumerate(row):
            grid[(x, y)] = int(height)

    total_risk = 0
    lowest_points = []
    for y, row in enumerate(data):
        for x, height in enumerate(row):
            neighbours = get_neighbours(x, y, grid)
            higher_neighbors = 0
            height = int(height)
            for dx, dy in neighbours:
                if grid[(dx, dy)] > height:
                    higher_neighbors += 1

            if higher_neighbors == len(neighbours):
                lowest_points.append((x, y))
                total_risk += 1 + height

    print(f'Part 1: {total_risk}')

    basins = []
    for point in lowest_points:
        basins.append(len(bfs(grid, point)))

    print(f'Part 2: {math.prod(sorted(basins, reverse=True)[:3])}')
