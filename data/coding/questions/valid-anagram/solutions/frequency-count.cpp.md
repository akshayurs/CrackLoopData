Anagrams are defined entirely by *how many* of each letter appear — order is irrelevant. So instead of sorting, tally the letters: add one for every character in `s` and subtract one for every character in `t`. If the two strings match, every count cancels back to zero.

Because the input is lowercase English letters, a fixed array of 26 slots serves as the frequency table — no hashing needed. A single sweep confirms that every bucket balances out.

```cpp
#include <string>
#include <array>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        array<int, 26> counts{};
        for (size_t i = 0; i < s.size(); i++) {
            counts[s[i] - 'a']++;
            counts[t[i] - 'a']--;
        }
        for (int c : counts) {
            if (c != 0) return false;
        }
        return true;
    }
};
```

## Why it works

Each letter maps to a slot `0..25`. Iterating both strings together, `s` increments its slot and `t` decrements the same kind of slot. If the strings are anagrams every letter is added and removed the same number of times, so all slots end at zero. Any leftover nonzero slot means one string has a surplus of that letter — not an anagram.

## Complexity

- Time: O(n) — one pass over the strings plus a constant 26-slot scan.
- Space: O(1) — a fixed 26-integer array regardless of input size.
