from collections import defaultdict


def parse_components():
    with open('day24.txt', 'r') as f:
        data = f.read().strip().split('\n')
    components = defaultdict(set)
    for component in data:
        a, b = component.split('/')
        components[int(a)].add(int(b))
        components[int(b)].add(int(a))
    return components


def generate_bridges(bridge, components):
    bridge = bridge or [(0, 0)]
    current_component = bridge[-1][1]
    for candidate_component in components[current_component]:
        if not ((current_component, candidate_component) in bridge or (candidate_component, current_component) in bridge):
            potential_bridge = bridge + [(current_component, candidate_component)]
            yield potential_bridge
            yield from generate_bridges(potential_bridge, components)


def run():
    components = parse_components()
    bridges = []
    for bridge in generate_bridges(None, components):
        bridges.append((len(bridge), sum(a + b for a, b in bridge)))
    return bridges

if __name__ == '__main__':
    bridges = run()
    print('Part 1: {}'.format(sorted(bridges, key=lambda x: x[1], reverse=True)[0][1]))
    print('Part 2: {}'.format(sorted(bridges, reverse=True)[1][1]))
