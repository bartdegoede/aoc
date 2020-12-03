from functools import reduce

with open('day3.txt', 'r') as f:
    slope = [[c for c in line.strip()] for line in f.readlines()]

def count_trees(right, down):
    x = 0
    y = 0
    trees = 0

    for i, row in enumerate(slope):
        x = i * right
        y = i * down
        if y <= len(slope) and slope[y][x % len(row)] == '#':
            trees += 1
    return trees

routes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = []
for right, down in routes:
    trees.append(count_trees(right=right, down=down))

print(f'There are {count_trees(right=3, down=1)} trees')
print(f'There are {reduce(lambda x, y: x * y, trees)} trees')
