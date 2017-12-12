class Node(object):
    def __init__(self, name, connected_to):
        self.name = name
        self.connected_to = connected_to

    def __repr__(self):
        return 'Node <{}>: {}'.format(self.name, self.connected_to)


def find_connected_nodes(graph, root=0):
    group = set([root])
    new = set([root])
    while new:
        connections = set()
        for item in new:
            connections.update(graph[item])
        # this will find the connections we didn't know about already
        new = connections - group
        # add any unknown connections to the group
        group.update(connections)
    return group

if __name__ == '__main__':
#     programs = """0 <-> 2
# 1 <-> 1
# 2 <-> 0, 3, 4
# 3 <-> 2, 4
# 4 <-> 2, 3, 6
# 5 <-> 6
# 6 <-> 4, 5"""
    nodes = {}
    with open('day12.txt', 'r') as f:
        for program in f:
            node, connected_to = program.split(' <-> ')
            nodes[int(node)] = [int(n) for n in connected_to.split(', ')]

    print 'Part 1:', len(find_connected_nodes(nodes))

    programs = set(nodes.keys())
    groups = 0
    while programs:
        groups += 1
        # find next group in the remaining programs
        prog = programs.pop()
        group = find_connected_nodes(nodes, prog)
        programs -= group # gotta love Python sets
    print 'Part 2:', groups
