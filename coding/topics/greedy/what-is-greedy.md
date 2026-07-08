A **greedy algorithm** builds a solution step by step, and at every step it takes the choice that looks best *right now* — the largest reach, the earliest finish time, the cheapest cost — without ever revisiting that choice later. There is no backtracking and no trying every alternative; you commit and move on.

That works only when the problem has a **greedy-choice property**: the locally optimal pick is always part of *some* globally optimal solution. Proving this (even informally, out loud in an interview) is the real skill — the code itself is usually a short loop.

Most greedy solutions follow one of two shapes. Either you **sort first** by some key (end time, ratio, size) and then sweep once, or you scan the array while tracking a **running best** (furthest reach so far, current running total) and update it as you go.

A typical sort-then-sweep shape:

```
sort items by some key
result = initial value
for each item in sorted order:
    if item fits the current state:
        take it, update result and state
    else:
        skip it, or close out the current group
return result
```

Greedy is fast — usually O(n log n) for the sort, O(n) for the sweep — and simple to code. The catch is that it is easy to write a greedy solution that *compiles and runs* but is wrong on some input, because the greedy-choice property was assumed rather than verified. When in doubt, test the greedy rule against a small adversarial example before trusting it.
