Reversal is symmetric: the character at the front trades places with the one at the back, then you step inward. Put one pointer at the start and another at the end, swap the pair they point to, and march them toward each other until they meet in the middle.

Because every swap fixes two characters at once, you only need to walk halfway across the string. Working on a mutable array of characters keeps the extra memory to the two indices themselves.

```javascript
function reverseString(s) {
    const chars = s.split("");
    let left = 0;
    let right = chars.length - 1;
    while (left < right) {
        [chars[left], chars[right]] = [chars[right], chars[left]];
        left++;
        right--;
    }
    return chars.join("");
}
```

## Why it works

`left` and `right` bound the still-unreversed middle. Each iteration swaps the outermost unfixed pair and shrinks that window from both sides. When `left` meets or passes `right` every position has been placed, and a single middle character (odd length) is already where it belongs.

## Complexity

- Time: O(n) — each character is touched once across n/2 swaps.
- Space: O(1) — only two index variables beyond the output buffer.
