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

        if i % 50000 == 0 and debug == True:
            print 'Generated {}/40000000 values, current total: {}'.format(i, total)

    return total


if __name__ == '__main__':
    generatorA = Generator(634, 16807)
    generatorB = Generator(301, 48271)

    print 'Part 1:', solve1(generatorA, generatorB, debug=True)
