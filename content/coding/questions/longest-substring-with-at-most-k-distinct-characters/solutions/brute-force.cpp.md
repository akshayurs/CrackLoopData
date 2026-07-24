Start from the definition directly: try every starting index, extend the substring one character at a time, and track how many distinct characters the current window holds. The moment the window would exceed `k` distinct characters, abandon that start and move on.

This examines every substring, so it is quadratic, but it maps straight onto the problem statement and makes a clean baseline before optimizing.

```cpp
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        if (k == 0) return 0;
        int best = 0;
        int n = (int)s.size();
        for (int start = 0; start < n; start++) {
            unordered_map<char, int> counts;
            for (int end = start; end < n; end++) {
                counts[s[end]]++;
                if ((int)counts.size() > k) break;
                best = max(best, end - start + 1);
            }
        }
        return best;
    }
};
```

## Why it works

Fixing `start` and growing `end` enumerates every substring beginning at `start`. The `counts` map tracks distinct characters in the window; once it exceeds `k`, all longer windows from the same start are invalid too, so breaking early is safe. The running maximum over valid windows yields the answer.

## Complexity

- Time: O(n^2) — up to n starts, each scanning up to n characters.
- Space: O(k) — the map holds at most k + 1 distinct characters.
