A substring can be turned into a single repeated letter when the number of letters that are *not* the most common one is at most `k` — those are exactly the positions you would overwrite. So fix a start index, extend the substring one letter at a time, and while extending keep a running count of each letter and the highest count seen. If `window - maxCount <= k`, this window is achievable, so record its length.

Trying every start index and extending to the end checks all substrings without ever building them explicitly.

```cpp
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = (int)s.size();
        int best = 0;
        for (int i = 0; i < n; i++) {
            vector<int> counts(26, 0);
            int maxCount = 0;
            for (int j = i; j < n; j++) {
                int idx = s[j] - 'A';
                counts[idx]++;
                maxCount = max(maxCount, counts[idx]);
                int window = j - i + 1;
                if (window - maxCount <= k) {
                    best = max(best, window);
                }
            }
        }
        return best;
    }
};
```

## Why it works

For a fixed window, `window - maxCount` is the count of the least-needed letters, which is the minimum number of replacements to make the whole window one letter. When that value is within `k`, the window is valid. The outer loop anchors every possible start; the inner loop grows the window and updates counts incrementally, so each candidate substring is evaluated in O(1) extra work.

## Complexity

- Time: O(n²) — n start positions, each extended up to n times; the 26-slot count update is constant.
- Space: O(1) — a fixed array of 26 counters.
