asciiToPriority ← ⊣-{⍵>90:96⋄38}
splitInTwo ←  ↓ 2∘,∘(÷∘2≢)⍴⊢

lines ← ⊃⎕NGET'src/03.in'1
⎕← +/ asciiToPriority∘⎕UCS¨(∪∘⊃∩/∘splitInTwo)¨ lines
