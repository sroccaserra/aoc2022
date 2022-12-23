import fileinput
import re


R = 0
D = 1
L = 2
U = 3


def solve_1(grid, commands):
    w = max([len(line) for line in grid])
    h = len(grid)
    pos = find_start(grid)
    state = (pos, R)
    for command in commands:
        state = apply_command(grid, state, command)
    row = state[0][0]+1
    col = state[0][1]+1
    d = state[1]
    return 1000*row + col*4 + d


def apply_command(grid, state, command):
    pos, d = state
    if 'L' == command:
        d = (d - 1) % 4
    elif 'R' == command:
        d = (d + 1) % 4
    else:
        n = int(command)
        fn = {R: get_next_j, D: get_next_i, L: get_prev_j, U: get_prev_i}[d]
        for _ in range(n):
            i, j = fn(grid, pos[0], pos[1])
            if grid[i][j] == '.':
                pos = (i, j)

    return (pos, d)


def get_next_j(grid, i, j):
    line = grid[i]
    candidate = j + 1
    while True:
        if len(line) <= candidate:
            candidate = 0
        if line[candidate] != ' ':
            break
        candidate += 1
    return (i, candidate)


def get_prev_j(grid, i, j):
    line = grid[i]
    candidate = j - 1
    while True:
        if candidate < 0:
            candidate = len(line)-1
        if line[candidate] != ' ':
            break
        candidate -= 1
    return (i, candidate)


def get_next_i(grid, i, j):
    candidate = i + 1
    while True:
        if len(grid) <= candidate:
            candidate = 0
        if grid[candidate][j] != ' ':
            break
        candidate += 1
    return (candidate, j)


def get_prev_i(grid, i, j):
    candidate = i - 1
    while True:
        if candidate < 0:
            candidate = len(grid)-1
        if grid[candidate][j] != ' ':
            break
        candidate -= 1
    return (candidate, j)


def find_start(grid):
    return get_next_j(grid, 0, 0)


lines = [line[:-1] for line in fileinput.input()]
w = len(lines[0])
grid = [line.ljust(w, ' ') for line in lines[:-2]]
commands = re.split(r'([0-9]+)', lines[-1])[1:-1]
print(solve_1(grid, commands))
