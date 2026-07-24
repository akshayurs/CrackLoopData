Consecutive windows overlap almost entirely: sliding one step right drops a single character on the left and adds one on the right. So instead of rebuilding the count each time, keep a running 26-slot frequency array for the current window and patch it in O(1) per move. Track how many of the 26 letters currently match the target count exactly; when all 26 agree, the window is an anagram.

Maintaining a single `matches` counter avoids re-scanning all 26 buckets on every step, keeping each slide constant work.

```cpp
#include <vector>
#include <string>
#include <array>
using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int m = p.size(), n = s.size();
        vector<int> result;
        if (m > n) return result;
        array<int, 26> need{}, win{};
        for (char c : p) need[c - 'a']++;
        int matches = 0;
        for (int v : need) if (v == 0) matches++;
        for (int i = 0; i < n; i++) {
            int r = s[i] - 'a';
            win[r]++;
            if (win[r] == need[r]) matches++;
            else if (win[r] == need[r] + 1) matches--;
            if (i >= m) {
                int l = s[i - m] - 'a';
                win[l]--;
                if (win[l] == need[l]) matches++;
                else if (win[l] == need[l] - 1) matches--;
            }
            if (matches == 26) result.push_back(i - m + 1);
        }
        return result;
    }
};
```

## Why it works

`matches` counts how many of the 26 letters have `win[c] == need[c]`. Adding the incoming character and removing the outgoing one each touch a single bucket, so `matches` only changes when that bucket crosses into or out of equality. Once the window is full width and all 26 buckets agree, its letters are exactly those of `p`, making `i - m + 1` a valid start. The left-to-right scan yields ascending indices.

## Complexity

- Time: O(n) — one pass; every character enters and leaves the window once with O(1) bookkeeping.
- Space: O(1) — two fixed arrays of 26 counts.
