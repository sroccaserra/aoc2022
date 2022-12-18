import fileinput
import re
from collections import deque


def solve_1(graph):
    opened = set()
    src = 'AA'
    target = find_target(graph, src)
    return target


def find_target(graph, src):
    distances = {'AA': 0}
    q = deque([('AA', 0)])
    while q:
        (name, d) = q.popleft()
        node = graph[name]
        for c in node[CHILDREN]:
            if c not in distances:
                new_dist = d + 1
                if graph[c][PRESSURE] > 0:
                    distances[c] = new_dist
                else:
                    distances[c] = -1
                q.append((c, new_dist))
    priorities = {}
    farthest = 0
    for n in distances:
        d = distances[n]
        if farthest < d:
            farthest = d

    max_gain = ('', 0)
    for (n, d) in distances.items():
        target_t = farthest + OPENING_T + TICK
        pressure = graph[n][PRESSURE]
        released = (target_t - d - OPENING_T)*pressure
        if max_gain[1] < released:
            max_gain = (n, released)

    return max_gain


def print_mermaid(graph):
    print('graph TD')
    keys = list(graph.keys())
    keys.sort()
    for name in keys:
        print('{}[{} {}]'.format(name, name, graph[name][PRESSURE]))

    seen = set()
    for name in keys:
        node = graph[name]
        for c in node[CHILDREN]:
            edge = [name, c]
            edge.sort()
            if tuple(edge) not in seen:
                seen.add(tuple(edge))
                print(name, '---', c)


NAME = 0
PRESSURE = 1
CHILDREN = 2
OPENING_T = 1
TICK = 1


def parse(line):
    words = line.split()
    rate = int(re.search(r'(\d+)', words[4]).group(0))
    return (words[1], rate, [re.sub(',','', w) for w in words[9:]])


readings = [parse(line.strip()) for line in fileinput.input()]
graph = {}
for reading in readings:
    graph[reading[NAME]] = reading
# print_mermaid(graph)
print(solve_1(graph))
