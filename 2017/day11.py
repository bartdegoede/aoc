"""
This is heavily inspired/stolen from https://www.redblobgames.com/grids/hexagons/
Hexagons and their coordinates are cool.
"""

class Cube(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'Cube <{}, {}, {}>'.format(self.x, self.y, self.z)


class Hex(object):
    def __init__(self, q, r):
        self.q = q
        self.r = r
        self.moves = {
            'n': lambda q, r: (q, r - 1),
            's': lambda q, r: (q, r + 1),
            'nw': lambda q, r: (q - 1, r),
            'sw': lambda q, r: (q - 1, r + 1),
            'ne': lambda q, r: (q + 1, r - 1),
            'se': lambda q, r: (q + 1, r)
        }

    def __repr__(self):
        return 'Hex <{}, {}>'.format(self.q, self.r)

    def move(self, direction):
        self.q, self.r = self.moves[direction](self.q, self.r)


def cube_to_axial(cube):
    q = cube.x
    r = cube.z
    return Hex(q, r)


def axial_to_cube(hex):
    x = hex.q
    z = hex.r
    y = -x-z
    return Cube(x, y, z)


def cube_distance(a, b):
    # 2D Manhattan distance: abs(dx) + abs(dy)
    # 3D Manhattan distance: abs(dx) + abs(dy) + abs(dz)
    # in hex grid, that's half: https://www.redblobgames.com/grids/hexagons/#distances-cube
    # return (abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)) / 2.0
    # however, one of the three coordinates is the sum of the other two,
    # as hex coordinates need to sum to zero:
    return max(abs(a.x - b.x), abs(a.y - b.y), abs(a.z - b.z))


def hex_distance(a, b):
    ac = axial_to_cube(a)
    bc = axial_to_cube(b)
    return cube_distance(ac, bc)

if __name__ == '__main__':
    with open('day11.txt', 'r') as f:
        directions = f.read().strip().split(',')
    position = Hex(0, 0)
    origin = Hex(0, 0)
    max_distance = 0
    for direction in directions:
        position.move(direction)

        distance_from_origin = hex_distance(origin, position)
        if distance_from_origin > max_distance:
            max_distance = distance_from_origin

    print 'Distance: ', hex_distance(origin, position)
    print 'Max distance from origin: ', max_distance
