"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8 3^2  10
21  22  23  24 5^2
..  ..  ..  ..  .. 7^2
"""

import math

input = 361527

def side_length(number):
    # this is the closest bottom right corner to number
    side = math.ceil(math.sqrt(number))
    side = side if side % 2 != 0 else side + 1
    return side

from itertools import count

def sum_spiral():
    a, i, j = {(0,0) : 1}, 0, 0
    for s in count(1, 2):
        for (ds, di, dj) in [(0, 1, 0), (0, 0, -1), (1, -1, 0), (1, 0, 1)]:
            for _ in xrange(s + ds):
                i += di
                j += dj
                a[i,j] = sum(a.get((k,l), 0) for k in range(i-1,i+2)
                                             for l in range(j-1,j+2))
                yield a[i,j]


def part2(number):
    for x in sum_spiral():
        if x>number: return x

print part2(input)
# side = side_length(input)
# steps_to_reach_center = (side - 1) / 2
# axes = [side**2 - ((side-1)*i) - math.floor(side/2) for i in range(0, 4)]
# steps_to_reach_axes_from_input = min([abs(axis - input) for axis in axes])
# print steps_to_reach_axes_from_input + steps_to_reach_center
