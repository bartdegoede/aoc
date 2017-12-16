import itertools

class Generator(object):
    def __init__(self, initial, factor):
        self.value = initial
        self.factor = factor

    def generate(self):
        self.value = (self.value * self.factor) % 2147483647

    @property
    def hash_value(self):
        return bin(self.value)[2:].zfill(32)


def compare(h1, h2):
    return True if h1[16:] == h2[16:] else False


def solve1(generatorA, generatorB, debug=False):
    total = 0
    for i in xrange(40000000):
        if compare(generatorA.hash_value, generatorB.hash_value):
            total += 1

        generatorA.generate()
        generatorB.generate()

        if i % 50000 == 0 and debug:
            print 'Generated {}/40000000 values, current total: {}'.format(i, total)

    return total


def solve2(generatorA, generatorB, debug=False):
    a = []
    b = []
    counter = 0
    while len(a) < 5000000 or len(b) < 5000000:
        if generatorA.value % 4 == 0 and len(a) < 5000000:
            a.append(generatorA.hash_value)
        if generatorB.value % 8 == 0 and len(b) < 5000000:
            b.append(generatorB.hash_value)

        generatorA.generate()
        generatorB.generate()
        counter += 1
        if counter % 100000 == 0 and debug:
            print 'Done {} iterations; A: {}, B: {}'.format(counter, len(a),
                                                            len(b))

    total = 0
    for h1, h2 in itertools.izip(a, b):
        if compare(h1, h2):
            total += 1

    return total

if __name__ == '__main__':
    print 'Part 1:', solve1(Generator(634, 16807), Generator(301, 48271), debug=True)
    print 'Part 2:', solve2(Generator(634, 16807), Generator(301, 48271), debug=True)
