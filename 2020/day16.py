# import re
# from functools import partial

# with open('day16.txt', 'r') as f:
#     notes, ticket, nearby_tickets = f.read().split('\n\n')

# def validate(lo1, hi1, lo2, hi2, v):
#     return (lo1 <= v <= hi1) or (lo2 <= v <= hi2)

# def parse_rule(rule_str):
#     k, ranges = rule_str.split(': ')
#     ranges = map(int, re.findall(r'\d+', ranges))
#     return k, partial(validate, *ranges)

# def parse_ticket(ticket):
#     return list(map(int, ticket.split(',')))

# def valid(rules, value):
#     for _, in_range in rules:
#         if in_range(value):
#             break
#         else:
#             return False
#     return True

# def invalid_values(rules, ticket):
#     return sum([value for value in ticket if not valid(rules, value)])

# rules = list(map(parse_rule, notes.split('\n')))
# nearby_tickets = tuple(map(parse_ticket, nearby_tickets.splitlines()[1:]))

# count = partial(invalid_values, rules)
# print(sum(map(count, nearby_tickets)))

def part1(data):
    rules, my_ticket, nearby_tickets = data

    ans = 0
    for ticket in nearby_tickets:
        for num in ticket:
            check = False

            for ranges in rules.values():
                for from_num, to_num in ranges:
                    if from_num <= num <= to_num:
                        check = True

            if not check:
                ans += num
    return ans


def part2(data):
    rules, my_ticket, nearby_tickets = data

    # Possible fields of each position
    # e.g. [{'row'}, {'class', 'row'}, {'class', 'row', 'seat'}]
    possible_fields = [set() for _ in my_ticket]

    for ticket in nearby_tickets:
        for ix, num in enumerate(ticket):
            fields = set()

            for name, ranges in rules.items():
                for from_num, to_num in ranges:
                    if from_num <= num <= to_num:
                        fields.add(name)

            if fields:
                possible_fields[ix] = possible_fields[ix].intersection(fields) if possible_fields[ix] else fields

    # Sort by number of possible fields
    sorted_possible_fields = [
        [len(fields), ix, fields]
        for ix, fields in enumerate(possible_fields)
    ]
    sorted_possible_fields.sort()

    visited = set()
    ans = 1
    for ix, data in enumerate(sorted_possible_fields):
        length, index, fields = data

        # Tricky implementation here. I observe that fields[ix-1] is always the subset of fields[ix]
        # and is always off by 1.
        field_name = list(fields - visited)[0]
        if 'departure' in field_name:
            ans *= my_ticket[index]
        visited = visited.union(fields)

    return ans


def extract_data(lines):
    # rules
    # e.g.
    # {
    #     class: [(1, 2), (5, 7)]
    #     row: [(6, 11), (33, 44)]
    #     seat: [(13, 40), (45, 50)]
    # }
    ix = 0
    rules = {}
    while lines[ix]:
        name, ranges = lines[ix].split(':')
        ranges = map(str.strip, ranges.split('or'))
        int_ranges = []
        for r in ranges:
            from_num, to_num = r.split('-')
            int_ranges.append((int(from_num), int(to_num)))
        rules[name] = int_ranges
        ix += 1

    # My ticket
    # e.g. [7, 1, 14]
    ix += 2
    my_ticket = list(map(int, lines[ix].split(',')))

    # Nearby tickets
    # e.g.
    # [
    #     [7, 3, 47],
    #     [40, 4, 50],
    #     [55, 2, 20],
    #     [38, 6, 12],
    # ]
    ix += 2
    nearby_tickets = []
    for line in lines[ix+1:]:
        nearby_tickets.append(list(map(int, line.split(','))))

    return rules, my_ticket, nearby_tickets


with open('day16.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]

    print(part1(extract_data(inputs)))
    print(part2(extract_data(inputs)))
