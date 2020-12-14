from functools import reduce

with open('day13.txt', 'r') as f:
    start, leave_times = f.read().split()

start = int(start)
leave_times = leave_times.split(',')
buses = [int(t)for t in leave_times if t != 'x']

def find_earliest_time(start):
    while True:
        for bus in buses:
            if start % bus == 0:
                return start, bus
        start += 1

t, bus = find_earliest_time(start)
print(f'The first bus leaves at {(t - start) * bus}')

# Nicked Chinese Reminder Theorem implementation nicked from
# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    total = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        total += a_i * mul_inv(p, n_i) * p
    return total % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

buses = [int(t) if t != 'x' else None for t in leave_times]
n = []
a = []
for i, t in enumerate(buses):
    if t:
        n.append(t)
        # we just need to offset the timestamps
        a.append(t - i)

print(f'The earliest timestamp is {chinese_remainder(n, a)}')
