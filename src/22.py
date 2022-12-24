import fileinput
import re


R = 0
D = 1
L = 2
U = 3
FACE_SIZE = 50
N_FACE_COLS = 3

NO_CHANGE = None
NO_CONF = None
CONFT_2 = (2, [(11,), (6, NO_CHANGE), (5,), (4,)])
CONFT_4 = (4, [(5, NO_CHANGE), (10,), (11,), (2,)])
CONFT_5 = (5, [(6, NO_CHANGE), (10,), (4, NO_CHANGE), (2,)])
CONFT_6 = (6, [(11,), (10, NO_CHANGE), (5, NO_CHANGE), (2, NO_CHANGE)])
CONFT10 = (10, [(4,), (11, NO_CHANGE), (5,), (6, NO_CHANGE)])
CONFT11 = (11, [(4,), (2,), (10, NO_CHANGE), (6,)])

TEST_CONF = (
        NO_CONF, NO_CONF, CONFT_2, NO_CONF,
        CONFT_4, CONFT_5, CONFT_6, NO_CONF,
        NO_CONF, NO_CONF, CONFT10, CONFT11)

CONF_01 = (1, [(1,), (1,), (1,), (1,)])
CONF_02 = (2, [(1,), (1,), (1,), (1,)])
CONF_04 = (4, [(1,), (1,), (1,), (1,)])
CONF_06 = (6, [(1,), (1,), (1,), (1,)])
CONF_07 = (7, [(1,), (1,), (1,), (1,)])
CONF_09 = (9, [(1,), (1,), (1,), (1,)])

CONF_4 = (4, [(11,), (6,), (5,), (4,)])
CONF = (NO_CONF, CONF_01, CONF_02,
        NO_CONF, CONF_04, NO_CONF,
        CONF_06, CONF_07, NO_CONF,
        CONF_09, NO_CONF, NO_CONF)


def solve_1(grid, commands):
    pos = find_start(grid)
    state = (pos, R)
    for command in commands:
        state = apply_command(grid, state, command)
    row = state[0][0]+1
    col = state[0][1]+1
    d = state[1]
    return 1000*row + col*4 + d


def solve_2(grid, commands):
    w = max([len(line) for line in grid])
    h = len(grid)
    for i in range(h):
        for j in range(max(w, 16)):
            n = face_n(i, j)
            s = '{}'.format(n)
            conf = CONF[n]
            if conf is None:
                s = '.'
            else:
                s = '{}'.format(conf[0])
            print(s.rjust(3, ' '), end='')
        print()
    return 0


def face_n(i, j):
    return N_FACE_COLS*(i//FACE_SIZE)+j//FACE_SIZE


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
if w == 12:
    FACE_SIZE = 4
    N_FACE_COLS = 4
    CONF = TEST_CONF
grid = [line.ljust(w, ' ') for line in lines[:-2]]
commands = re.split(r'([0-9]+)', lines[-1])[1:-1]
print(solve_1(grid, commands))
print(solve_2(grid, commands))
