Copying every value into an array works, but it spends O(n) space just to compare things that are already sitting in the list. You can get away with O(1) space if you're willing to rearrange the list itself: find the middle with a fast/slow pointer, reverse the second half in place, then walk the two halves toward each other comparing values.

Once the comparison is done, the halves point away from each other rather than forming a clean chain, but returning the boolean is all that's required here, so there's no need to stitch the list back together.

```javascript
function isPalindrome(head) {
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  let previous = null;
  let node = slow;
  while (node) {
    const following = node.next;
    node.next = previous;
    previous = node;
    node = following;
  }

  let left = head;
  let right = previous;
  while (right) {
    if (left.val !== right.val) return false;
    left = left.next;
    right = right.next;
  }
  return true;
}
```

## Why it works

The fast/slow pointer pair lands `slow` on the start of the second half once `fast` runs off the end. Reversing from `slow` onward turns the second half into a list that reads front-to-back in the same order the original reads back-to-front, so walking it alongside the first half from the front compares mirrored positions directly. The second half is never longer than the first, so `right` running out first (or matching in length) is exactly what a true palindrome produces.

## Complexity

- Time: O(n) — finding the middle, reversing, and comparing are each a single pass.
- Space: O(1) — only a handful of pointers; the existing nodes are reused.
