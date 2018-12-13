import numpy as np

def power_level(x, y):
    rack_id = x + 10
    lvl = rack_id * y
    lvl += serial
    lvl *= rack_id
    lvl = (lvl // 100) % 10
    return lvl - 5

def area_power(x, y, grid):
    power = 0
    for i in range(3):
        for j in range(3):
            power += grid[(x+i, y+j)]
    return power


def np_power(x, y):
    rack_id = x + 1 + 10
    lvl = rack_id * (y + 1)
    lvl += serial
    lvl *= rack_id
    lvl = (lvl // 100) % 10
    return lvl - 5

if __name__ == '__main__':
    serial = 2866
    grid = {}
    for x in range(1, 301):
        for y in range(1, 301):
            grid[(x, y)] = power_level(x, y)

    max_power = 0
    for x in range(1, 299):
        for y in range(1, 299):
            coord_power = area_power(x, y, grid)
            if coord_power > max_power:
                max_power = coord_power
                coords = (x, y)

    print(f'Coordinates with maximum power are {coords}')

    # lets make a 2d numpy array, because it'll be faster/easier to do
    # window selection
    grid = np.fromfunction(np_power, (300, 300))

    max_power = 0
    for width in range(3, 300):
        windows = sum([grid[x:x-width+1 or None, y:y-width+1 or None] for x in range(width) for y in range(width)])
        maximum = int(windows.max())
        location = np.where(windows == maximum)
        # most values are negative, so at bigger windows the power level will
        # be negative too, so just break out Ctrl+C
        print(width, maximum)
        if maximum > max_power:
            max_power = maximum
            w = width
            coords = (location[0][0] + 1, location[1][0] + 1)

    print(f'Coordinates with maximum power are {coords}, {w}')
