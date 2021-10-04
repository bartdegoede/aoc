import re

GRID_SIZE = 600

class Point:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy


def image(points, t):
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    for point in points:
        grid[int(point.y + GRID_SIZE/2)][int(point.x + GRID_SIZE/2)] = 1

    with open(f'./day10/{t}.pbm', 'w') as f:
        f.write('P1\n')
        f.write(f'{GRID_SIZE} {GRID_SIZE}\n')
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                f.write(f'{grid[row][column]}')
            f.write('\n')


if __name__ == '__main__':
    with open('day10.txt', 'r') as f:
        data = f.read().strip().split('\n')

    positions = []
    for position in data:
        positions.append(Point(*map(int, re.findall(r'-?\d+', position))))

    for t in range(1, 12000):
        in_range = True
        for pt in positions:
            pt.x += pt.vx
            pt.y += pt.vy

        for pt in positions:
            if not(pt.x > -GRID_SIZE/2 and pt.x < GRID_SIZE/2 and pt.y >-GRID_SIZE/2 and pt.y < GRID_SIZE/2):
                in_range = False
                break

        if in_range:
            print('in range at time', t)
            image(positions, t)
