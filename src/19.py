import fileinput
from collections import deque


MAX_TIME = 24

def solve_1(blueprints):
    quality_level = 0
    for blueprint in blueprints:
        max_geodes = find_max_geodes(blueprint)
        quality_level += max_geodes*blueprint['id']
    #     print(blueprint['id'], max_geodes)
    return quality_level


def find_max_geodes(blueprint):
    max_geodes = 0

    start_time = 0

    start_ore = 0
    start_clay = 0
    start_obsidian = 0
    start_geodes = 0

    start_ore_robots = 1
    start_clay_robots = 0
    start_obsidian_robots = 0
    start_geode_robots = 0

    ore_cost = blueprint['ore_cost']
    clay_cost = blueprint['clay_cost']
    (obsidian_ore_cost, obsidian_clay_cost) = blueprint['obsidian_cost']
    (geode_ore_cost, geode_obsidian_cost) = blueprint['geode_cost']

    q = ([(
        start_time,
        start_ore, start_clay, start_obsidian, start_geodes,
        start_ore_robots, start_clay_robots, start_obsidian_robots, start_geode_robots)])
    seen = set()
    max_len = 0
    to_beat = {}
    while q:
        # if len(q) > max_len:
        #     max_len = len(q)
        #     print(blueprint['id'], max_len, len(seen))
        current = q.pop()
        if current in seen:
            continue
        seen.add(current)
        (time, ore, clay, obsidian, geodes, ore_rs, clay_rs, obsidian_rs, geode_rs) = current
        if time not in to_beat:
            to_beat[time] = geodes
        elif to_beat[time] < geodes:
            to_beat[time] = geodes
        if geodes > max_geodes:
            max_geodes = geodes
        if MAX_TIME <= time:
            continue
        if geodes < to_beat[time]:
            continue
        if ore_cost <= ore:
            dt = 1
            new_ore = ore + ore_rs*dt - ore_cost
            new_clay = clay + clay_rs*dt
            new_obsidian = obsidian + obsidian_rs*dt
            new_geodes = geodes + geode_rs*dt
            q.append((
                time + dt,
                new_ore, new_clay, new_obsidian, new_geodes,
                ore_rs+1, clay_rs, obsidian_rs, geode_rs))
        if clay_cost <= ore:
            dt = 1
            new_ore = ore + ore_rs*dt - clay_cost
            new_clay = clay + clay_rs*dt
            new_obsidian = obsidian + obsidian_rs*dt
            new_geodes = geodes + geode_rs*dt
            q.append((
                time + dt,
                new_ore, new_clay, new_obsidian, new_geodes,
                ore_rs, clay_rs+1, obsidian_rs, geode_rs))
        if obsidian_ore_cost <= ore and obsidian_clay_cost <= clay:
            dt = 1
            new_ore = ore + ore_rs*dt - obsidian_ore_cost
            new_clay = clay + clay_rs*dt - obsidian_clay_cost
            new_obsidian = obsidian + obsidian_rs*dt
            new_geodes = geodes + geode_rs*dt
            q.append((
                time + dt,
                new_ore, new_clay, new_obsidian, new_geodes,
                ore_rs, clay_rs, obsidian_rs+1, geode_rs))
        if geode_ore_cost <= ore and geode_obsidian_cost <= obsidian:
            dt = 1
            new_ore = ore + ore_rs*dt - geode_ore_cost
            new_clay = clay + clay_rs*dt
            new_obsidian = obsidian + obsidian_rs*dt - geode_obsidian_cost
            new_geodes = geodes + geode_rs*dt
            q.append((
                time + dt,
                new_ore, new_clay, new_obsidian, new_geodes,
                ore_rs, clay_rs, obsidian_rs, geode_rs+1))
        else:
            dt = 1
            new_ore = ore + ore_rs*dt
            new_clay = clay + clay_rs*dt
            new_obsidian = obsidian + obsidian_rs*dt
            new_geodes = geodes + geode_rs*dt
            q.append((
                time + dt,
                new_ore, new_clay, new_obsidian, new_geodes,
                ore_rs, clay_rs, obsidian_rs, geode_rs))
    return max_geodes

def parse(line):
    words = line.split()
    parts = [words[1][:-1], words[6], words[12], words[18], words[21], words[27], words[30]]
    values = [int(s) for s in parts]
    return {
            'id': values[0],
            'ore_cost': values[1],
            'clay_cost': values[2],
            'obsidian_cost': (values[3], values[4]),
            'geode_cost': (values[5], values[6]),
            }


blueprints = [parse(line.strip()) for line in fileinput.input()]
print(solve_1(blueprints))
