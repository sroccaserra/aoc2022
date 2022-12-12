import fileinput
from collections import deque


def solve_1(heights):
    w = len(heights[0])
    h = len(heights)
    start = None
    end = None
    for y in range(h):
        for x in range(w):
            c = heights[y][x]
            if c == ord('S'):
                start = (x, y)
                heights[y][x] = ord('a')
            if c == ord('E'):
                end = (x, y)
                heights[y][x] = ord('z')
    return find_distance(heights, start, end)


def find_distance(heights, start, end):
    w = len(heights[0])
    h = len(heights)
    q = deque([start])
    distances = {start: 0}
    while q:
        node = q.popleft()
        distance = distances[node]
        if node == end:
            return distances[node]
        cs = children(heights, w, h, node)
        for c in cs:
            if c not in distances:
                distances[c] = distance + 1
                print(c, distance+1)
                q.append(c)
    raise Exception('Not found')


def children(heights, w, h, coords):
    x, y = coords
    result = []
    n = heights[y][x]
    for d in [-1, 1]:
        xc = x + d
        if (0 <= xc < w) and heights[y][xc] <= n + 1:
            result.append((xc, y))
        yc = y + d
        if 0 <= yc < h and heights[yc][x] <= n + 1:
            result.append((x, yc))
    return result

lines = [line.strip() for line in fileinput.input()]
heights = [[ord(c) for c in line] for line in lines]
print(solve_1(heights))
