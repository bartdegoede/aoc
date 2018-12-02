from collections import Counter

if __name__ == '__main__':
    with open('day2.txt', 'r') as f:
        ids = f.read().strip().split('\n')

    twos = 0
    threes = 0
    for id in ids:
        c = Counter(id)
        values = c.values()
        if 2 in values:
            twos += 1
        if 3 in values:
            threes += 1

    print(f'Checksum is {twos} * {threes} = {twos * threes}')
    for x in ids:
        for y in ids:
            diff = [i for i, j in zip(x, y) if i == j]
            if len(y) - len(diff) == 1:
                print(''.join(diff))
                break
