The direct reading of the problem: try every starting index, then extend the window rightward until it first covers `t`, and remember the shortest cover seen. Once a start position produces a valid window we can stop extending it — growing further only makes that window longer.

Counting requirements with a frequency map lets us compare "how many of each character we have" against "how many we need," so duplicates in `t` are handled correctly.

```cpp
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        if (t.empty() || t.size() > s.size()) return "";
        unordered_map<char, int> need;
        for (char c : t) need[c]++;
        string best = "";
        for (int i = 0; i < (int)s.size(); i++) {
            unordered_map<char, int> window;
            for (int j = i; j < (int)s.size(); j++) {
                window[s[j]]++;
                bool ok = true;
                for (auto& p : need) {
                    if (window[p.first] < p.second) { ok = false; break; }
                }
                if (ok) {
                    if (best.empty() || j - i + 1 < (int)best.size())
                        best = s.substr(i, j - i + 1);
                    break;
                }
            }
        }
        return best;
    }
};
```

## Why it works

`need` records how many copies of each character the window must contain. For a fixed start `i`, we widen the end `j` and stop the instant every requirement is met — that is the shortest valid window beginning at `i`. Comparing lengths across all starts yields the global minimum, and scanning starts left-to-right keeps the earliest window on ties.

## Complexity

- Time: O(n^2) — every start extends across the rest of the string; the coverage check touches only the distinct characters of `t`.
- Space: O(m) — the two frequency maps, where m = t.size().
