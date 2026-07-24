Start with a list holding just the empty string, and grow it one digit at a time. For each digit, take every combination built so far and append each of that digit's letters to it, producing a brand-new, larger vector. After the last digit, the vector holds every full combination.

It is the most direct translation of "multiply out the possibilities" and needs no recursion, but it keeps rebuilding a fresh vector at every step.

```cpp
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> combinations;
        if (digits.empty()) {
            return combinations;
        }

        vector<string> keypad = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        combinations.push_back("");

        for (char digit : digits) {
            const string& letters = keypad[digit - '0'];
            vector<string> next;
            for (const string& prefix : combinations) {
                for (char letter : letters) {
                    next.push_back(prefix + letter);
                }
            }
            combinations = next;
        }

        return combinations;
    }
};
```

## Why it works

`combinations` is an invariant: after processing the first `k` digits, it holds exactly every combination for those `k` digits, in keypad order. Each step multiplies its size by the number of letters on the next digit, and every existing prefix is extended by every letter — so no combination is missed and none is duplicated.

## Complexity

- Time: O(4^n) — n is `digits.size()`; the vector size (and work to build it) grows by a factor of up to 4 per digit.
- Space: O(4^n) — every intermediate vector, up to the final one, is kept in memory.
