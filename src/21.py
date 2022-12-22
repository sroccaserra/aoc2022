import fileinput
import re


OPS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
        }


def solve_1(monkeys):
    return shout(monkeys, 'root')


def shout(monkeys, name):
    value = monkeys[name]
    if is_shout_known(value):
        return int(value)
    parts = value.split()
    op = OPS[parts[1]]
    return op(shout(monkeys, parts[0]), shout(monkeys, parts[2]))


def is_shout_known(value):
    pattern = r'\+|-|\*|/'
    return not re.search(pattern, value)


monkey_info = [line.strip().split(': ') for line in fileinput.input()]
monkeys = {mi[0]: mi[1] for mi in monkey_info}
print(solve_1(monkeys))
