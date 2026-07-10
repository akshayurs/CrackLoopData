Instead of picking all three cut points up front and validating afterward, build the address one octet at a time and abandon a branch the instant it can't possibly lead anywhere. At each step, try consuming 1, 2, or 3 characters for the next octet; skip a length immediately if it produces a leading zero or a value over 255, and skip the whole branch if the remaining characters can't be split into the remaining octets.

Because every octet is at most 3 digits and there are always exactly 4 of them, the search tree stays tiny regardless of the input length — the pruning turns what looks like exponential search into a small, fixed amount of work.

```cpp
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string digits) {
        results.clear();
        parts.clear();
        backtrack(digits, 0);
        sort(results.begin(), results.end());
        return results;
    }

private:
    vector<string> results;
    vector<string> parts;

    void backtrack(const string& digits, int start) {
        int n = digits.size();
        int remainingParts = 4 - (int)parts.size();
        int remainingChars = n - start;
        if (remainingChars < remainingParts || remainingChars > remainingParts * 3) return;
        if (parts.size() == 4) {
            if (start == n) {
                string address = parts[0] + "." + parts[1] + "." + parts[2] + "." + parts[3];
                results.push_back(address);
            }
            return;
        }

        for (int length = 1; length <= 3 && start + length <= n; length++) {
            string piece = digits.substr(start, length);
            if (piece[0] == '0' && length > 1) break;
            if (stoi(piece) > 255) break;
            parts.push_back(piece);
            backtrack(digits, start + length);
            parts.pop_back();
        }
    }
};
```

## Why it works

The `remainingChars` bound prunes any branch where the leftover string is too short or too long to fill the remaining octets, so hopeless prefixes are dropped before any recursion happens. Within a single octet, the loop stops as soon as a length is invalid (leading zero or value over 255), since a longer piece starting the same way can only be worse. `parts` is built and unwound in place, so each successful path down to 4 octets that exactly consumes the string is one valid address.

## Complexity

- Time: O(1) — each octet has at most 3 candidate lengths and there are always exactly 4 octets, so the search explores at most 3^4 branches no matter how long `digits` is.
- Space: O(n) — recursion depth is bounded by the string length, plus the output vector of matched addresses.
