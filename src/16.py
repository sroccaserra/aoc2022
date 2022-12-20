import fileinput
import re
from collections import deque


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
    distances = {src: NaD}
    q = deque([(src, 0)])
    while q:
        (name, d) = q.popleft()
        node = graph[name]
        for c in node[CHILDREN]:
            if c not in distances:
                new_dist = d + 1
                if c in to_open:
                    distances[c] = new_dist
                else:
                    distances[c] = NaD
                q.append((c, new_dist))
    farthest = 0
    for n in distances:
        d = distances[n]
        if farthest < d:
            farthest = d

    candidate = next(iter(to_open))
    max_gain = (candidate, distances[candidate])
    for (n, d) in distances.items():
        if d == NaD:
            continue
        target_t = farthest + OPENING_T
        pressure = graph[n][PRESSURE]
        released = (target_t - d - OPENING_T)*pressure
        if max_gain[1] < released:
            max_gain = (n, released)

    target_name = max_gain[0]
    return (target_name, distances[target_name])


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
NaD = -1


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
