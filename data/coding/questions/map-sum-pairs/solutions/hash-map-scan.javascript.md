The simplest thing that works: keep a plain `Map` from key to value, letting a fresh `insert` naturally overwrite whatever was stored under that key before. For `sum`, there is no shortcut yet — walk every stored key, check whether it starts with the prefix, and add up the values of the ones that match.

This is easy to reason about and get right first, but every `sum` call redoes the prefix check for every key, which gets expensive once many keys share long common prefixes.

```javascript
class MapSum {
  constructor() {
    this.store = new Map();
  }

  insert(key, val) {
    this.store.set(key, val);
  }

  sum(prefix) {
    let total = 0;
    for (const [key, val] of this.store) {
      if (key.startsWith(prefix)) {
        total += val;
      }
    }
    return total;
  }
}
```

## Why it works

`this.store` always holds the *current* value for every key, because `insert` simply calls `set(key, val)` — a repeated key overwrites its old entry instead of adding a duplicate. `sum` then just filters: `String.prototype.startsWith` correctly identifies every key that has `prefix` as its leading substring, and summing their (already up-to-date) values gives the right total, including the case where no key matches and the sum is 0.

## Complexity

- Time: O(1) for `insert`; O(n * L) for `sum`, where n is the number of stored keys and L is the average key length (each `startsWith` check costs up to O(L)).
- Space: O(n * L) to store all keys and values.
