import fileinput


def solve(commands):
    vm = {'X': 1, 'ticks': 0}
    probe = []
    for command in commands:
        if command[0] == 'noop':
            tick(vm, probe)
        if command[0] == 'addx':
            for _ in range(2):
                tick(vm, probe)
            vm['X'] += command[1]
    return sum(probe)


def tick(vm, probe):
    vm['ticks'] += 1
    if (vm['ticks'] +20)% 40 == 0:
        probe.append(vm['ticks']*vm['X'])


lines = [line.strip() for line in fileinput.input()]
commands = []
for line in lines:
    parts = line.split()
    if len(parts) > 1:
        commands.append((parts[0], int(parts[1])))
    else:
        commands.append((line,))
print(solve(commands))
