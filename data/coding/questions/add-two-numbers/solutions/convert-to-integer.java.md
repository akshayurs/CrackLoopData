The simplest reading of the problem: rebuild the actual numbers the two lists represent, add them with ordinary arithmetic, then chop the result back into digit nodes. Since the lists store digits ones-first, reversing the digit string before parsing gives the true number.

This sidesteps any carry bookkeeping entirely — `BigInteger` addition does that work — at the cost of materializing the whole number as a string along the way.

```java
import java.math.BigInteger;

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        BigInteger total = toBigInteger(l1).add(toBigInteger(l2));
        String digits = total.toString();
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        for (int i = digits.length() - 1; i >= 0; i--) {
            tail.next = new ListNode(digits.charAt(i) - '0');
            tail = tail.next;
        }
        return dummy.next;
    }

    private BigInteger toBigInteger(ListNode node) {
        StringBuilder sb = new StringBuilder();
        while (node != null) {
            sb.append(node.val);
            node = node.next;
        }
        return new BigInteger(sb.reverse().toString());
    }
}
```

## Why it works

`toBigInteger` walks a list front-to-back, appending digits in ones-first order, then reverses the buffer so it reads most-significant digit first before parsing — exactly reconstructing the number each list encodes. `BigInteger` has unbounded precision, so adding the two reconstructed numbers never overflows the way a primitive `long` would. Converting the sum to a string and reading it back-to-front regenerates digits in the ones-first order the output list needs.

## Complexity

- Time: O(m + n) — build both numbers in one pass each, plus a pass over the result's digits.
- Space: O(m + n) — the string buffers and the resulting `BigInteger` hold as many characters as there are input digits.
