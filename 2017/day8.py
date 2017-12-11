from collections import defaultdict

def parse_instruction(instruction, data, max_value):
    instruction = line.split()
    registry = instruction[0]
    action = instruction[1]
    increment = int(instruction[2])
    condition = instruction[4:]

    if eval('{} {}'.format(data[condition[0]], ' '.join(condition[1:]))):
        if action == 'inc':
            newval = data[registry] + increment
            data[registry] = newval
        else:
            newval = data[registry] - increment
            data[registry] = newval
        return newval


if __name__ == '__main__':
#     instructions = """b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10"""
    max_value = 0
    data = defaultdict(lambda: 0)
    with open('day8.txt', 'r') as instructions:
        for line in instructions:
            newval = parse_instruction(line, data, max_value)
            if newval > max_value:
                max_value = newval

    print max(data.values())
    print max_value

