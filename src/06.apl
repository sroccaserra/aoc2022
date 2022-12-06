solve ← {(⍺-1)+⍺⍳⍨≢∘∪¨⍺,/⍵}

line ← ⊃⊃⎕NGET'src/06.in'1
⎕← 4 solve line
⎕← 14 solve line
