⍝ (⎕NS⍬).(_←enableSALT⊣⎕CY'salt')
⍝ ]box on -style=max
⍝ ]rows on

asciiToPriority ← 58∘|20∘+
splitInTwo ←  ↓ 2∘,∘(÷∘2≢)⍴⊢

lines ← ⊃⎕NGET'src/03.in'1
⎕← +/ ⊃∘asciiToPriority∘⎕UCS¨(∪∘⊃∩/∘splitInTwo)¨ lines
⎕← +/ ⊃∘↑∘asciiToPriority∘⎕UCS¨∪¨↑∩/¨({3/⍳(÷∘3)≢⍵}⊆⊢)lines
