The blunt approach: any well-formed string of length `2n` is some arrangement of `n` opening and `n` closing brackets, so enumerate *every* binary sequence of that length and keep the ones that are balanced. Treat each of the `2n` positions as a bit that is either `(` or `)`, generate all `2^(2n)` candidates, and test each one.

A candidate is valid when scanning left to right never drives the running balance negative and it ends back at zero. Collect the survivors and sort them so the result is identical no matter the traversal order.

```cpp
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        int len = 2 * n;
        vector<string> result;
        for (int mask = 0; mask < (1 << len); mask++) {
            string seq;
            for (int i = 0; i < len; i++) {
                seq += (mask & (1 << i)) ? '(' : ')';
            }
            if (valid(seq)) result.push_back(seq);
        }
        sort(result.begin(), result.end());
        return result;
    }

private:
    bool valid(const string& seq) {
        int balance = 0;
        for (char ch : seq) {
            balance += ch == '(' ? 1 : -1;
            if (balance < 0) return false;
        }
        return balance == 0;
    }
};
```

## Why it works

Every valid combination is one of the `2^(2n)` bracket sequences, so exhaustively generating and filtering cannot miss any. The `valid` check enforces both well-formedness rules at once: `balance < 0` catches a closing bracket with no open partner, and a nonzero final balance catches unmatched openings. Sorting at the end guarantees a canonical, deterministic order.

## Complexity

- Time: O(2^(2n) · n) — every sequence is generated and scanned.
- Space: O(2^(2n) · n) — worst-case storage for the candidate strings.
