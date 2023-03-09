import fileinput
import re
from copy import deepcopy


START_NODE = 'AA'
MAX_TIME = 30
OPENING_COST = 1


def solve_1(graph):
    graph = deepcopy(graph)
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


def solve_2(graph):
    graph = deepcopy(graph)
    compute_floyd_distances(graph)
    remove_useless_nodes(graph)
    start_time = 0
    start_moves = 0
    start_pressure = 0
    start_seen = set([START_NODE])
    max_time = MAX_TIME - 4
    stack = [(START_NODE, start_time, START_NODE, start_time, start_pressure, start_seen)]
    # stack = [('JJ', 3, 'DD', 2, 963, {'JJ', 'DD', 'AA'})]
    max_pressure = 0
    # nb_visited = 0
    # max_stack_len = len(stack)
    while stack:
        (node_me, time_me, node_el, time_el, pressure, seen) = stack.pop()
        if pressure > max_pressure:
            max_pressure = pressure
        #     print('new max:', max_pressure)
        # nb_visited += 1
        # if len(stack) > max_stack_len:
        #     max_stack_len = len(stack)
        # if 0 == nb_visited % 1_000_000:
        #     min_me_time = max_time
        #     min_el_time = max_time
        #     max_me_time = 0
        #     max_el_time = 0
        #     for (_, t_me, _, t_el, _, _) in stack:
        #         if t_me < min_me_time:
        #             min_me_time = t_me
        #         if t_el < min_el_time:
        #             min_el_time = t_el
        #         if max_me_time < t_me:
        #             max_me_time = t_me
        #         if max_el_time < t_el:
        #             max_el_time = t_el
        #     print(nb_visited, max_pressure, max_stack_len, len(stack), min_me_time, max_me_time, min_el_time, max_el_time)
        if time_me < time_el:
            open_me = True
            dests_me = graph[node_me]['neighbors']
            open_el = False
            dests_el = {node_el: time_el - time_me}
        elif time_el < time_me:
            open_me = False
            dests_me = {node_me: time_me - time_el}
            open_el = True
            dests_el = graph[node_el]['neighbors']
        else:
            open_me = True
            dests_me = graph[node_me]['neighbors']
            open_el = True
            dests_el = graph[node_el]['neighbors']
        for (dest_me, cost_me) in dests_me.items():
            for (dest_el, cost_el) in dests_el.items():
                if ((dest_me in seen) and (dest_el in seen)) or dest_me == dest_el:
                    continue
                if open_me:
                    new_time_me = time_me + cost_me + OPENING_COST
                else:
                    new_time_me = time_me
                if open_el:
                    new_time_el = time_el + cost_el + OPENING_COST
                else:
                    new_time_el = time_el
                if max_time <= new_time_me and max_time <= new_time_el:
                    continue
                new_pressure = pressure
                new_seen = seen.copy()
                if open_me and (dest_me not in seen) and new_time_me < max_time:
                    remaining_time_me = max_time - new_time_me
                    new_pressure += graph[dest_me]['rate']*remaining_time_me
                    new_seen.add(dest_me)
                if open_el and (dest_el not in seen) and new_time_el < max_time:
                    remaining_time_el = max_time - new_time_el
                    new_pressure += graph[dest_el]['rate']*remaining_time_el
                    new_seen.add(dest_el)
                stack.append((dest_me, new_time_me, dest_el, new_time_el, new_pressure, new_seen))
        # for i in stack: print(i)
        # print(graph.keys())
        # print(graph)
        # return max_pressure
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
print(solve_2(graph))
