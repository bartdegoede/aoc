with open('day1.txt', 'r') as f:
    data = f.read()

elves = data.split('\n\n')
calories = []
for i, elf in enumerate(elves):
    calories.append((sum(map(int, elf.split())), i+1))

sorted_calories = sorted(calories, key=lambda x: x[0], reverse=True)
print(f'Most calories: {sorted_calories[0][0]}')
print(f'Top 3 most calories: {sum([cal[0] for cal in sorted_calories[:3]])}')
