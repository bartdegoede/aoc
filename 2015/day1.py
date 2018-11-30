

if __name__ == '__main__':
    with open('day1.txt', 'r') as f:
        instructions = f.read().strip()

    been_in_basement = False
    floor = 0
    for i, instruction in enumerate(instructions):
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1
        if floor < 0 and not been_in_basement:
            print(f'Enter basement at position {i + 1}')
            been_in_basement = True
    print(f'End at floor {floor}')
