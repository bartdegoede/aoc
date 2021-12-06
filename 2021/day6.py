from collections import defaultdict

def run_days(days, fish):
    age_to_count = defaultdict(int)
    for f in fish:
        age_to_count[f] += 1

    for _ in range(days):
        n = defaultdict(int)
        for age, count in age_to_count.items():
            if age > 0:
                n[age - 1] += count
            else:
                n[6] += count
                n[8] += count
            age_to_count = n

    return sum(age_to_count.values())


if __name__ == "__main__":
    with open('day6.txt') as f:
        fish = list(map(int, f.read().strip().split(',')))

    print(f'Part 1: {run_days(80, fish)} lanternfish')
    print(f'Part 2: {run_days(256, fish)} lanternfish')
