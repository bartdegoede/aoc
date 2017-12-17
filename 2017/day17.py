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
    steps = 355
    spinlock_buffer = deque([0])
    for i in xrange(1, 50000001):
        spinlock_buffer.rotate(-steps)
        spinlock_buffer.append(i)

    buff = list(spinlock_buffer)

    return buff[buff.index(0) + 1]


def solve2a():
    # we don't actually have to do the rotation of the array and insert
    # values; we just need to keep track of the value we're inserting
    # when we're inserting at position 1
    steps = 355
    position = 0
    value = None
    for i in xrange(1, 50000001):
        new_position = ((position + steps) % i) + 1
        if new_position == 1:
            value = i
        position = new_position

    return value


if __name__ == '__main__':
    print 'Part 1:', solve1()
    start = time.time()
    print 'Part 2:', solve2()
    print 'Took {} seconds'.format(time.time() - start)
    start = time.time()
    print 'Part 2a:', solve2a()
    print 'Took {} seconds'.format(time.time() - start)
