Instead of generating garbage and filtering it, build only strings that can still become valid. Track two counters as you grow the string: how many `(` you have placed and how many `)`. You may add a `(` whenever fewer than `n` have been opened, and you may add a `)` only when it would close an existing open bracket (closed < open). When the string reaches length `2n` it is guaranteed well-formed.

This prunes every dead branch the brute force wasted time on, so the recursion visits exactly the Catalan-number set of valid strings. Adding `(` before `)` at each step means the strings emerge in lexicographic order; a final sort makes that canonical order explicit and deterministic.

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        build(result, new StringBuilder(), 0, 0, n);
        Collections.sort(result);
        return result;
    }

    private void build(List<String> result, StringBuilder current,
                       int openCount, int closeCount, int n) {
        if (current.length() == 2 * n) {
            result.add(current.toString());
            return;
        }
        if (openCount < n) {
            current.append('(');
            build(result, current, openCount + 1, closeCount, n);
            current.deleteCharAt(current.length() - 1);
        }
        if (closeCount < openCount) {
            current.append(')');
            build(result, current, openCount, closeCount + 1, n);
            current.deleteCharAt(current.length() - 1);
        }
    }
}
```

## Why it works

The two guards encode the well-formedness invariant directly: never open more than `n` brackets, and never close one that was not opened. Any path that reaches length `2n` has therefore placed `n` opens and `n` valid closes, so it is well-formed by construction — no filtering needed. The append/delete pair restores the shared buffer after each branch so sibling paths start clean.

## Complexity

- Time: O(4^n / √n) — the number of valid strings is the nth Catalan number, and each takes O(n) to build.
- Space: O(n) — recursion depth is at most 2n (output not counted).
