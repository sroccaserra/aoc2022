⍝ (⎕NS⍬).(_←enableSALT⊣⎕CY'salt')
⍝ ]box on -style=max
⍝ ]rows on

asciiToPriority ← 58∘|20∘+
splitInTwo ←  ↓ 2∘,∘(÷∘2≢)⍴⊢

priorities ← asciiToPriority∘⎕UCS¨ ⊃⎕NGET'src/03.in'1
⎕← +/⊃∘(∪∘⊃∩/∘splitInTwo)¨ priorities
⎕← +/⊃∘∪¨↑∩/¨({3/⍳(÷∘3)≢⍵}⊆⊢) priorities
