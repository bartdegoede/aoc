import heapq

def adjacent(positions):
    adj = set()
    for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        for x, y in positions:
            adj.add((x + dx, y + dy))
    return adj

def shortest_paths(source, targets, occupied):
    result = []
    best = None
    visited = set(occupied)
    queue = [(0, [source])]
    while queue:
        distance, path = heapq.heappop(queue)
        if best and len(path) > best:
            return result
        node = path[-1]
        if node in targets:
            result.append(path)
            best = len(path)
            continue
        if node in visited:
            continue
        visited.add(node)
        for neighbour in adjacent({node}):
            if neighbour not in visited:
                heapq.heappush(queue, (distance + 1, path + [neighbour]))
    return result


def choose_target(position, targets, occupied):
    if not targets:
        return None
    if position in targets:
        return position
    paths = shortest_paths(position, targets, occupied)
    ends = [x[-1] for x in paths]
    if ends:
        return min(ends)


def choose_move(position, target, occupied):
    if position == target:
        return position
    paths = shortest_paths(position, {target}, occupied)
    starts = [x[1] for x in paths]
    if starts:
        return min(starts)


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class Unit(object):
    def __init__(self, side, position):
        self.side = side # elf (E)/goblin (G)
        self.position = position # (x, y)
        self.hp = 200


class Battle(object):
    def __init__(self):
        self.walls = set()
        self.units = []
        self.rounds = 0
        self._init_map()

    def _init_map(self):
        # initialize map (basically, set up units and walls)
        with open('day15.txt', 'r') as f:
            area = f.read().split()

        for y, line in enumerate(area):
            for x, c in enumerate(line):
                if c == '#':
                    self.walls.add((x, y))
                elif c in 'EG':
                    self.units.append(Unit(c, (x, y)))

    def occupied_coords(self, unit=None):
        # return a set of occupied coordinates, omitting the provided unit
        # itself (you can't block yourself)
        units = set(x.position for x in self.units if x != unit and x.hp > 0)
        return self.walls.union(units)

    def next_move(self, unit):
        # given a unit, figure out its next move
        occupied = self.occupied_coords(unit)
        targets = set(x.position for x in self.units if x.side != unit.side
                                                     and x.hp > 0)
        if not targets:
            return
        in_range = adjacent(targets) - occupied
        target = choose_target(unit.position, in_range, occupied)
        if target is None:
            return unit.position
        return choose_move(unit.position, target, occupied)

    def attack(self, unit):
        targets = []
        for x in self.units:
            if (x.side != unit.side and x.hp > 0
                and manhattan_distance(unit.position, x.position) == 1):
                # this will let us sort by HP first, position second
                targets.append((x.hp, x.position, x))
        if targets:
            return min(targets)[-1]

    @property
    def total_hp(self):
        return sum([unit.hp for unit in self.units if unit.hp > 0])

    def step(self):
        units = sorted(self.units, key=lambda x: x.position)
        for unit in units:
            if unit.hp <= 0: # this one is dead, move on
                continue
            move = self.next_move(unit)
            if not move:
                return False
            unit.position = move
            attacked_unit = self.attack(unit)
            if attacked_unit:
                attacked_unit.hp -= 3

        self.rounds += 1
        return True

    def run(self):
        # run battle until one of the sides has lost
        while True:
            if not self.step():
                return self.rounds, self.total_hp
        # while self.step():
        #     if self.rounds % 10 == 0:
        #         print(f'{self.rounds} rounds of battle have passed')
        # return self.rounds, self.total_hp


if __name__ == '__main__':
    battle = Battle()
    rounds, total_hp = battle.run()
    print(f'Rounds * HP = {rounds * total_hp}')
