from fileinput import input
from collections import deque


def solve_1(blizzards, w, h):
    start = ((1, 0), 0)
    q = deque([start])
    seen = set([start])
    bs_hist = [blizzards]
    while q:
        ((x, y), d) = q.popleft()
        if x == w - 2 and y == h - 2:
            return d+1
        while len(bs_hist) < d+2:
            bs_last = bs_hist[-1]
            bs_hist.append(blow(bs_last, w, h))
        ns = neighbors(bs_hist[d+1], w, h, x, y)
        for n in ns:
            candidate = (n, d+1)
            if candidate in seen:
                continue
            seen.add(candidate)
            q.append(candidate)

    return None


def neighbors(blizzards, w, h, x, y):
    blocked = set([pos for (pos, _, _) in blizzards])
    result = []
    for n in ((x, y), (x+1, y), (x-1, y), (x, y+1), (x, y-1)):
        if n == (1, 0):
            result.append(n)
        elif n not in blocked and (0 < n[0] < w-1) and (0 < n[1] < h - 1):
            result.append(n)
    return result


def blow(blizzards, w, h):
    result = []
    for ((x, y), (dx, dy), c) in blizzards:
        x = x + dx
        if w-1 <= x:
            x = 1
        if x <= 0:
            x = w-2
        y = y + dy
        if h-1 <= y:
            y = 1
        if y <= 0:
            y = h-2
        result.append(((x, y), (dx, dy), c))
    return tuple(result)


DIRS = {'>': (1, 0), 'v': (0, 1), '<': (-1, 0), '^': (0, -1)}


def print_blizzards(blizzards, w, h):
    found = set()
    for y in range(h):
        for x in range(w):
            done = False
            for b in blizzards:
                if (x, y) == b[0] and (x, y) not in found:
                    print(b[2], end='')
                    found.add((x, y))
                    done = True
                    continue
            if not done:
                print('.', end='')
        print()
    print()


lines = [line.strip() for line in input()]
blizzard_list = []
w = len(lines[0])
h = len(lines)
for y in range(h):
    line = lines[y]
    for x in range(w):
        c = line[x]
        if c in '>v<^':
            blizzard_list.append(((x, y), DIRS[c], c))
blizzards = tuple(blizzard_list)
print(solve_1(blizzards, w, h))
