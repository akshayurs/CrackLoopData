Reach for a stack the moment a problem sounds like any of these:

- **"Valid" / "balanced" brackets, tags, or parentheses** — push opens, pop and match on close. Any nesting-validity check is a matching stack.
- **"Next greater/smaller element"** — for every element, find the next one to its left/right that is bigger or smaller. This is the monotonic-stack signature almost verbatim.
- **"Daily temperatures" / "how many days until warmer"** — a next-greater problem in disguise; the stack holds indices waiting for their answer.
- **Histogram / "largest rectangle" / "trapping water" shapes** — you need, for each bar, how far it extends before something shorter blocks it. Monotonic stack finds that boundary in one pass.
- **Evaluate an expression** (RPN, calculator, decode a nested string like `3[a2[c]]`) — operators/operands or nesting levels naturally live on a stack.
- **"Span" problems** ("how many consecutive prior days were ≤ today's price") — Online Stock Span keeps a monotonic stack of (value, span) pairs.
- **Simplify a path / undo-redo / matching function calls** — anything where the *most recent unresolved thing* must be resolved first.
- **Asteroid/collision-style simulation** — items moving toward each other where only the most recent still-alive item can collide with the next.

Signal words: *"valid"*, *"balanced"*, *"nested"*, *"next greater"*, *"next smaller"*, *"span"*, *"until a warmer/taller/bigger one"*, *"evaluate the expression"*. If you catch yourself wanting to look backward for "the nearest unmatched X," that backward search is what a stack replaces with O(1) top access.
