The simplest thing that works: keep a plain dictionary from key to value, letting a fresh `insert` naturally overwrite whatever was stored under that key before. For `sum`, there is no shortcut yet — walk every stored key, check whether it starts with the prefix, and add up the values of the ones that match.

This is easy to reason about and get right first, but every `sum` call redoes the prefix check for every key, which gets expensive once many keys share long common prefixes.

```python
class MapSum:
    def __init__(self):
        self.store = {}

    def insert(self, key: str, val: int) -> None:
        self.store[key] = val

    def sum(self, prefix: str) -> int:
        total = 0
        for key, val in self.store.items():
            if key.startswith(prefix):
                total += val
        return total
```

## Why it works

`self.store` always holds the *current* value for every key, because `insert` simply assigns `self.store[key] = val` — a repeated key replaces its old entry instead of adding a duplicate. `sum` then just filters: `str.startswith` correctly identifies every key that has `prefix` as its leading substring, and summing their (already up-to-date) values gives the right total, including the case where no key matches and the sum is 0.

## Complexity

- Time: O(1) for `insert`; O(n * L) for `sum`, where n is the number of stored keys and L is the average key length (each `startswith` check costs up to O(L)).
- Space: O(n * L) to store all keys and values.
