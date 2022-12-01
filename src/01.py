import sys
import fileinput


def solve_1(elves):
    sums = [sum(e) for e in elves]
    return max(sums)


def solve_2(elves):
    sums = [sum(e) for e in elves]
    sums.sort()
    return sum(sums[-3:])


def parse(contents):
    elves = []
    elf = []
    for line in contents:
        if line == '':
            elves.append(elf)
            elf = []
        else:
            elf.append(int(line))

    return elves


if __name__ == '__main__' and not sys.flags.interactive:
    contents = [line.strip() for line in fileinput.input()]
    elves = parse(contents)
    print(solve_1(elves))
    print(solve_2(elves))
