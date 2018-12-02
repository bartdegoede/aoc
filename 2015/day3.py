directions = {
    '^': lambda x, y: (x, y+1),
    '>': lambda x, y: (x+1, y),
    'v': lambda x, y: (x, y-1),
    '<': lambda x, y: (x-1, y)
}


if __name__ == '__main__':
    with open('day3.txt', 'r') as f:
        instructions = f.read().strip()

    pos = (0, 0)
    visited = set([pos])
    for step in instructions:
        pos = directions[step](*pos)
        visited.add(pos)

    print(f'Santa visited at least {len(visited)} houses')

    santa_pos = (0, 0)
    robo_pos = (0, 0)
    santa_visited = set([santa_pos])
    robot_visited = set([robo_pos])
    for i, step in enumerate(instructions):
        if i % 2 == 0:
            # santa goes first
            santa_pos = directions[step](*santa_pos)
            santa_visited.add(santa_pos)
        else:
            robo_pos = directions[step](*robo_pos)
            robot_visited.add(robo_pos)

    print(f'Santa and Robosanta visited {len(santa_visited.union(robot_visited))} unique houses')
