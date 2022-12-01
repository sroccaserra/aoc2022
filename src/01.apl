solve1 ← {⌈/⍵ }
solve2 ← {+/3↑⍵[⍒⍵]}

sums ← (+/⍎¨)¨ ((×≢¨)⊆⊢) ⊃⎕NGET'src/01.in'1
⎕ ← solve1 sums
⎕ ← solve2 sums
