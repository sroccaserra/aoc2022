⍝ (⎕NS⍬).(_←enableSALT⊣⎕CY'salt')
⍝ ]box on -style=max
⍝ ]rows on

asciiToPriority ← 58∘|20∘+
splitInTwo ← {↓2(2÷⍨≢⍵)⍴⍵}
chunkByThree ← {3/⍳3÷⍨≢⍵}⊆⊢
findUniqueCommons ← ⊃∘∪¨∘↑∩/¨

priorities ← asciiToPriority∘⎕UCS¨ ⊃⎕NGET'src/03.in'1
⎕← +/ findUniqueCommons splitInTwo¨ priorities
⎕← +/ findUniqueCommons chunkByThree priorities
