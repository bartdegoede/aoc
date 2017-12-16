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

    def __repr__(self):
        return 'Scanner <{}, {}, position: {}>'.format(self.depth,
                                                       self.range,
                                                       self.position)


def move_scanners(scanners):
    for scanner in scanners.values():
        scanner.step()


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


def solve2(scanners):
    counter = 0
    while True:
        if solve1(scanners) == 0:
            break
        move_scanners(scanners)
        counter += 1
        if counter % 100 == 0:
            print 'Tried {} steps'.format(counter)
    return counter


if __name__ == '__main__':
    scanners = {}
    scanners2 = {}
    with open('day13.txt', 'r') as f:
        for scanner in f:
            depth, scanner_range = scanner.split(': ')
            scanners[int(depth)] = Scanner(int(depth), int(scanner_range))
            scanners2[int(depth)] = Scanner(int(depth), int(scanner_range))

    print 'Part 1:', solve1(scanners)
    print 'Part 2:', solve2(scanners2)


