import fileinput
from collections import deque


INITIAL = 'o'
MOVED = 'x'


def solve_1(numbers):
    size = len(numbers)
    moved = [(INITIAL, n) for n in numbers]
    p = 0
    for _ in range(size):
        while True:
            (status, n) = moved[p]
            if status == INITIAL:
                break
            p = (p + 1)%size
        src = p
        nb_moves = n%(size-1)
        if nb_moves == 0:
            moved[src] = (MOVED, n)
        for _ in range(nb_moves):
            dst = (src+1)%size
            tmp = moved[dst]
            moved[dst] = (MOVED, n)
            moved[src] = tmp
            src = dst
    for (status, _) in moved:
        assert status == MOVED

    offset = 0
    for (_, n) in moved:
        if n == 0:
            break
        offset += 1
    (_, a) = moved[(1000+offset)%size]
    (_, b) = moved[(2000+offset)%size]
    (_, c) = moved[(3000+offset)%size]
    return a + b + c


numbers = [int(line.strip()) for line in fileinput.input()]
print(solve_1(numbers))
