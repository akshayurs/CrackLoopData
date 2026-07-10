The most direct plan: count how often each word shows up, then rank the distinct words by that count. A single comparator — frequency descending, word ascending — handles the ranking and the tie-break in one step.

Once the distinct words are ordered this way, the answer is just the first `k` of them.

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<string> topKFrequentWords(vector<string>& words, int k) {
        unordered_map<string, int> counts;
        for (auto& w : words) counts[w]++;

        vector<string> ordered;
        for (auto& [word, count] : counts) ordered.push_back(word);

        sort(ordered.begin(), ordered.end(), [&](const string& a, const string& b) {
            if (counts[a] != counts[b]) return counts[a] > counts[b];
            return a < b;
        });
        ordered.resize(k);
        return ordered;
    }
};
```

## Why it works

The comparator first orders by descending frequency; when two words tie, it falls back to plain string comparison, which puts the alphabetically smaller word first — exactly the tie-break the problem requires. Resizing to `k` after sorting gives the correct answer.

## Complexity

- Time: O(n log n) — counting is O(n); sorting the up-to-n distinct words dominates.
- Space: O(n) — the map and the ordered vector each hold up to n entries.
