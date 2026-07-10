Start from the definition: try every substring and keep the longest one whose characters are all distinct. Fix a left endpoint, then extend the right endpoint one character at a time, tracking the characters seen so far in a set.

The moment a character repeats inside the current window, that starting point can grow no further, so we break and move the left endpoint forward.

```cpp
#include <string>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int best = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            unordered_set<char> seen;
            for (int j = i; j < (int)s.size(); j++) {
                if (seen.count(s[j])) break;
                seen.insert(s[j]);
                best = max(best, j - i + 1);
            }
        }
        return best;
    }
};
```

## Why it works

For each start index `i`, the inner loop grows the window until it hits a duplicate, which is exactly the longest duplicate-free substring beginning at `i`. Taking the maximum over all starts covers every candidate, so the true answer is never missed.

## Complexity

- Time: O(n²) — n start positions, each scanning up to n characters before a repeat.
- Space: O(min(n, k)) — the set holds distinct characters, bounded by the alphabet size k.
