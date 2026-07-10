Instead of generating garbage and filtering it, build only strings that can still become valid. Track two counters as you grow the string: how many `(` you have placed and how many `)`. You may add a `(` whenever fewer than `n` have been opened, and you may add a `)` only when it would close an existing open bracket (closed < open). When the string reaches length `2n` it is guaranteed well-formed.

This prunes every dead branch the brute force wasted time on, so the recursion visits exactly the Catalan-number set of valid strings. Adding `(` before `)` at each step means the strings emerge in lexicographic order; a final sort makes that canonical order explicit and deterministic.

```python
def generate_parenthesis(n):
    result = []

    def build(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            build(current + "(", open_count + 1, close_count)
        if close_count < open_count:
            build(current + ")", open_count, close_count + 1)

    build("", 0, 0)
    return sorted(result)
```

## Why it works

The two guards encode the well-formedness invariant directly: never open more than `n` brackets, and never close one that was not opened. Any path that reaches length `2n` has therefore placed `n` opens and `n` valid closes, so it is well-formed by construction — no filtering needed. Because both choices are explored, every valid string is produced exactly once.

## Complexity

- Time: O(4^n / √n) — the number of valid strings is the nth Catalan number, and each takes O(n) to build.
- Space: O(n) — recursion depth is at most 2n (output not counted).
