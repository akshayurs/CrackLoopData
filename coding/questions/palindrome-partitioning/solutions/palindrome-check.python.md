Explore every way to cut the string using backtracking: at each position, try every possible next piece, and only recurse into it if that piece is itself a palindrome. When the cut reaches the end of the string, the path taken so far is one valid partition.

Checking whether a candidate piece is a palindrome is done fresh every time with a simple string comparison — no precomputation. Sorting the collected results at the end guarantees deterministic output.

```python
def partition_palindromes(s):
    n = len(s)
    result = []
    path = []

    def is_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def backtrack(start):
        if start == n:
            result.append(path[:])
            return
        for end in range(start, n):
            if is_palindrome(start, end):
                path.append(s[start:end + 1])
                backtrack(end + 1)
                path.pop()

    backtrack(0)
    result.sort()
    return result
```

## Why it works

Every partition of `s` corresponds to a sequence of cut points; the backtracking loop tries each possible next cut in increasing order and only commits to it when the resulting piece is a palindrome, so every branch it explores is a valid prefix of a legal partition. Popping `path` after each recursive call undoes the choice so sibling branches start clean. Because the recursion only ever appends a complete partition when it consumes the whole string, no partial or invalid partition ever lands in `result`.

## Complexity

- Time: O(n^2 * 2^n) — there are up to 2^(n-1) ways to place cuts, and each palindrome check costs up to O(n).
- Space: O(n) — recursion depth and the current `path`, excluding the output.
