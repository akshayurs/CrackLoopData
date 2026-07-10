Start with a list holding just the empty string, and grow it one digit at a time. For each digit, take every combination built so far and append each of that digit's letters to it, producing a brand-new, larger list. After the last digit, the list holds every full combination.

It is the most direct translation of "multiply out the possibilities" and needs no recursion, but it keeps rebuilding a fresh list at every step.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> combinations = new ArrayList<>();
        if (digits.isEmpty()) {
            return combinations;
        }

        String[] keypad = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        combinations.add("");

        for (char digit : digits.toCharArray()) {
            String letters = keypad[digit - '0'];
            List<String> next = new ArrayList<>();
            for (String prefix : combinations) {
                for (char letter : letters.toCharArray()) {
                    next.add(prefix + letter);
                }
            }
            combinations = next;
        }

        return combinations;
    }
}
```

## Why it works

`combinations` is an invariant: after processing the first `k` digits, it holds exactly every combination for those `k` digits, in keypad order. Each step multiplies its size by the number of letters on the next digit, and every existing prefix is extended by every letter — so no combination is missed and none is duplicated.

## Complexity

- Time: O(4^n) — n is `digits.length()`; the list size (and work to build it) grows by a factor of up to 4 per digit.
- Space: O(4^n) — every intermediate list, up to the final one, is kept in memory.
