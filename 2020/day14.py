with open('day14.txt', 'r') as f:
    program = [line.strip() for line in f.readlines()]

mem1 = {}
mem2 = {}

def apply_mask(value, mask):
    value_in_bits = list(format(value, '036b'))
    for i in range(len(mask)):
        if mask[i] != 'X':
            value_in_bits[i] = mask[i]
    return int(''.join(value_in_bits), 2)

def generate_memory_addresses(addr, mask, value):
    value_in_bits = list(format(int(addr), '036b'))
    for i in range(len(mask)):
        if mask[i] != '0':
            value_in_bits[i] = mask[i]
    floating = []
    floating_count = value_in_bits.count('X')
    for i in range(2**floating_count):
        floating.append(list(bin(i)[2:].zfill(floating_count)))

    for f in floating:
        i = 0
        address = ''
        for j, v in enumerate(value_in_bits):
            if v != 'X':
                address += str(v)
            else:
                address += str(f[i])
                i += 1
        mem2[int(address, 2)] = value

for line in program:
    if line.startswith('mask'):
        mask = line.replace('mask = ', '')
        continue
    address, value = line.split(' = ')
    value = int(value)
    mem1[int(address.replace('mem[', '').replace(']', ''))] = apply_mask(value, mask)
    generate_memory_addresses(address.replace('mem[', '').replace(']', ''), mask, value)

print(f'Sum of all values is {sum(mem1.values())}')
print(f'Sum of all values is {sum(mem2.values())}')
