from collections import Counter
import numpy as np

def get_most_common_bits(data):
    most_common_bits = ''
    for i in range(len(data[0])):
        counts = Counter(data[:,i])
        most_common_bits += counts.most_common()[0][0]

    return most_common_bits

def get_least_common_bits(data):
    return get_most_common_bits(data).replace('1', '2').replace('0', '1').replace('2', '0')

def part2(data):
    o2_numbers = data[:]
    co2_numbers = data[:]

    for i in range(len(data[0])):
        o2_counter = Counter([n[i] for n in o2_numbers])
        co2_counter = Counter([n[i] for n in co2_numbers])

        if len(o2_numbers) > 1:
            if o2_counter['0'] > o2_counter['1']:
                o2_numbers = [n for n in o2_numbers if n[i] == '0']
            else:
                o2_numbers = [n for n in o2_numbers if n[i] == '1']

        if len(co2_numbers) > 1:
            if co2_counter['0'] > co2_counter['1']:
                co2_numbers = [n for n in co2_numbers if n[i] == '1']
            else:
                co2_numbers = [n for n in co2_numbers if n[i] == '0']

    return int(''.join(o2_numbers[0]), 2) * int(''.join(co2_numbers[0]), 2)

if __name__ == '__main__':
    with open('day3.txt') as f:
        data = []
        for line in f.readlines():
            data.append([c for c in line.strip()])
        np_data = np.array(data)

    most_common_bits = get_most_common_bits(np_data)
    least_common_bits = get_least_common_bits(np_data)

    print(f"Part1: {int(most_common_bits, 2)} * {int(least_common_bits, 2)} = {int(most_common_bits, 2) * int(least_common_bits, 2)}")
    print(f'Part 2: {part2(data)}')
