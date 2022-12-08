import math

tree_map = []
with open('day8.txt', 'r') as f:
    for row in f.readlines():
        tree_map.append(list(map(int, row.strip())))

max_i = len(tree_map)
max_j = len(tree_map[0])
invisible = 0
scores = []

for i in range(1, max_i - 1):
    for j in range(1, max_j - 1):
        # go to -1 to include the edge row
        left = [tree_map[i][l] for l in range(j-1, -1, -1)]
        # pretty cool, copilot figured out the next three lines after I typed the first one :exploding_head:
        right = [tree_map[i][r] for r in range(j+1, max_j)]
        up = [tree_map[u][j] for u in range(i-1, -1, -1)]
        down = [tree_map[d][j] for d in range(i+1, max_i)]

        current_height = tree_map[i][j]
        # instead of finding the visible trees, we'll count the invisible ones and subtract later
        highest_trees = [max(left), max(right), max(up), max(down)]
        if not [tree for tree in highest_trees if tree < current_height]:
            invisible += 1

        direction_scores = []
        for direction in [left, right, up, down]:
            direction_score = []
            for tree_height in direction:
                if current_height > tree_height:
                    direction_score.append(1)
                else:
                    direction_score.append(0)

            try:
                s = direction_score.index(0) + 1
            except ValueError: # i.e. there's no 0 in the list
                s = len(direction_score)
            direction_scores.append(s)
        scores.append(math.prod(direction_scores))

print(f'Part 1: {max_i*max_j - invisible}')
print(f'Part 2: {max(scores)}')
