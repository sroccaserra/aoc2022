import fileinput
import re


START_NODE = 'AA'
MAX_TIME = 30
OPENING_COST = 1


def solve_1(graph):
    compute_floyd_distances(graph)
    remove_useless_nodes(graph)
    start_time = 0
    start_pressure = 0
    start_seen = set([START_NODE])
    stack = [(START_NODE, start_time, start_pressure, start_seen)]
    max_pressure = 0
    while stack:
        (node, time, pressure, seen) = stack.pop()
        if pressure > max_pressure:
            max_pressure = pressure
        for (dest, cost) in graph[node]['neighbors'].items():
            if dest in seen:
                continue
            new_time = time + cost + OPENING_COST
            if MAX_TIME <= new_time:
                continue
            remaining_time = MAX_TIME - new_time
            new_pressure = pressure + graph[dest]['rate']*remaining_time
            new_seen = seen.copy()
            new_seen.add(dest)
            stack.append((dest, new_time, new_pressure, new_seen))
    return max_pressure


def compute_floyd_distances(graph):
    names = graph.keys()
    huge = 9999999
    for k in names:
        neighbors_k = graph[k]['neighbors']
        for i in names:
            neighbors_i = graph[i]['neighbors']
            for j in names:
                neighbors_j = graph[j]['neighbors']
                by_k = neighbors_i.get(k, huge) + neighbors_k.get(j, huge)
                ij = neighbors_i.get(j, huge)
                if ij > by_k:
                    neighbors_i[j] = by_k


def remove_useless_nodes(graph):
    to_remove = set()
    for name, node in graph.items():
        if node['rate'] == 0:
            to_remove.add(name)
    for name in to_remove:
        if name != START_NODE:
            del graph[name]
    for name, node in graph.items():
        del node['neighbors'][name]
        for x in to_remove:
            node['neighbors'].pop(x, None)


def parse(line):
    words = line.split()
    rate = int(re.search(r'(\d+)', words[4]).group(0))
    return {'name': words[1], 'rate': rate, 'neighbors': {re.sub(',','', w): 1 for w in words[9:]}}


graph = {reading['name']: reading for reading in [parse(line.strip()) for line in fileinput.input()]}
print(solve_1(graph))
