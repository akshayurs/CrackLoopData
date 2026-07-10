Instead of picking all three cut points up front and validating afterward, build the address one octet at a time and abandon a branch the instant it can't possibly lead anywhere. At each step, try consuming 1, 2, or 3 characters for the next octet; skip a length immediately if it produces a leading zero or a value over 255, and skip the whole branch if the remaining characters can't be split into the remaining octets.

Because every octet is at most 3 digits and there are always exactly 4 of them, the search tree stays tiny regardless of the input length — the pruning turns what looks like exponential search into a small, fixed amount of work.

```javascript
function restoreIpAddresses(digits) {
  const n = digits.length;
  const results = [];
  const parts = [];

  const backtrack = (start) => {
    const remainingParts = 4 - parts.length;
    const remainingChars = n - start;
    if (remainingChars < remainingParts || remainingChars > remainingParts * 3) {
      return;
    }
    if (parts.length === 4) {
      if (start === n) results.push(parts.join("."));
      return;
    }

    for (let length = 1; length <= 3 && start + length <= n; length++) {
      const piece = digits.slice(start, start + length);
      if (piece[0] === "0" && length > 1) break;
      if (Number(piece) > 255) break;
      parts.push(piece);
      backtrack(start + length);
      parts.pop();
    }
  };

  backtrack(0);
  return results.sort();
}
```

## Why it works

The `remainingChars` bound prunes any branch where the leftover string is too short or too long to fill the remaining octets, so hopeless prefixes are dropped before any recursion happens. Within a single octet, the loop stops as soon as a length is invalid (leading zero or value over 255), since a longer piece starting the same way can only be worse. `parts` is built and unwound in place, so each successful path down to 4 octets that exactly consumes the string is one valid address.

## Complexity

- Time: O(1) — each octet has at most 3 candidate lengths and there are always exactly 4 octets, so the search explores at most 3^4 branches no matter how long `digits` is.
- Space: O(n) — recursion depth is bounded by the string length, plus the output array of matched addresses.
