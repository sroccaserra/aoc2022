import sys

NEXT = None

def solve_1(packets):
    result = 0
    for i in range(len(packets)):
        lhs, rhs = packets[i]
        # print(i+1, lhs, rhs)
        if are_in_order(lhs, rhs, {'n': 0}):
           result += 1+i
        # print('------')
    return result


def are_in_order(lhs, rhs, ctx):
    ctx['n'] += 1
    both_ints = isinstance(lhs, int) and isinstance(rhs, int)
    if both_ints:
        if lhs == rhs:
            # print(NEXT, lhs, rhs, ctx)
            return NEXT
        # print(lhs< rhs, lhs, rhs, ctx)
        return lhs < rhs
    lhs = coerce_list(lhs)
    rhs = coerce_list(rhs)
    common_len = min(len(lhs), len(rhs))
    for i in range(common_len):
        cmp = are_in_order(lhs[i], rhs[i], ctx)
        if cmp != NEXT:
            # print(cmp, lhs, rhs, ctx)
            return cmp
    if len(lhs) == len(rhs):
        return NEXT
    return len(lhs) < len(rhs)


def coerce_list(x):
    if isinstance(x, list):
        return x
    return [x]


infile = sys.argv[1] if len(sys.argv)>1 else 'src/13.in'
line_pairs = open(infile).read().strip().split('\n\n')
packets = []
for s in line_pairs:
    ls, rs = s.split('\n')
    packets.append((eval(ls), eval(rs)))

print(solve_1(packets))

"""
- If both values are integers, the lower integer should come first. If the left
  integer is lower than the right integer, the inputs are in the right order.
  If the left integer is higher than the right integer, the inputs are not in
  the right order. Otherwise, the inputs are the same integer; continue
  checking the next part of the input.
- If both values are lists, compare the first value of each list, then the
  second value, and so on. If the left list runs out of items first, the inputs
  are in the right order. If the right list runs out of items first, the inputs
  are not in the right order. If the lists are the same length and no
  comparison makes a decision about the order, continue checking the next part
  of the input.
- If exactly one value is an integer, convert the integer to a list which
  contains that integer as its only value, then retry the comparison. For
  example, if comparing [0,0,0] and 2, convert the right value to [2] (a list
  containing 2); the result is then found by instead comparing [0,0,0] and [2].
 """
