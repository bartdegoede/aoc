import string

def polymer_length(p):
    p1 = 0
    p2 = 1

    while p2 < len(p):
        if p[p1].swapcase() == p[p2]:
            p = p[:p1] + p[p2+1:]
            # indices will change (i.e. characters will move "back")
            if p1 > 0:
                p1 -= 1
            else:
                p1 = 0
            p2 = p1 + 1
        else:
            p1 += 1
            p2 += 1

    return len(p)

if __name__ == '__main__':
    with open('day5.txt', 'r') as f:
        polymer = f.read().strip()

    print(f'Polymer length part 1: {polymer_length(polymer)}')

    pairs = []
    for letter in string.ascii_lowercase:
        pairs.append(polymer_length(polymer.replace(letter, '').replace(letter.swapcase(), '')))

    print(f'Polymer length part 2: {min(pairs)}')
