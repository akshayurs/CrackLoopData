Start with a list holding just the empty string, and grow it one digit at a time. For each digit, take every combination built so far and append each of that digit's letters to it, producing a brand-new, larger array. After the last digit, the array holds every full combination.

It is the most direct translation of "multiply out the possibilities" and needs no recursion, but it keeps rebuilding a fresh array at every step.

```javascript
function letterCombinations(digits) {
  if (digits.length === 0) return [];

  const keypad = {
    2: "abc", 3: "def", 4: "ghi", 5: "jkl",
    6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz",
  };

  let combinations = [""];
  for (const digit of digits) {
    const letters = keypad[digit];
    const next = [];
    for (const prefix of combinations) {
      for (const letter of letters) {
        next.push(prefix + letter);
      }
    }
    combinations = next;
  }

  return combinations;
}
```

## Why it works

`combinations` is an invariant: after processing the first `k` digits, it holds exactly every combination for those `k` digits, in keypad order. Each step multiplies its size by the number of letters on the next digit, and every existing prefix is extended by every letter — so no combination is missed and none is duplicated.

## Complexity

- Time: O(4^n) — n is `digits.length`; the array size (and work to build it) grows by a factor of up to 4 per digit.
- Space: O(4^n) — every intermediate array, up to the final one, is kept in memory.
