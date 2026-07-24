Sort the catalog once so matches for any prefix already come out in the right order. Then, for every prefix of `searchWord` (length 1, 2, 3, ...), walk the sorted list and collect the first three entries that start with it.

This redoes a linear scan for every prefix, so it re-examines products you already ruled out on the previous, shorter prefix — simple, but wasteful once the query gets long.

```cpp
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> searchSuggestions(vector<string>& products, string searchWord) {
        sort(products.begin(), products.end());
        vector<vector<string>> result;
        string prefix;
        for (char ch : searchWord) {
            prefix += ch;
            vector<string> matches;
            for (const string& p : products) {
                if (p.compare(0, prefix.size(), prefix) == 0) {
                    matches.push_back(p);
                    if (matches.size() == 3) break;
                }
            }
            result.push_back(matches);
        }
        return result;
    }
};
```

## Why it works

Sorting the catalog once guarantees that any subset of matches, collected in vector order, is already lexicographically sorted — so taking the first three matches is always the three smallest. Comparing the growing prefix against each candidate correctly narrows the matches at each step, and stopping once 3 are found caps the suggestion list as required.

## Complexity

- Time: O(n log n + m * n * L) — one sort, then for each of the `m` prefix lengths a scan of `n` products with an O(L) prefix check.
- Space: O(n) — the output vectors (sorting is done in place).
