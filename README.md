- <http://adventofcode.com/2022>

See also:

- <https://github.com/sroccaserra/aoc2015#learnings>
- <https://github.com/sroccaserra/aoc2018#learnings>
- <https://github.com/sroccaserra/aoc2019#learnings>
- <https://github.com/sroccaserra/aoc2020#learnings>
- <https://github.com/sroccaserra/aoc2021#learnings>

## Learnings

- Floyd–Warshall algorithm: algorithm for finding shortest paths in a directed
  weighted graph ~
  <https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm>

- When we have to explore all / most possibilities without a good pruning
  strategy, a DFS uses much less memory than a BFS

- [Day 16][day16] [comment / spoiler][src16]: after having kept only the nodes
  with valves to open, explore all possibilities to open all valves with a
  buddy elephant is like partitioning the set of valves to open in two disjoint
  subsets. There was only 15 valves to open in my input. The number of
  interesting ways to split a set of 15 elements is 2<sup>15</sup>/2 = 16384.
  Then for a given split, we can search for the max independently, which is
  like applying part one to each subset. With a fairly efficient part one (eg.
  a DFS that avoids already known states), it is good enough.

[day16]: https://adventofcode.com/2022/day/16
[src16]: /sroccaserra/aoc2022/blob/main/src/16.py
