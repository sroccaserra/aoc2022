import fileinput
import re


# LINENO = 10
LINENO = 2000000


def solve_1(readings):
    segments = []
    beacons = []
    min_x = 999999999999999999
    max_x = 0
    for (x1, y1, x2, y2) in readings:
        d = distance(x1, y1, x2, y2)
        if y2 == LINENO:
            beacons.append(x2)
        toline = abs(y1 - LINENO)
        if toline <= d:
            amplitude = d - toline
            segments.append((x1-amplitude, x1+amplitude))
            min_x = min(x1 - amplitude, min_x)
            max_x = max(x1 + amplitude, max_x)
    result = 0
    for x in range(min_x, max_x+1):
        for (x1, x2) in segments:
            if x1 <= x <= x2 and x not in beacons:
                # print(x1, x, x2)
                result +=1
                break
    return result


def distance(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)


readings = [[int(s) for s in re.findall(r'=([-0-9]+)', line.strip())] for line in fileinput.input()]
print(solve_1(readings))
