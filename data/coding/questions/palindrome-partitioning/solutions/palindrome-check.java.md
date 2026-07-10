Explore every way to cut the string using backtracking: at each position, try every possible next piece, and only recurse into it if that piece is itself a palindrome. When the cut reaches the end of the string, the path taken so far is one valid partition.

Checking whether a candidate piece is a palindrome is done fresh every time with a simple two-pointer scan — no precomputation. Sorting the collected results at the end guarantees deterministic output.

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        backtrack(s, 0, new ArrayList<>(), result);
        result.sort((a, b) -> {
            for (int i = 0; i < Math.min(a.size(), b.size()); i++) {
                int cmp = a.get(i).compareTo(b.get(i));
                if (cmp != 0) return cmp;
            }
            return Integer.compare(a.size(), b.size());
        });
        return result;
    }

    private void backtrack(String s, int start, List<String> path, List<List<String>> result) {
        if (start == s.length()) {
            result.add(new ArrayList<>(path));
            return;
        }
        for (int end = start; end < s.length(); end++) {
            if (isPalindrome(s, start, end)) {
                path.add(s.substring(start, end + 1));
                backtrack(s, end + 1, path, result);
                path.remove(path.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
}
```

## Why it works

Every partition of `s` corresponds to a sequence of cut points; the backtracking loop tries each possible next cut in increasing order and only commits to it when the resulting piece is a palindrome, so every branch it explores is a valid prefix of a legal partition. Removing the last element of `path` after each recursive call undoes the choice so sibling branches start clean. Because the recursion only ever records a complete partition when it consumes the whole string, no partial or invalid partition ever lands in `result`.

## Complexity

- Time: O(n^2 * 2^n) — there are up to 2^(n-1) ways to place cuts, and each palindrome check costs up to O(n).
- Space: O(n) — recursion depth and the current `path`, excluding the output.
