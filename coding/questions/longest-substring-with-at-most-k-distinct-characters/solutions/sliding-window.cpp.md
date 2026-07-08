Instead of restarting for every start index, keep one window that slides across the string. Grow it on the right by adding characters; whenever it holds more than `k` distinct characters, shrink it from the left until it is valid again. Each character enters and leaves the window at most once.

A count map keyed by character reports the window's distinct-character count as its size. Track the widest valid window seen.

```cpp
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        if (k == 0) return 0;
        unordered_map<char, int> counts;
        int best = 0;
        int left = 0;
        for (int right = 0; right < (int)s.size(); right++) {
            counts[s[right]]++;
            while ((int)counts.size() > k) {
                char leftCh = s[left];
                if (--counts[leftCh] == 0) counts.erase(leftCh);
                left++;
            }
            best = max(best, right - left + 1);
        }
        return best;
    }
};
```

## Why it works

`counts` always describes the current window `s[left..right]`, and its size is the distinct-character count. After each right-side addition, the `while` loop restores the "at most `k` distinct" invariant by dropping characters from the left, erasing a key when its count reaches zero. Since `left` and `right` only advance, each character is added and removed at most once, and every measured window is valid — so the maximum width is the answer.

## Complexity

- Time: O(n) — left and right pointers each traverse the string once.
- Space: O(k) — the map holds at most k + 1 distinct characters.
