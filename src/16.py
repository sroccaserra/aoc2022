import fileinput
import re
from collections import deque


def compute_distances(graph, nodes, indexes):
    n = len(nodes)
    dists = []
    for _ in range(n):
        dists.append([99999]*n)
    for i in range(n):
        node = nodes[i]
        dists[i][i] = 0
        for c in graph[node][CHILDREN]:
            dists[i][indexes[c]] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dists[i][j] > dists[i][k]+dists[k][j]:
                    dists[i][j] = dists[i][k]+dists[k][j]
    return dists


def solve_1(graph):
    opened = set()
    to_open = set()
    for name in graph:
        if graph[name][PRESSURE] > 0:
            to_open.add(name)
    result = 0
    src = 'AA'
    n = len(to_open)
    t = 0
    target_time = 30
    for _ in range(len(to_open)):
        time_left = target_time - t
        (target_name, ticks) = find_target(graph, time_left, to_open, src)
        ticks += OPENING_T
        print(time_left, graph[target_name]) # wrong order here, should be d b j h e c, actual is d b j e h c
        if t + ticks > target_time:
            ticks = target_time - t
        for o in opened:
            result += o*(ticks)
        t += ticks
        opened.add(graph[target_name][PRESSURE])
        to_open.remove(target_name)
        src = target_name
    for o in opened:
        result += o*(target_time-t)

    return result


def find_target(graph, time_left, to_open, src):
    farthest = 0
    for n in to_open:
        d = distance(src, n)
        if d != NaD:
            assert distance(src, n) == d
        if farthest < d:
            farthest = d

    candidate = next(iter(to_open))
    max_gain = (candidate, distance(src, candidate))
    target_t = farthest + OPENING_T
    for n in to_open:
        d = distance(src, n)
        if d == 0:
            continue
        pressure = graph[n][PRESSURE]
        released = (target_t - d - OPENING_T)*pressure
        if max_gain[1] < released:
            max_gain = (n, released)

    target_name = max_gain[0]
    return (target_name, distance(src, target_name))


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


def distance(src, dst):
    i = INDEXES[src]
    j = INDEXES[dst]
    return DISTS[i][j]


NAME = 0
PRESSURE = 1
CHILDREN = 2
OPENING_T = 1
TICK = 1
NaD = -1


def parse(line):
    words = line.split()
    rate = int(re.search(r'(\d+)', words[4]).group(0))
    return (words[1], rate, [re.sub(',','', w) for w in words[9:]])


readings = [parse(line.strip()) for line in fileinput.input()]
graph = {}
for reading in readings:
    graph[reading[NAME]] = reading
NODES = list(graph.keys())
NODES.sort()
INDEXES = {}
for i in range(len(NODES)):
    INDEXES[NODES[i]] = i
DISTS = compute_distances(graph, NODES, INDEXES)
print(NODES)
print(DISTS)
print(solve_1(graph))
