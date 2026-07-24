An IP address always has exactly three dots, so it always has exactly three "cut points" inside the digit string. The most direct approach is to try every combination of three cut positions with three nested loops, slice out the four resulting pieces, and keep the combination only if all four pieces are legal octets.

It never looks more than one string ahead — no recursion, no early exit — so it re-validates a lot of dead-end prefixes, but it is the natural first attempt.

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public List<String> restoreIpAddresses(String digits) {
        int n = digits.length();
        List<String> results = new ArrayList<>();

        for (int i = 1; i < Math.min(4, n); i++) {
            for (int j = i + 1; j < Math.min(i + 4, n); j++) {
                for (int k = j + 1; k < Math.min(j + 4, n); k++) {
                    String a = digits.substring(0, i);
                    String b = digits.substring(i, j);
                    String c = digits.substring(j, k);
                    String d = digits.substring(k);
                    if (isValid(a) && isValid(b) && isValid(c) && isValid(d)) {
                        results.add(a + "." + b + "." + c + "." + d);
                    }
                }
            }
        }

        Collections.sort(results);
        return results;
    }

    private boolean isValid(String piece) {
        if (piece.isEmpty() || piece.length() > 3) return false;
        if (piece.charAt(0) == '0' && piece.length() > 1) return false;
        return Integer.parseInt(piece) <= 255;
    }
}
```

## Why it works

Every valid split is uniquely described by the lengths of its first three octets, so scanning `i < j < k` over the string's index range enumerates every possible four-way partition exactly once. `isValid` rejects empty pieces, pieces longer than three digits, values above 255, and leading zeros on multi-digit pieces — the three conditions that make an octet malformed. Bounding each loop to at most 3 steps ahead keeps the search from wasting time on octets that could never be valid anyway.

## Complexity

- Time: O(n^3) — three nested loops over cut positions, each iteration doing O(1) validation since every piece is at most 3 characters.
- Space: O(1) extra beyond the output list.
