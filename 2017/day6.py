import itertools

if __name__ == '__main__':
    # banks = [0, 2, 7, 0]
    banks = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
    count = 0
    seen = {}
    while tuple(banks) not in seen:
        seen[tuple(banks)] = count
        idx, max_value = max(enumerate(banks), key=lambda k: (k[1], -k[0]))
        banks[idx] = 0
        for i in itertools.islice(itertools.cycle(xrange(len(banks))), idx + 1, idx + max_value + 1):
            banks[i] += 1
        count += 1
    print count

