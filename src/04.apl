ns ← ⎕CSV('\W+'⎕R','⊢⊃⎕NGET'src/04.in'1)⍬4
n1 n2 n3 n4 ← {,⍵/ns}¨↓∘.=⍨⍳4
x ← +/(n1 ≤ n3) ^ n4 ≤ n2
y ← +/(n3 ≤ n1) ^ n2 ≤ n4
z ← +/(n3 = n1) ^ n2 = n4
⎕← x+y-z
⎕← +/(n1 ≤ n4) ^ n3 ≤ n2
