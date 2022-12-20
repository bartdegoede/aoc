with open('day9.txt', 'r') as f:
    data = f.read().splitlines()

directions = {
    'U': lambda pos: (pos[0], pos[1] + 1),
    'D': lambda pos: (pos[0], pos[1] - 1),
    'L': lambda pos: (pos[0] - 1, pos[1]),
    'R': lambda pos: (pos[0] + 1, pos[1])
}

def move(x):
    return 1 if x > 0 else -1

def distance_between(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def update_tail_position(head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]

    # if positions are adjancent, return tail
    if abs(x_diff) <= 1 and abs(y_diff) <= 1:
        return tail

    # same column
    if x_diff == 0:
        return (tail[0], tail[1] + move(y_diff))
    # same row
    elif y_diff == 0:
        return (tail[0] + move(x_diff), tail[1])
    # diagonal
    else:
        if x_diff > 0 and y_diff > 0:
            return (tail[0] + 1, tail[1] + 1)
        elif x_diff < 0 and y_diff > 0:
            return (tail[0] - 1, tail[1] + 1)
        elif x_diff < 0 and y_diff < 0:
            return (tail[0] - 1, tail[1] - 1)
        elif x_diff > 0 and y_diff < 0:
            return (tail[0] + 1, tail[1] - 1)


def part1():
    visited =  set()

    head_position = (0, 0)
    tail_position = (0, 0)

    for instruction in data:
        direction = instruction[0]
        distance = int(instruction[1:])

        for _ in range(distance):
            head_position = directions[direction](head_position)
            tail_position = update_tail_position(head_position, tail_position)
            visited.add(tail_position)

    print(f'Part 1: {len(visited)}')

def part2():
    visited =  set()

    positions = [
        (0, 0)
    ] * 10

    for instruction in data:
        direction = instruction[0]
        distance = int(instruction[1:])

        for _ in range(distance):
            positions[0] = directions[direction](positions[0])
            for i in range(1, len(positions)):
                positions[i] = update_tail_position(positions[i - 1], positions[i])

            # last knot
            if i == len(positions) - 1:
                visited.add(positions[i])

    print(f'Part 2: {len(visited)}')

if __name__ == '__main__':
    part1()
    part2()
