from collections import defaultdict, deque

def count(obj):
    total = 0
    for orbit in orbits.get(obj, []):
        total += count(orbit)
        total += 1
    return total

if __name__ == '__main__':
    with open('day6.txt', 'r') as f:
        data = f.readlines()

    orbits = defaultdict(list)
    reverse_orbits = defaultdict(list)

    for orbit in data:
        a, b = orbit.strip().split(')')
        orbits[a].append(b)
        # we need a bidirectional graph, effectively; this is bad naming
        reverse_orbits[a].append(b)
        reverse_orbits[b].append(a)
    total = 0
    for orbit in orbits:
        total += count(orbit)
    print(f'Part 1: {total}')

    visited = {}
    queue = deque()
    queue.append(('YOU', 0))
    while queue:
        obj, dist = queue.popleft()
        if obj in visited:
            continue
        visited[obj] = dist
        for ob in reverse_orbits[obj]:
            queue.append((ob, dist + 1))
    # we need to -2 because otherwise we count YOU and SAN as well
    print(f'Part 2: {visited["SAN"] - 2}')
