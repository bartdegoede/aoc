def declines(number):
    i = 0
    j = 1
    while j < len(number):
        if int(number[j]) < int(number[i]):
            return True
        i += 1
        j += 1
    return False

def doubles(number):
    for digit in number:
        if number.count(digit) >= 2:
            return True
    return False


def more_than_double(number):
    # not exactly more than doubles, but we'll use it in conjunction with
    # the other criteria, so eh
    for digit in number:
        if number.count(digit) == 2:
            return False
    return True


def is_valid(number):
    if declines(number):
        return False
    if not doubles(number):
        return False
    return True

if __name__ == '__main__':
    cnt = 0
    cnt2 = 0
    for i in range(165432, 707913):
        if is_valid(str(i)):
            cnt += 1
            if not more_than_double(str(i)):
                cnt2 += 1
    print(f'Part 1: {cnt}')
    print(f'Part 2: {cnt2}')
