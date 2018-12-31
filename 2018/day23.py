from collections import namedtuple
import networkx as nx
from parse import parse
import re

Nanobot = namedtuple('Nanobot', ['x', 'y', 'z', 'r'])
ORIGIN = namedtuple('Origin', ['x', 'y', 'z'])(0, 0, 0)

def manhattan_distance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)

def _parse(line):
    return list(parse('pos=<{:d},{:d},{:d}>, r={:d}', line))

if __name__ == '__main__':
    with open('day23.txt', 'r') as f:
        nanobots = [Nanobot(*_parse(line)) for line in f.read().splitlines()]

    strongest = max(nanobots, key=lambda bots: bots.r)
    c = 0
    for bot in nanobots:
        if manhattan_distance(bot, strongest) <= strongest.r:
            c += 1
    print(f'There are {c} nanobots in range of the strongest bot')

    graph = nx.Graph()
    for i, bot in enumerate(nanobots):
        # bots overlap if distance between them is lte the sum of their r's
        overlapping_bots = []
        for other in nanobots:
            if manhattan_distance(bot, other) <= (bot.r + other.r):
                overlapping_bots.append((bot, other))
            graph.add_edges_from(overlapping_bots)
        # this will take forever, so log some progress
        if (i + 1) % 25 == 0:
            print(f'Processed {i+1}/{len(nanobots)} bots')

    # find groups of overlapping bots (i.e. fully connected sub graphs)
    print('Find cliques')
    cliques = list(nx.find_cliques(graph))
    # select the largest cluster of overlapping nanobots (maximum clique sub-graph)
    clique = max(cliques, key=len)

    print(max([manhattan_distance(ORIGIN, bot) - bot.r for bot in clique]))
