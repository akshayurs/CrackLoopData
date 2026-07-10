The simplest reading of the problem: rebuild the actual numbers the two lists represent, add them with ordinary arithmetic, then chop the result back into digit nodes. Since the lists store digits ones-first, reversing the digit string before parsing gives the true number.

This sidesteps any carry bookkeeping entirely — `BigInt` addition does that work — at the cost of materializing the whole number as a string along the way.

```javascript
function addTwoNumbers(l1, l2) {
  function toBigInt(node) {
    const digits = [];
    while (node) {
      digits.push(node.val);
      node = node.next;
    }
    return BigInt(digits.reverse().join('') || '0');
  }

  const total = (toBigInt(l1) + toBigInt(l2)).toString();
  const dummy = new ListNode(0);
  let tail = dummy;
  for (let i = total.length - 1; i >= 0; i--) {
    tail.next = new ListNode(Number(total[i]));
    tail = tail.next;
  }
  return dummy.next;
}
```

## Why it works

`toBigInt` walks a list front-to-back, collecting digits in ones-first order, then reverses them so joining the array reads most-significant digit first before parsing — exactly reconstructing the number each list encodes. `BigInt` has unbounded precision, so adding the two reconstructed numbers never overflows the way a regular `number` would. Converting the sum to a string and reading it back-to-front regenerates digits in the ones-first order the output list needs.

## Complexity

- Time: O(m + n) — build both numbers in one pass each, plus a pass over the result's digits.
- Space: O(m + n) — the digit arrays and the resulting `BigInt` string hold as many characters as there are input digits.
