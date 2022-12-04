m ← ⎕CSV('\W+'⎕R','⊢⊃⎕NGET'src/04.in'1)⍬4
a1 a2 b1 b2 ← ↓⍉m
⎕← +/0≥(a1-b1)×a2-b2
⎕← +/0≥(a1-b2)×a2-b1
