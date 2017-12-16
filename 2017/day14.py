from day10 import knothash


def to_binary(h):
    return ''.join([bin(int(c, 16))[2:].zfill(4) for c in h])


if __name__ == '__main__':
    inp = 'vbqugkhl'
    total = 0
    grid = set()
    for i in xrange(128):
        h = knothash('{}-{}'.format(inp, i))
        row = map(int, to_binary(h))
        total += sum(row)
        # add coordinates of 1 bits for part 2
        for j, bit in enumerate(row):
            if bit == 1:
                grid.add((i, j))

    print 'Part 1:', total

    regions = 0
    while grid:
        regions += 1
        coordinates = [grid.pop()]
        while coordinates:
            # empty the coordinates set, so we can break out of the loop
            # when we don't find any neighbours anymore
            # make sure we keep a copy of the original coordinates though
            current_coordinates = list(coordinates)
            coordinates = []
            for x, y in current_coordinates:
                # look at neighbours
                for pair in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if pair in grid:
                        # we don't have to consider this neighbour anymore later
                        grid.remove(pair)
                        # check this neighbours coordinates
                        coordinates.append(pair)
    print 'Part 2:', regions
