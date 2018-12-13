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
