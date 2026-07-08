Anagrams share one property that survives rearrangement: sort their letters and they become identical. So the sorted form of a string is a fingerprint that every member of a group agrees on — `"eat"`, `"tea"`, and `"ate"` all sort to `"aet"`.

Use that fingerprint as an `unordered_map` key. Walk the vector once, sort a copy of each string to get its key, and push the original string into the bucket for that key. The bucket values are the answer.

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> buckets;
        for (const string& s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            buckets[key].push_back(s);
        }
        vector<vector<string>> result;
        for (auto& entry : buckets) result.push_back(move(entry.second));
        return result;
    }
};
```

## Why it works

Two strings are anagrams exactly when their multisets of characters match, and sorting canonicalizes that multiset into a single comparable string. Strings with the same sorted key land in the same bucket; strings with different letters never collide. Because we push the original (unsorted) string, each group preserves the input words.

## Complexity

- Time: O(n · k log k) — for n strings of max length k, each sort costs O(k log k).
- Space: O(n · k) — every character is stored once across the buckets.
