The simplest reading of the problem: rebuild the actual numbers the two lists represent, add them with ordinary arithmetic, then chop the result back into digit nodes. Since the lists store digits ones-first, reversing the digit string before parsing gives the true number.

This sidesteps any carry bookkeeping entirely — the language's own integer addition does that work — at the cost of materializing the whole number as a string along the way.

```python
def add_two_numbers(l1, l2):
    def to_int(node):
        digits = []
        while node:
            digits.append(str(node.val))
            node = node.next
        return int("".join(reversed(digits)) or "0")

    total = str(to_int(l1) + to_int(l2))
    dummy = ListNode(0)
    tail = dummy
    for ch in reversed(total):
        tail.next = ListNode(int(ch))
        tail = tail.next
    return dummy.next
```

## Why it works

`to_int` walks a list front-to-back, collecting digits in ones-first order, then reverses them so `"".join(...)` reads most-significant digit first before parsing — exactly reconstructing the number each list encodes. Python integers have unbounded precision, so adding the two reconstructed numbers never overflows. Converting the sum back to a string and walking it in reverse regenerates digits in the same ones-first order the output list needs.

## Complexity

- Time: O(m + n) — build both numbers in one pass each, plus a pass over the result's digits.
- Space: O(m + n) — the digit strings and the resulting number hold as many characters as there are input digits.
