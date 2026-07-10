**Backtracking** is brute force with pruning: build a candidate solution one choice at a time, and the moment a partial choice can no longer lead to a valid answer, abandon it and try the next option. It systematically explores the full decision tree — every subset, every arrangement, every placement — without ever holding more than one path in memory at a time.

The shape is always the same: pick a choice, recurse into the smaller subproblem, then **undo the choice** before trying the next one. That undo step is what separates backtracking from plain recursion — it lets the same working array or path variable be reused across every branch instead of copying state at each level.

A typical skeleton:

```
function backtrack(path, choices):
    if path is a complete solution:
        record a copy of path
        return
    for choice in choices:
        if choice is invalid here:
            continue  # prune
        path.add(choice)
        backtrack(path, remaining choices)
        path.remove(choice)   # undo — the "backtrack" step
```

Two families of problems dominate: **combinatorial generation** (subsets, permutations, combinations — decide "include or skip" or "which one goes next") and **constraint search on a grid or board** (word search, N-Queens, Sudoku — decide "place here or not" and check constraints before recursing).

The naive tree is exponential, so the real skill is **pruning early** — checking validity before recursing rather than after, so whole subtrees are skipped instead of visited and rejected one leaf at a time.
