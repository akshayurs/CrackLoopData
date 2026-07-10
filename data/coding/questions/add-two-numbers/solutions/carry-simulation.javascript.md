Do it the way you would add two numbers by hand on paper: walk both lists digit by digit from the ones place, add the corresponding digits plus whatever carried in from the previous column, and write down the ones digit of that sum while carrying the tens digit forward. A dummy head node lets you build the result list without special-casing the first digit.

Keep going as long as either list still has digits or there's a leftover carry — that last check is what correctly handles a final carry like `9999999 + 9999`, which grows the result one digit longer than either input.

```javascript
function addTwoNumbers(l1, l2) {
  const dummy = new ListNode(0);
  let tail = dummy;
  let carry = 0;
  while (l1 || l2 || carry) {
    let total = carry;
    if (l1) {
      total += l1.val;
      l1 = l1.next;
    }
    if (l2) {
      total += l2.val;
      l2 = l2.next;
    }
    carry = Math.floor(total / 10);
    tail.next = new ListNode(total % 10);
    tail = tail.next;
  }
  return dummy.next;
}
```

## Why it works

Because digits are stored ones-first, adding node-by-node from the heads processes the numbers from least significant to most significant digit — the same order carries propagate in manual addition. `total` combines the two current digits with the incoming carry; dividing by 10 splits that into the carry to pass along, and the remainder is the digit to emit. The loop condition `l1 || l2 || carry` keeps running past the shorter list as long as a carry is still pending, which is exactly what produces the extra leading digit when the sum overflows both inputs' lengths.

## Complexity

- Time: O(max(m, n)) — one step per digit position, including at most one extra step for a final carry.
- Space: O(1) extra — only a running `carry` and pointers; the output list is not counted as auxiliary space.
