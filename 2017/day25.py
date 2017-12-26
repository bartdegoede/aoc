if __name__ == '__main__':
    head = 0
    tape = {}
    steps = 12481997
    a, b, c, d, e, f = range(6)
    state = a
    left = -1
    right = 1

    turing_machine = {
        (a, 0): (1, right, b),
        (a, 1): (0, left, c),
        (b, 0): (1, left, a),
        (b, 1): (1, right, d),
        (c, 0): (0, left, b),
        (c, 1): (0, left, e),
        (d, 0): (1, right, a),
        (d, 1): (0, right, b),
        (e, 0): (1, left, f),
        (e, 1): (1, left, c),
        (f, 0): (1, right, d),
        (f, 1): (1, right, a)
    }

    for i, step in enumerate(range(steps)):
        value = tape.get(head, 0)
        write_val, move, next_state = turing_machine.get((state, value))

        tape[head] = write_val
        head += move
        state = next_state
        if i % 10000 == 0:
            print('{}/{}'.format(i, steps))

    print('Part 1: {}'.format(sum(tape.values())))

