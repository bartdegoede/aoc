with open('day4.txt', 'r') as f:
    pairs = f.read().strip().split('\n')

def to_range(pair):
    start, end = map(int, pair.split('-'))
    # the ranges are inclusive
    return set(range(start, end+1))

ranges = 0
overlaps = 0
for pair in pairs:
    pair1, pair2 = map(to_range, pair.split(','))
    if pair1.issubset(pair2) or pair2.issubset(pair1):
        ranges += 1
    if pair1.intersection(pair2):
        overlaps += 1

print(f'Part 1: {ranges}')
print(f'Part 2: {overlaps}')
