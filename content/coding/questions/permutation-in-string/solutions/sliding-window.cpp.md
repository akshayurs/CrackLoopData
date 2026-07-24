Re-sorting every window throws away work: consecutive windows differ by only one character leaving and one entering. Track a running frequency count of a fixed-size window instead, and keep a `matches` counter of how many of the 26 letters currently have the exact count `s1` needs.

Slide the window one step at a time. When a character enters or leaves, update its count and adjust `matches` only for that letter. The moment all 26 letters match, the window is a permutation of `s1`.

```cpp
#include <string>
#include <array>
using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n = s1.size(), m = s2.size();
        if (n > m) return false;
        array<int, 26> need{}, win{};
        for (char c : s1) need[c - 'a']++;
        int matches = 0;
        for (int i = 0; i < 26; i++) if (need[i] == win[i]) matches++;
        for (int i = 0; i < m; i++) {
            int r = s2[i] - 'a';
            win[r]++;
            matches += win[r] == need[r] ? 1 : (win[r] == need[r] + 1 ? -1 : 0);
            if (i >= n) {
                int l = s2[i - n] - 'a';
                win[l]--;
                matches += win[l] == need[l] ? 1 : (win[l] == need[l] - 1 ? -1 : 0);
            }
            if (matches == 26) return true;
        }
        return false;
    }
};
```

## Why it works

`matches` counts how many letters have `win[c] == need[c]`. Each character add/remove changes one letter's count by one, so `matches` can only shift by one, and we update it in O(1): +1 when the count just became equal, -1 when it just left equality. Once the window holds exactly `n` characters, `matches == 26` means every letter's frequency equals `s1`'s — i.e. the window is a permutation.

## Complexity

- Time: O(m) — each character enters and leaves the window once; alphabet work is constant.
- Space: O(1) — two fixed 26-slot arrays.
