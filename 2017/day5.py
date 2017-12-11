if __name__ == '__main__':
    with open('day5.txt', 'r') as f:
        instructions = [int(i) for i in f.read().split()]
    position = 0
    counter = 0
    while position < len(instructions) and position > -1:
        jump = instructions[position]
        if jump >= 3:
            instructions[position] -= 1
        else:
            instructions[position] += 1
        position = position + jump
        counter += 1
        if counter % 1000 == 0:
            print 'Processed {} steps'.format(counter)
    print counter
