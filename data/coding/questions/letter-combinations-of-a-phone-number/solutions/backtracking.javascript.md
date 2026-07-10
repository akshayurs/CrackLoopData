Instead of rebuilding a whole array of partial results at every digit, grow one combination at a time in a shared buffer. Pick a letter for the current digit, recurse into the next digit, and once the buffer is as long as `digits` record it. When the recursive call returns, undo the last choice ("backtrack") and try the next letter.

This produces the same combinations as brute-force expansion but never materializes intermediate partial arrays — only the final results and a single path buffer exist at once.

```javascript
function letterCombinations(digits) {
  if (digits.length === 0) return [];

  const keypad = {
    2: "abc", 3: "def", 4: "ghi", 5: "jkl",
    6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz",
  };
  const result = [];
  const path = [];

  function backtrack(index) {
    if (index === digits.length) {
      result.push(path.join(""));
      return;
    }
    for (const letter of keypad[digits[index]]) {
      path.push(letter);
      backtrack(index + 1);
      path.pop();
    }
  }

  backtrack(0);
  return result;
}
```

## Why it works

`path` always holds the letters chosen for digits `0..index-1`. At depth `index === digits.length`, `path` is one complete combination, so it is recorded. Trying every letter of the current digit before returning, and popping after each recursive call, ensures every branch is explored and the buffer is restored for the sibling choice — so all `4^n` combinations are generated exactly once, none skipped, none duplicated.

## Complexity

- Time: O(4^n) — n is `digits.length`; the recursion tree has one leaf per combination, and building each combination costs O(n).
- Space: O(n) beyond the output — the recursion depth and `path` buffer are bounded by `digits.length`; the output array itself holds all combinations.
