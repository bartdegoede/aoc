from day10 import knothash

def to_binary(h):
    return ''.join([bin(int(c, 16))[2:].zfill(4) for c in h])

def solve1(inp):
    total = 0
    hashes = [knothash('{}-{}'.format(inp, i)) for i in xrange(128)]
    for h in hashes:
        total += sum([int(c) for c in to_binary(h)])

    return total


if __name__ == '__main__':
    print 'Part 1:', solve1('vbqugkhl')
