import collections

def problem1():
    with open('day7.txt', 'r') as f:
        lefts = set()
        rights = set()
        for line in f:
            d = line.split(' -> ')
            if len(d) > 1:
                lefts.update([d[0].split()[0]])
                rights.update(d[1].strip().split(', '))


class Program(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []

    def is_balanced(self):
        return len(set([st.total_weight() for st in self.children])) == 1 or not self.children

    def total_weight(self):
        return self.weight + sum([st.total_weight() for st in self.children])

    def __repr__(self):
        return 'Program "{}" ({})'.format(self.name, self.total_weight())


def solve(programs, root='eqgvf'):
    parent = programs[root]
    children = parent.children

    offending_diff = None

    while True:
        weights = collections.Counter(w.total_weight() for w in children)
        weights = weights.most_common()

        if len(weights) == 1:
            # found it! nodes are balanced now, and there's only one
            # imbalanced node, which must be the parent
            break

        if offending_diff is None:
            offending_diff = weights[1][0] - weights[0][0]

        offending_weight = weights[1][0]

        offender = next(child for child in children if child.total_weight() == weights[1][0])

        parent = offender
        children = offender.children

    result = parent.weight - offending_diff
    print result
    print parent

if __name__ == '__main__':
    programs = {}
    with open('day7.txt', 'r') as f:
        lines = [line.strip() for line in f]

    for line in lines:
        d = line.split(')')[0].split()
        programs[d[0]] = Program(name=d[0], weight=int(d[1].replace('(', '')))

    for line in lines:
        d = line.split(' -> ')
        if len(d) > 1:
            program = programs[d[0].split()[0]]
            for child in d[1].split(', '):
                program.children.append(programs[child])
