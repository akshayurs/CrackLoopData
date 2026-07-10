The insight is that the minimum only ever changes at push and pop boundaries, so you can precompute it. Alongside the main stack, keep a second "min stack" whose top always holds the minimum of everything below and including the current top of the main stack. When you push `val`, push `min(val, previous_min)` onto the min stack; when you pop, pop both in lockstep.

Now `get_min` is just reading the top of the min stack — no scan. Because the two stacks grow and shrink together, the min stack's top is always in sync with the current contents, which turns the linear query into a constant-time lookup.

```python
class MinStack:
    def __init__(self):
        self._stack = []
        self._mins = []

    def push(self, val):
        self._stack.append(val)
        cur_min = val if not self._mins else min(val, self._mins[-1])
        self._mins.append(cur_min)

    def pop(self):
        self._stack.pop()
        self._mins.pop()

    def top(self):
        return self._stack[-1]

    def get_min(self):
        return self._mins[-1]
```

## Why it works

`_mins[i]` is invariant: it equals the minimum of the first `i + 1` values on the main stack. On push, the new minimum is either the new value or the old minimum, so `min(val, _mins[-1])` maintains it. On pop, removing the top of both stacks restores the exact state that existed one push earlier — including the correct minimum. Duplicate minimums are handled naturally: each push records its own min entry, so popping one copy leaves the other's entry intact.

## Complexity

- Time: O(1) for every operation, including `get_min`.
- Space: O(n) — the auxiliary min stack mirrors the main stack's size.
