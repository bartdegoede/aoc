if __name__ == '__main__':
    with open('day2.txt', 'r') as f:
        all_dimensions = f.read().strip()

    total = 0
    total_length = 0
    for dimensions in all_dimensions.split('\n'):
        l, w, h = [int(x) for x in dimensions.split('x')]
        total += sum([2*l*w, 2*w*h, 2*h*l, min([l*w, w*h, h*l])])

        total_length += sum([x*2 for x in sorted([l, w, h])[:2]])
        res = 1
        for x in [l, w, h]:
            res *= x
        total_length += res

    print(f'Wrapping paper needed {total} sqft')
    print(f'Length of ribbon needed {total_length} ft')
