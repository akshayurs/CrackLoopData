An IP address always has exactly three dots, so it always has exactly three "cut points" inside the digit string. The most direct approach is to try every combination of three cut positions with three nested loops, slice out the four resulting pieces, and keep the combination only if all four pieces are legal octets.

It never looks more than one string ahead — no recursion, no early exit — so it re-validates a lot of dead-end prefixes, but it is the natural first attempt.

```javascript
function restoreIpAddresses(digits) {
  const n = digits.length;
  const results = [];

  const isValid = (piece) => {
    if (!piece || piece.length > 3) return false;
    if (piece[0] === "0" && piece.length > 1) return false;
    return Number(piece) <= 255;
  };

  for (let i = 1; i < Math.min(4, n); i++) {
    for (let j = i + 1; j < Math.min(i + 4, n); j++) {
      for (let k = j + 1; k < Math.min(j + 4, n); k++) {
        const a = digits.slice(0, i);
        const b = digits.slice(i, j);
        const c = digits.slice(j, k);
        const d = digits.slice(k);
        if (isValid(a) && isValid(b) && isValid(c) && isValid(d)) {
          results.push(`${a}.${b}.${c}.${d}`);
        }
      }
    }
  }

  return results.sort();
}
```

## Why it works

Every valid split is uniquely described by the lengths of its first three octets, so scanning `i < j < k` over the string's index range enumerates every possible four-way partition exactly once. `isValid` rejects empty pieces, pieces longer than three digits, values above 255, and leading zeros on multi-digit pieces — the three conditions that make an octet malformed. Bounding each loop to at most 3 steps ahead keeps the search from wasting time on octets that could never be valid anyway.

## Complexity

- Time: O(n^3) — three nested loops over cut positions, each iteration doing O(1) validation since every piece is at most 3 characters.
- Space: O(1) extra beyond the output array.
