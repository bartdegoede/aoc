class Node(object):
    def __init__(self, sequence):
        self.number_of_children, self.metadata_count = sequence[:2]
        sequence = sequence[2:]
        self.children = []
        for _ in range(self.number_of_children):
            node = Node(sequence)
            self.children.append(node)
            sequence = sequence[node.size:]
        self.metadata = sequence[:self.metadata_count]

    @property
    def size(self):
        return 2 + self.metadata_count + sum([n.size for n in self.children])

    @property
    def total(self):
        return sum(self.metadata + [c.total for c in self.children])

    @property
    def value(self):
        if self.children:
            value = 0
            for entry in self.metadata:
                idx = entry - 1 # friggin 1-indexing
                if idx < len(self.children):
                    value += self.children[idx].value
            return value
        else:
            return sum(self.metadata)

if __name__ == '__main__':
    with open('day8.txt', 'r') as f:
        sequence = list(map(int, f.read().strip().split()))

    tree = Node(sequence)
    print(f'Sum of metadata entries: {tree.total}')
    print(f'Value of the root node: {tree.value}')
