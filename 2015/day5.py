import re
from collections import Counter

def is_nice(string):
    if re.search(r'ab|cd|pq|xy', string):
        return False

    counter = Counter(string)
    vowel_count = sum([counter.get(vowel, 0) for vowel in 'aeiou'])
    if vowel_count < 3:
        return False

    # final condition is it needs to have at least one pair
    p0 = 0
    p1 = 1
    while p1 < len(string):
        if string[p0] == string[p1]:
            return True
        p0 += 1
        p1 += 1
    return False


def is_nice2(string):
    pairs = []
    for i in range(0, len(string), 2):
        pairs.append(string[i:i+2])
    if len(pairs) == len(set(pairs)):
        return False
    i = 0
    while (i + 2) < len(string):
        if string[i] == string[i+2]:
            print(string, string[i:i+3])
            return True
        i += 1
    return False

if __name__ == '__main__':
    with open('day5.txt', 'r') as f:
        print(f'Part 1: {sum([1 for line in f if is_nice(line.strip())])}')
        f.seek(0)
        print(f'Part 2: {sum([1 for line in f if is_nice2(line.strip())])}')
