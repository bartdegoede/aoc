from collections import defaultdict

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

if __name__ == '__main__':
    with open('day6.txt', 'r') as f:
        coordinates = f.readlines()

    coords = []
    for coordinate in coordinates:
        coords.append(tuple(map(int, coordinate.split(', '))))

    region_sizes = defaultdict(int)
    ignore = set()
    shared_region = 0

    max_x, min_x = max(coords, key=lambda x: x[0])[0], min(coords, key=lambda x: x[0])[0]
    max_y, min_y = max(coords, key=lambda x: x[1])[1], min(coords, key=lambda x: x[1])[1]

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            # for all the potential coordinates, find the closest point
            # i will correspond to the position in coords
            dists = sorted([(manhattan_distance((x, y), coord), i) for i, coord in enumerate(coords)])
            dist_sum = sum([dist[0] for dist in dists])
            # we don't have to count the coordinate if it is equally far to
            # more than one coordinate
            if dists[0][0] != dists[1][0]:
                region_sizes[dists[0][1]] += 1
                if x in (min_x, max_x) or y in (min_y, max_y):
                    ignore.add(dists[0][1])

            # this works because the edge coordinates we ignored before will be
            # far enough from the other edge coordinates
            if dist_sum < 10000:
                shared_region += 1

    print(f'Largest area: {max([size for coord_id, size in region_sizes.items() if coord_id not in ignore])}')
    print(f'Largest shared region: {shared_region}')
