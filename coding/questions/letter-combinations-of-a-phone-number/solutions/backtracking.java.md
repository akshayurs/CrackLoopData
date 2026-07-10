Instead of rebuilding a whole list of partial results at every digit, grow one combination at a time in a shared buffer. Pick a letter for the current digit, recurse into the next digit, and once the buffer is as long as `digits` record it. When the recursive call returns, undo the last choice ("backtrack") and try the next letter.

This produces the same combinations as brute-force expansion but never materializes intermediate partial lists — only the final results and a single path buffer exist at once.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final String[] KEYPAD =
        {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits.isEmpty()) {
            return result;
        }
        backtrack(digits, 0, new StringBuilder(), result);
        return result;
    }

    private void backtrack(String digits, int index, StringBuilder path, List<String> result) {
        if (index == digits.length()) {
            result.add(path.toString());
            return;
        }
        String letters = KEYPAD[digits.charAt(index) - '0'];
        for (char letter : letters.toCharArray()) {
            path.append(letter);
            backtrack(digits, index + 1, path, result);
            path.deleteCharAt(path.length() - 1);
        }
    }
}
```

## Why it works

`path` always holds the letters chosen for digits `0..index-1`. At depth `index == digits.length()`, `path` is one complete combination, so it is recorded. Trying every letter of the current digit before returning, and deleting the last character after each recursive call, ensures every branch is explored and the buffer is restored for the sibling choice — so all `4^n` combinations are generated exactly once, none skipped, none duplicated.

## Complexity

- Time: O(4^n) — n is `digits.length()`; the recursion tree has one leaf per combination, and building each combination costs O(n).
- Space: O(n) beyond the output — the recursion depth and `path` buffer are bounded by `digits.length()`; the output list itself holds all combinations.
