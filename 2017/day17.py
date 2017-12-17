from collections import deque

def solve1():
    steps = 355
    position = 0
    spinlock_buffer = [0]

    for i in xrange(2017):
        new_position = ((position + steps) % len(spinlock_buffer)) + 1
        spinlock_buffer.insert(new_position, i + 1)
        position = new_position

    return spinlock_buffer[position + 1]

if __name__ == '__main__':
    print 'Part 1:', solve1()
