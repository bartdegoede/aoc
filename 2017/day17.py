from collections import deque
import time

def solve1():
    steps = 355
    position = 0
    spinlock_buffer = [0]

    for i in xrange(2017):
        new_position = ((position + steps) % len(spinlock_buffer)) + 1
        spinlock_buffer.insert(new_position, i + 1)
        position = new_position

    return spinlock_buffer[position + 1]


def solve2():
    start = time.time()
    steps = 355
    spinlock_buffer = deque([0])
    for i in xrange(1, 50000001):
        spinlock_buffer.rotate(-steps)
        spinlock_buffer.append(i)
        if i % 100000 == 0:
            print 'Cycled {} times'.format(i)

    buff = list(spinlock_buffer)
    print 'Took {} seconds'.format(time.time() - start)
    return buff[buff.index(0) + 1]


if __name__ == '__main__':
    print 'Part 1:', solve1()
    print 'Part 2:', solve2()
