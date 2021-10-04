from itertools import count
import heapq

# return the shortest path from source to any of the targets
# in the case of a tie, return all shortest paths
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
        for neighbor in adjacent({node}):
            if neighbor in visited:
                continue
            heapq.heappush(queue, (distance + 1, path + [neighbor]))
    return result

# compute the manhattan distance between points
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# adjacent returns all cells that are adjacent to all of the provided positions
def adjacent(positions):
    return set((y + dy, x + dx)
        for y, x in positions
            for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)])

# choose_target determines which target square a unit at `position` should
# move toward, given the specified target units
def choose_target(position, targets, occupied):
    if not targets:
        return None
    if position in targets:
        return position
    paths = shortest_paths(position, targets, occupied)
    ends = [x[-1] for x in paths]
    return min(ends) if ends else None

# choose_move determines the immediate up/down/left/right move to make
# given the source and target squares
def choose_move(position, target, occupied):
    if position == target:
        return position
    paths = shortest_paths(position, {target}, occupied)
    starts = [x[1] for x in paths]
    return min(starts) if starts else None

# a Unit is an elf or a goblin
# team is E or G, position is a (y, x) tuple, hp is remaining hit points
class Unit:
    def __init__(self, team, position):
        self.team = team
        self.position = position
        self.hp = 200

# Model tracks the state of the game, including walls, units, # of rounds, etc.
class Model:
    def __init__(self, lines, elf_attack=None):
        self.elf_attack = elf_attack
        self.walls = set()
        self.units = []
        self.rounds = 0
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                if c == '#':
                    self.walls.add((y, x))
                elif c in 'EG':
                    self.units.append(Unit(c, (y, x)))

    # total_hp returns the total hit points for all remaining (alive) units
    def total_hp(self):
        return sum(x.hp for x in self.units if x.hp > 0)

    # occupied returns a set of occupied squares (walls or other units)
    # the provided unit is omitted, as a unit cannot block itself
    def occupied(self, unit=None):
        units = set(x.position for x in self.units
            if x != unit and x.hp > 0)
        return self.walls | units

    # get_move returns the new position for the unit on its turn
    def get_move(self, unit):
        occupied = self.occupied(unit)
        targets = set(x.position for x in self.units
            if x.team != unit.team and x.hp > 0)
        if not targets:
            return None
        in_range = adjacent(targets) - occupied
        target = choose_target(unit.position, in_range, occupied)
        if target is None:
            return unit.position
        move = choose_move(unit.position, target, occupied)
        return move

    # get_attack return which unit to attack given the specified attacker
    def get_attack(self, unit):
        units = [(x.hp, x.position, x) for x in self.units
            if x.team != unit.team and x.hp > 0 and
                manhattan_distance(unit.position, x.position) == 1]
        return min(units)[-1] if units else None

    # step executes one round - a single turn for each remaining unit
    def step(self):
        units = sorted(self.units, key=lambda x: x.position)
        for unit in units:
            if unit.hp <= 0:
                continue
            move = self.get_move(unit)
            if move is None:
                return False
            unit.position = move
            attack = self.get_attack(unit)
            if attack:
                if self.elf_attack:
                    if unit.team == 'G':
                        attack.hp -= 3
                        if attack.hp <= 0:
                            raise Exception
                    else:
                        attack.hp -= self.elf_attack
                else:
                    attack.hp -= 3
        self.rounds += 1
        return True

    # run executes the game until one of the teams has lost
    # it returns the number of complete rounds executed and the total hp
    # of all remaining units
    def run(self):
        while True:
            if not self.step():
                return self.rounds, self.total_hp()

with open('day15.txt', 'r') as f:
    lines = f.read().split()

# part 1
rounds, hp = Model(lines).run()
print(rounds * hp)

# part 2
for elf_attack in count(4):
    try:
        rounds, hp = Model(lines, elf_attack).run()
        print(rounds * hp)
        break
    except Exception:
        pass
