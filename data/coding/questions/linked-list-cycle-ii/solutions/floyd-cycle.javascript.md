Trade memory for a bit of math: Floyd's tortoise-and-hare. Move a slow pointer one step at a time and a fast pointer two steps at a time. If there's a cycle they're guaranteed to meet somewhere inside the loop — no bookkeeping of visited nodes required.

The clever second half is turning that meeting point into the actual start of the cycle. Reset one pointer to `head` and advance both one step at a time; the node where they meet again is exactly the cycle's entrance. This falls out of the distance algebra: if the cycle starts `a` nodes into the list and the meeting point is `b` nodes into the cycle, walking `a` more steps from both `head` and the meeting point lands on the same node.

```javascript
function detectCycle(head) {
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) {
      let ptr = head;
      while (ptr !== slow) {
        ptr = ptr.next;
        slow = slow.next;
      }
      return ptr;
    }
  }
  return null;
}
```

## Why it works

If a cycle exists, the fast pointer laps the slow one and they collide inside the loop — a standard pursuit argument on a circular structure. Let `a` be the distance from `head` to the cycle start and `c` the cycle length; when slow and fast meet, the offset works out so that advancing a fresh pointer from `head` and the meeting point in lockstep, one step at a time, converges exactly at the cycle's start after `a` steps. No cycle means `fast` reaches `null` first and the loop exits.

## Complexity

- Time: O(n) — each phase is a single bounded pass.
- Space: O(1) — only two pointers, no extra structure.
