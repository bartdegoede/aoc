# from collections import deque

# def bresenham(x0, y0, x1, y1):
#     # Bresenham's line algorithm can give us all the coordinates between two points
#     # https://en.wikipedia.org/wiki/Bresenham's_line_algorithm
#     dx = x1 - x0
#     dy = y1 - y0

#     xsign = 1 if dx > 0 else -1
#     ysign = 1 if dy > 0 else -1

#     dx = abs(dx)
#     dy = abs(dy)

#     if dx > dy:
#         xx, xy, yx, yy = xsign, 0, 0, ysign
#     else:
#         dx, dy = dy, dx
#         xx, xy, yx, yy = 0, ysign, xsign, 0

#     D = 2*dy - dx
#     y = 0

#     for x in range(dx+1):
#         yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
#         if D >= 0:
#             y += 1
#             D -= 2*dx
#         D += 2*dy


# if __name__ == '__main__':
#     with open('day10.txt', 'r') as f:
#         data = f.readlines()

#     coordinates = set([])
#     for y, row in enumerate(data):
#         for x, column in enumerate(row.strip()):
#             if column == '#':
#                 coordinates.add((x,y))

#     # we're tracing a line from each asteroid to the edge of the grid
#     grid_edges = [(x, 0) for x in range(len(row))]
#     grid_edges += [(len(row) - 1, y) for y in range(len(data))]
#     grid_edges += [(0, y) for y in range(len(data))]
#     grid_edges += [(x, len(row) - 1) for x in range(len(row))]

#     max_observable_asteroids = 0
#     for i, coordinate in enumerate(coordinates):
#         observable_asteroids = 0
#         observed_asteroids = set([])
#         for other_coordinate in grid_edges:
#             for position in list(bresenham(*coordinate, *other_coordinate))[1:]:
#                 if position in coordinates and position not in observed_asteroids:
#                     observable_asteroids += 1
#                     observed_asteroids.add(position)
#                     break
#         print(coordinate, observable_asteroids)
#         max_observable_asteroids = max(observable_asteroids, max_observable_asteroids)
#         if i % 10 == 0:
#             print(f'Compared {i}/{len(coordinates)}')
#     print(f'Part 1: {max_observable_asteroids}')

import collections
import itertools
import cmath
import math
import re
import sys

import sortedcollections

with open(sys.argv[1]) as f:
    lines = [l.rstrip('\n') for l in f]

    # part 1
    maxcnt = 0
    best = None
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '.':
                continue
            cnt = 0
            s = set()
            for x in range(len(lines)):
                for y in range(len(lines[0])):
                    if lines[x][y] == '.':
                        continue
                    gc = int(abs(math.gcd(x - i, y - j)))
                    no = False
                    #print(x,y, gc)
                    for q in range(1, gc):
                        if lines[i + (x - i) // gc * q][j + (y - j) // gc * q] == '#':
                            no = True
                            break
                    if not no:
                        s.add((x, y))
                        cnt += 1
            #print(i, j, cnt, sorted(s))
            maxcnt = max(cnt, maxcnt)
            if cnt == maxcnt:
                best = i, j
    print(maxcnt, best)

    # part 2
    allast = set()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                allast.add((i, j))
    phase = lambda xy: cmath.phase((xy[0] - best[0]) + (xy[1] - best[1]) * 1j)
    so = sorted(allast, key=phase,reverse=True)
    for i, (direc, asts) in enumerate(itertools.groupby(so, key=phase)):
        if i + 1 == 200:
            print(i + 1, direc, list(asts))

    # part 2 appendix: I didn't write this during the timed contest but if I
    # had to loop around to get the answer (i.e. if there were fewer than 200
    # different directions) it might've looked something like this:
    grouped = []
    for direc, asts in itertools.groupby(so, key=phase):
        grouped.append(list(asts))
    i = 0
    def pop():
        global i
        oi = i
        while not grouped[i]:
            i = (i + 1) % len(grouped)
            if i == oi:
                return None
        closest = min(grouped[i], key=lambda xy: math.hypot(xy[0] - best[0], xy[1] - best[1]))
        grouped[i][:] = [p for p in grouped[i] if p != closest]
        i = (i + 1) % len(grouped)
        return closest
    for _ in range(200 - 1):
        pop()
    print(pop())
