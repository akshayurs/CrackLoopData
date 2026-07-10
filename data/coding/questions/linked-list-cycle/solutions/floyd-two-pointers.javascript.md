You can decide the question with no extra memory by racing two pointers at different speeds — Floyd's tortoise-and-hare. The slow pointer moves one node per step; the fast pointer moves two. On a finite acyclic list the fast pointer runs off the end into `null`. On a list with a cycle the fast pointer keeps circling and eventually collides with the slow pointer.

Picture two runners on a track: on a straight road the faster finishes and stops, but on a loop the faster runner always laps and meets the slower one.

```javascript
function hasCycle(head) {
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
}
```

## Why it works

Without a cycle, `fast` or `fast.next` becomes `null` and the loop returns `false`. With a cycle, both pointers enter the loop and the fast pointer gains one node on the slow pointer each step; the gap therefore decreases by one until it hits zero, at which point `slow === fast` and the function returns `true`. Because the gap changes by exactly one per step, they cannot overshoot without meeting.

## Complexity

- Time: O(n) — a constant number of passes over the list.
- Space: O(1) — two pointers, no extra structures.
