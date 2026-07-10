Reversal is symmetric: the character at the front trades places with the one at the back, then you step inward. Put one pointer at the start and another at the end, swap the pair they point to, and march them toward each other until they meet in the middle.

Because every swap fixes two characters at once, you only need to walk halfway across the string. The string's own storage is mutable, so the extra memory is just the two indices.

```cpp
#include <string>
#include <utility>
using namespace std;

class Solution {
public:
    string reverseString(string s) {
        int left = 0, right = (int)s.size() - 1;
        while (left < right) {
            swap(s[left], s[right]);
            left++;
            right--;
        }
        return s;
    }
};
```

## Why it works

`left` and `right` bound the still-unreversed middle. Each iteration swaps the outermost unfixed pair and shrinks that window from both sides. When `left` meets or passes `right` every position has been placed, and a single middle character (odd length) is already where it belongs.

## Complexity

- Time: O(n) — each character is touched once across n/2 swaps.
- Space: O(1) — only two index variables beyond the output buffer.
