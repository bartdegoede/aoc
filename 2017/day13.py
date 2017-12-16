class Scanner(object):
    def __init__(self, depth, scanner_range):
        self.depth = depth
        self.range = scanner_range
        self.position = 1
        self.reverse = False

    def step(self):
        if self.reverse:
            self.position -= 1
        else:
            self.position += 1

        if self.position == self.range:
            self.reverse = True
        if self.position == 1:
            self.reverse = False

    def get_position_at(self, t, scanner_range):
        # https://en.wikipedia.org/wiki/Chinese_remainder_theorem
        # thanks Vincent
        offset = t % ((scanner_range - 1) * 2)
        if offset > scanner_range - 1:
            return 2 * (scanner_range - 1) - offset
        else:
            return offset

    def __repr__(self):
        return 'Scanner <{}, {}, position: {}>'.format(self.depth,
                                                       self.range,
                                                       self.position)


def move_scanners(scanners):
    for scanner in scanners.values():
        scanner.step()


def load_scanners():
    scanners = {}
    with open('day13.txt', 'r') as f:
        for scanner in f:
            depth, scanner_range = scanner.split(': ')
            scanners[int(depth)] = Scanner(int(depth), int(scanner_range))
    return scanners


def solve1(scanners):
    max_depth = max(scanners) + 1
    position = 0
    severities = []

    for step in range(max_depth):
        current_scanner = scanners.get(step)
        if current_scanner and current_scanner.position == 1:
            severities.append(step * current_scanner.range)
        move_scanners(scanners)
        position += 1
    return sum(severities)


def solve2(debug=False):
    scanners = {}
    # just pretend that this is not here
    s = Scanner(1, 1)
    with open('day13.txt', 'r') as f:
        for scanner in f:
            depth, scanner_range = scanner.split(': ')
            scanners[int(depth)] = int(scanner_range)

    t = 0
    while True:
        if not any([s.get_position_at(t + depth, scanner_range) == 0 for depth, scanner_range in scanners.iteritems()]):
            print 'Part 2: Start at t = {}'.format(t)
            break
        t += 1
        if t % 1000 == 0 and debug == True:
            print 'Waited {}'.format(t)




if __name__ == '__main__':
    print 'Part 1:', solve1(load_scanners())
    solve2()


