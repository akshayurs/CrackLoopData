The blunt approach: any well-formed string of length `2n` is some arrangement of `n` opening and `n` closing brackets, so enumerate *every* binary sequence of that length and keep the ones that are balanced. Treat each of the `2n` positions as a bit that is either `(` or `)`, generate all `2^(2n)` candidates, and test each one.

A candidate is valid when scanning left to right never drives the running balance negative and it ends back at zero. Collect the survivors and sort them so the result is identical no matter the traversal order.

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        int len = 2 * n;
        for (int mask = 0; mask < (1 << len); mask++) {
            StringBuilder seq = new StringBuilder();
            for (int i = 0; i < len; i++) {
                seq.append((mask & (1 << i)) != 0 ? '(' : ')');
            }
            if (valid(seq.toString())) result.add(seq.toString());
        }
        Collections.sort(result);
        return result;
    }

    private boolean valid(String seq) {
        int balance = 0;
        for (char ch : seq.toCharArray()) {
            balance += ch == '(' ? 1 : -1;
            if (balance < 0) return false;
        }
        return balance == 0;
    }
}
```

## Why it works

Every valid combination is one of the `2^(2n)` bracket sequences, so exhaustively generating and filtering cannot miss any. The `valid` check enforces both well-formedness rules at once: `balance < 0` catches a closing bracket with no open partner, and a nonzero final balance catches unmatched openings. Sorting at the end guarantees a canonical, deterministic order.

## Complexity

- Time: O(2^(2n) · n) — every sequence is generated and scanned.
- Space: O(2^(2n) · n) — worst-case storage for the candidate strings.
