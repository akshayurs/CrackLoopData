The simplest way to check for a palindrome is the way you'd check it on paper: write down the sequence, then compare it to its own reverse. Walk the list once, copying each `val` into a plain array.

Once the values sit in an array, the two-pointer palindrome check is trivial — compare the first and last, then step inward, or just compare the array to its reverse directly.

```python
def is_palindrome(head):
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next
    return values == values[::-1]
```

## Why it works

The array preserves the exact order the values appeared in the list, so `values[::-1]` is precisely what the list would look like read backwards. If the two sequences are equal, every value at position `i` matches the value at the mirrored position — which is the definition of a palindrome.

## Complexity

- Time: O(n) — one pass to copy, one pass to compare.
- Space: O(n) — the array holds all n values.
