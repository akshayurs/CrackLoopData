Sorting each string is more work than the problem needs. What actually defines an anagram group is the count of each of the 26 lowercase letters — not their order. So build a fixed 26-length count array for each string and use *that* as the key, skipping the O(k log k) sort entirely.

Serialize the counts into a `string` so it can key an `unordered_map`. Every anagram produces the same serialized counts, so the grouping matches the sort approach but each key costs only a linear pass over the string.

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <array>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> buckets;
        for (const string& s : strs) {
            array<int, 26> counts{};
            for (char ch : s) counts[ch - 'a']++;
            string key;
            for (int c : counts) { key += to_string(c); key += '#'; }
            buckets[key].push_back(s);
        }
        vector<vector<string>> result;
        for (auto& entry : buckets) result.push_back(move(entry.second));
        return result;
    }
};
```

## Why it works

Two strings are anagrams if and only if their per-letter frequency vectors are equal, so the serialized 26-count string is a perfect canonical key. Building it scans the string once — no comparison sort. The `#` separator keeps multi-digit counts unambiguous. Identical vectors collide into one bucket; any difference in even a single letter's count yields a different key and a separate group.

## Complexity

- Time: O(n · k) — n strings, each scanned once in O(k); building the 26-length key is O(k + 26).
- Space: O(n · k) — the stored strings dominate; each key is a constant 26 entries.
