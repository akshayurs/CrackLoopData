Restarting the scan from every index repeats work. Instead keep one window with two pointers: push the right edge to gather characters, and once the window covers `t`, pull the left edge inward as far as possible while it still covers `t`. Each pointer only ever moves forward, so the whole string is traversed a constant number of times.

Track coverage with a single `missing` counter — the number of still-needed characters. Let `need` counts go negative to represent surplus copies; a character is "still needed" only while its count is strictly positive. When `missing` hits zero the current window is valid and we try to shrink it.

```cpp
#include <string>
#include <unordered_map>
#include <climits>
using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        if (t.empty() || t.size() > s.size()) return "";
        unordered_map<char, int> need;
        for (char c : t) need[c]++;
        int missing = (int)t.size();
        int left = 0, bestLeft = 0, bestLen = INT_MAX;
        for (int right = 0; right < (int)s.size(); right++) {
            char ch = s[right];
            if (need[ch] > 0) missing--;
            need[ch]--;
            while (missing == 0) {
                if (right - left + 1 < bestLen) { bestLeft = left; bestLen = right - left + 1; }
                char lc = s[left];
                need[lc]++;
                if (need[lc] > 0) missing++;
                left++;
            }
        }
        return bestLen == INT_MAX ? "" : s.substr(bestLeft, bestLen);
    }
};
```

## Why it works

Advancing `right` consumes a character; if it was one we still owed, `missing` drops. When `missing == 0` every required character is present, so we record the length and then release the leftmost character. Releasing raises its `need` count; only when it becomes positive again do we truly lose a required character, ending the shrink. Because both pointers march forward monotonically, every window boundary is examined once.

## Complexity

- Time: O(n + m) — each character enters and leaves the window at most once.
- Space: O(m) — the `need` map holds the distinct characters of `t`.
