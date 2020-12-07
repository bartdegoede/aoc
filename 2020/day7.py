with open('day7.txt', 'r') as f:
    rules = [line.strip() for line in f.readlines()]

bags = {}
for rule in rules:
    left, right = rule.split(' contain ')
    left = left.replace(' bags', '')
    bags[left] = []
    if right != 'no other bags.':
        for bag in right.split(', '):
            count, *colors, _ = bag.split()
            bags[left].append((int(count), ' '.join(colors)))

def count_colors(bag_color):
    return any(color == 'shiny gold' or count_colors(color) for _, color in bags[bag_color])

def count_bags(bag_color):
    return 1 + sum(count * count_bags(color) for count, color in bags[bag_color])

print(f'There are {sum(map(count_colors, bags.keys()))} bag colors')
print(f'There are {count_bags("shiny gold") - 1} individual bags')
