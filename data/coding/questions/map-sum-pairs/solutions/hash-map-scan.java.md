The simplest thing that works: keep a plain `HashMap` from key to value, letting a fresh `insert` naturally overwrite whatever was stored under that key before. For `sum`, there is no shortcut yet — walk every stored key, check whether it starts with the prefix, and add up the values of the ones that match.

This is easy to reason about and get right first, but every `sum` call redoes the prefix check for every key, which gets expensive once many keys share long common prefixes.

```java
import java.util.HashMap;
import java.util.Map;

class MapSum {
    private final Map<String, Integer> store = new HashMap<>();

    public void insert(String key, int val) {
        store.put(key, val);
    }

    public int sum(String prefix) {
        int total = 0;
        for (Map.Entry<String, Integer> entry : store.entrySet()) {
            if (entry.getKey().startsWith(prefix)) {
                total += entry.getValue();
            }
        }
        return total;
    }
}
```

## Why it works

`store` always holds the *current* value for every key, because `insert` simply calls `put(key, val)` — a repeated key overwrites its old entry instead of adding a duplicate. `sum` then just filters: `String.startsWith` correctly identifies every key that has `prefix` as its leading substring, and summing their (already up-to-date) values gives the right total, including the case where no key matches and the sum is 0.

## Complexity

- Time: O(1) for `insert`; O(n * L) for `sum`, where n is the number of stored keys and L is the average key length (each `startsWith` check costs up to O(L)).
- Space: O(n * L) to store all keys and values.
