The simplest way to check for a palindrome is the way you'd check it on paper: write down the sequence, then compare it to its own reverse. Walk the list once, copying each `val` into a plain array.

Once the values sit in an array, the two-pointer palindrome check is trivial — compare the first and last, then step inward, or just compare the array to its reverse directly.

```javascript
function isPalindrome(head) {
  const values = [];
  let node = head;
  while (node) {
    values.push(node.val);
    node = node.next;
  }
  for (let i = 0, j = values.length - 1; i < j; i++, j--) {
    if (values[i] !== values[j]) return false;
  }
  return true;
}
```

## Why it works

The array preserves the exact order the values appeared in the list. Walking two pointers inward from both ends compares every value at position `i` against its mirrored position `n - 1 - i`; if any pair disagrees, the sequence cannot be a palindrome, and if the pointers cross without a mismatch, every pair agreed.

## Complexity

- Time: O(n) — one pass to copy, one pass to compare.
- Space: O(n) — the array holds all n values.
