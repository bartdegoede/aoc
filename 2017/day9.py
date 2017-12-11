def solve1():
    in_garbage = False
    garbage_count = 0
    current_nesting = 0
    nesting_score = 0
    with open('day9.txt', 'r') as f:
        for char in f.read():
            if char == '!' and in_garbage:
                # ignore next character
                continue
            elif char == '<':
                # entering garbage block
                if in_garbage:
                    garbage_count += 1
                in_garbage = True
            elif char == '>':
                # completed garbage block
                in_garbage = False
            elif char == '{' and not in_garbage:
                current_nesting += 1
                nesting_score += current_nesting
            elif char == '}' and not in_garbage:
                current_nesting -= 1
            elif in_garbage:
                garbage_count += 1

    print 'Total nesting score: {}'.format(nesting_score)
    print 'Garbage count: {}'.format(garbage_count)


def solve2():
    with open('day9.txt') as input_file:
        line = input_file.readline()

    score = 0
    garbage_score = 0
    current_depth = 0
    inside_garbage = False
    skip_char = False
    for char in line:
        if inside_garbage:
            if skip_char:
                skip_char = False
            elif char == '!':
                skip_char = True
            elif char == '>':
                inside_garbage = False
            else:
                garbage_score += 1
        else:  # when inside group, not garbage
            if char == '{':
                current_depth += 1
            elif char == '}':
                score += current_depth
                current_depth -= 1
            elif char == '<':
                inside_garbage = True

    print("Part 1:   ", score)
    print("Part 2:   ", garbage_score)



if __name__ == '__main__':
    solve2()
