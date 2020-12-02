from collections import Counter

with open('day2.txt', 'r') as f:
    passwords = [line.strip().split(': ') for line in f.readlines()]

valid_passwords_1 = 0
valid_passwords_2 = 0

for password in passwords:
    pw_range, character = password[0].split()
    min_range, max_range = list(map(int, pw_range.split('-')))
    character_counts = Counter(password[1])
    if min_range <= character_counts.get(character, 0) <= max_range:
        valid_passwords_1 += 1

    first = password[1][min_range - 1]
    second = password[1][max_range - 1]
    if first == character or second == character:
        if first != second:
            valid_passwords_2 += 1

print(f'There are {valid_passwords_1} valid passwords')
print(f'There are {valid_passwords_2} valid passwords')
