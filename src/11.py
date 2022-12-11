import fileinput
from collections import deque


def solve(monkeys):
    for _ in range(20):
        for monkey in monkeys:
            step(monkeys, monkey)
    inspections = [m['inspections'] for m in monkeys]
    inspections.sort()
    inspections.reverse()
    return inspections[0]*inspections[1]


def step(monkeys, monkey):
    items = monkey['items']
    while items:
        monkey['inspections'] += 1
        item = items.popleft()
        item = monkey['operation'](item)//3
        if item % monkey['test'] == 0:
            dst = monkey['next_t']
        else:
            dst = monkey['next_f']
        monkeys[dst]['items'].append(item)


lines = [line.strip() for line in fileinput.input()]
monkeys = []
while True:
    n = len(monkeys)
    start = n*7
    if start > len(lines):
        break
    items = deque([int(s) for s in lines[start + 1].split(': ')[1].split(', ')])
    expr = lines[start+2].split('= ')[1]
    operation = lambda old, expr=expr: eval(expr.replace('old', str(old)))
    test = int(lines[start+3][19:])
    next_t = int(lines[start+4][25:])
    next_f = int(lines[start+5][26:])
    monkey = {
            'n': n,
            'items': items,
            'operation': operation,
            'test': test,
            'next_t': next_t,
            'next_f': next_f,
            'inspections': 0,
            }
    monkeys.append(monkey)
print(solve(monkeys))
