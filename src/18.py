import fileinput
from collections import Counter


def solve_1(cubes):
    face_counter = Counter()
    for cube in cubes:
        new_faces = faces(cube)
        face_counter.update(faces(cube))
    result = 0
    for (_, cnt) in face_counter.items():
        if cnt == 1:
            result += 1
    return result


def faces(cube):
    (x, y, z) = cube
    return [(cube, 'up'), (cube, 'right'), (cube, 'front'),
            ((x, y-1, z), 'up'), ((x-1, y, z), 'right'), ((x, y, z+1), 'front')]


cubes = [tuple([int(w) for w in line.strip().split(',')]) for line in fileinput.input()]
print(solve_1(cubes))
