from operator import xor

def reverse_sublist(lst, start, end):
    sublist = []
    for i in xrange(start, end+1):
        sublist.append(lst[i % len(lst)])
    reverse = list(reversed(sublist))
    j = 0
    for i in xrange(start, end+1):
        lst[i % len(lst)] = reverse[j]
        j += 1
    return lst


def solve1(inp):
    lengths = [int(x) for x in inp.split(',')]
    lst = range(256)
    current_position = 0
    skip = 0

    for length in lengths:
        lst = reverse_sublist(lst, current_position, current_position + length - 1)
        current_position += (length + skip)
        skip += 1
    print lst[0] * lst[1]


def solve2(inp):
    lengths = [ord(c) for c in inp]
    lengths += [17, 31, 73, 47, 23]

    lst = range(256)
    current_position = 0
    skip = 0

    for i in xrange(64):
        for length in lengths:
            lst = reverse_sublist(lst, current_position, current_position + length - 1)
            current_position += (length + skip)
            skip += 1
    dense_hash = []
    for start, end in zip(range(0, len(lst), 16), range(16, len(lst)+16, 16)):
        dense_hash.append(reduce(xor, lst[start:end]))

    print ''.join([format(h, 'x').zfill(2) for h in dense_hash])


if __name__ == '__main__':
    lengths = '102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216'
    # solve1(lengths)
    solve2(lengths)

    # part2

