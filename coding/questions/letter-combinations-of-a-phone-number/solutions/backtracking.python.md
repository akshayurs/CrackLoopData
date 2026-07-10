Instead of rebuilding a whole list of partial results at every digit, grow one combination at a time in a shared buffer. Pick a letter for the current digit, recurse into the next digit, and once the buffer is as long as `digits` record it. When the recursive call returns, undo the last choice ("backtrack") and try the next letter.

This produces the same combinations as brute-force expansion but never materializes intermediate partial lists — only the final results and a single path buffer exist at once.

```python
def letter_combinations(digits):
    if not digits:
        return []

    keypad = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
    }
    result = []
    path = []

    def backtrack(index):
        if index == len(digits):
            result.append("".join(path))
            return
        for letter in keypad[digits[index]]:
            path.append(letter)
            backtrack(index + 1)
            path.pop()

    backtrack(0)
    return result
```

## Why it works

`path` always holds the letters chosen for digits `0..index-1`. At depth `index == len(digits)`, `path` is one complete combination, so it is recorded. Trying every letter of the current digit before returning, and popping after each recursive call, ensures every branch is explored and the buffer is restored for the sibling choice — so all `4^n` combinations are generated exactly once, none skipped, none duplicated.

## Complexity

- Time: O(4^n) — n is `len(digits)`; the recursion tree has one leaf per combination, and building each combination costs O(n).
- Space: O(n) beyond the output — the recursion depth and `path` buffer are bounded by `len(digits)`; the output list itself holds all combinations.
