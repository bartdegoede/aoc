from collections import defaultdict

def directory(path):
    return '/'.join(path).replace('//', '/')

def get_directories(data):
    cwd = []
    directories = defaultdict(int)

    for line in data:
        if line.startswith('dir'):
            continue
        if line.startswith('$'):
            _, command, *args = line.split()
            if command == 'cd':
                if args[0] == '..':
                    cwd.pop()
                else:
                    cwd.append(args[0])
        # the LAST command is 'ls', so the NEXT line will have the sizes, and we DON'T update 'command'
        elif command == 'ls':
            size = int(line.split()[0])
            for i in range(len(cwd)):
                directories[directory(cwd[:i + 1])] += size

    return directories

if __name__ == '__main__':
    with open('day7.txt', 'r') as f:
        data = f.read().strip().split('\n')
    directories = get_directories(data)

    print(f'Part 1: {sum([d for d in directories.values() if d <= 100000])}')

    used_space = directories['/']
    free_space = 70000000 - used_space
    required_space = 30000000 - free_space
    # sorted is asc order
    for size in sorted(directories.values()):
        if size >= required_space:
            print(f'Part 2: {size}')
            break
