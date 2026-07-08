Keep a stack of bar indices whose heights are strictly increasing. As long as the stack rises, we don't yet know how far right each bar can extend. The moment a shorter bar arrives, every taller bar on the stack is "closed off" on the right — so pop it and settle its rectangle: its height is the popped bar's height, and its width runs from just after the new stack top up to the current index.

A trailing sentinel of height `0` forces every remaining bar to be popped and measured at the end. Each bar is pushed and popped once, giving a single linear scan.

```python
def largest_rectangle_area(heights):
    stack = []
    best = 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            best = max(best, height * width)
        stack.append(i)
    return best
```

## Why it works

When bar `i` is shorter than the stack's top, that top bar can extend no further right than `i - 1`, and no further left than the index just above the new top (all bars between are taller). So its maximal rectangle has width `i - stack[-1] - 1`, or `i` if the stack empties (it reached the far left). The `0` sentinel guarantees the stack drains, so every bar's rectangle is evaluated exactly once.

## Complexity

- Time: O(n) — each index is pushed and popped at most once.
- Space: O(n) — the stack holds up to n indices.
