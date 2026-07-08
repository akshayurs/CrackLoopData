Start with the simplest thing that works: keep the values in one ordinary stack. Push, pop, and top are trivial list operations. The only interesting method is `get_min`, and the naive answer is to look at everything currently stored and take the smallest.

This is easy to reason about and obviously correct, but it pays for that simplicity on every `get_min` call — scanning the whole stack means the minimum query is linear, not constant.

```python
class MinStack:
    def __init__(self):
        self._stack = []

    def push(self, val):
        self._stack.append(val)

    def pop(self):
        self._stack.pop()

    def top(self):
        return self._stack[-1]

    def get_min(self):
        return min(self._stack)
```

## Why it works

A Python list used as a stack gives O(1) `append`, `pop`, and `[-1]`, so the LIFO behaviour is exactly right. `get_min` simply asks the built-in `min` for the smallest value among everything still on the stack, which is by definition the current minimum. Nothing extra is tracked, so there is no bookkeeping to get wrong.

## Complexity

- Time: O(1) for `push`, `pop`, `top`; O(n) for `get_min` — it inspects every element.
- Space: O(n) — the single stack holds all pushed values.
