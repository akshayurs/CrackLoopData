The simplest thing that works: keep a plain `unordered_map` from key to value, letting a fresh `insert` naturally overwrite whatever was stored under that key before. For `sum`, there is no shortcut yet — walk every stored key, check whether it starts with the prefix, and add up the values of the ones that match.

This is easy to reason about and get right first, but every `sum` call redoes the prefix check for every key, which gets expensive once many keys share long common prefixes.

```cpp
#include <string>
#include <unordered_map>
using namespace std;

class MapSum {
public:
    void insert(string key, int val) {
        store[key] = val;
    }

    int sum(string prefix) {
        int total = 0;
        for (const auto& entry : store) {
            const string& key = entry.first;
            if (key.size() >= prefix.size() && key.compare(0, prefix.size(), prefix) == 0) {
                total += entry.second;
            }
        }
        return total;
    }

private:
    unordered_map<string, int> store;
};
```

## Why it works

`store` always holds the *current* value for every key, because `insert` simply assigns `store[key] = val` — a repeated key overwrites its old entry instead of adding a duplicate. `sum` then just filters: comparing the leading `prefix.size()` characters of each key against `prefix` correctly identifies every key that starts with it, and summing their (already up-to-date) values gives the right total, including the case where no key matches and the sum is 0.

## Complexity

- Time: O(1) for `insert`; O(n * L) for `sum`, where n is the number of stored keys and L is the average key length (each comparison costs up to O(L)).
- Space: O(n * L) to store all keys and values.
