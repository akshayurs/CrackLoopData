A **linked list** is a chain of nodes where each node holds a value and a pointer (`next`) to the following node — no contiguous memory, no random-access indexing. To reach the fifth node you must walk through the first four. That single constraint — sequential access only — is what shapes every technique in this pattern.

What you get in exchange for losing O(1) indexing is O(1) insertion and deletion once you already hold a pointer to the right spot, with no shifting of the rest of the structure the way an array requires. Most linked-list problems are really about **pointer surgery**: rewiring `next` references to reverse, splice, merge, or remove nodes without ever copying values around.

The two pointers you almost always work with are `prev` and `curr`, walked forward one node at a time while you redirect links behind you. A **dummy head node** removes the awkward "is this the first node?" special case whenever the head itself might change or be deleted.

The other half of the pattern is **fast/slow pointers** (Floyd's technique): two pointers start together, one advances one step per iteration and the other advances two. This finds the middle of a list in one pass, and detects a cycle — if the two pointers ever meet, there is a loop.

A typical reversal shape:

```
prev = null
curr = head
while curr is not null:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
return prev
```

Recursion is a natural fit too: reversing or processing "the rest of the list" and then patching the current node onto the result mirrors the recursive definition of the structure itself.
