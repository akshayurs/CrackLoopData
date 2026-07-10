Forget that the individual lists are sorted at all — walk every list, dump every value into one flat array, sort that array, then rebuild a brand-new list from the sorted values. It ignores the structure you're handed, but it's the fastest thing to reason about correctly.

Because the original nodes are discarded during traversal (only their `val` is kept), the final list is built out of fresh nodes rather than the input's own nodes.

```python
def merge_k_lists(lists):
    values = []
    for node in lists:
        while node:
            values.append(node.val)
            node = node.next
    values.sort()

    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next
```

## Why it works

`values` ends up holding every node's value exactly once, regardless of which list it came from. Sorting that flat array produces the required non-decreasing order directly. The final loop then lays down one fresh node per value in that order — since the array is already sorted, no comparisons are needed while rebuilding.

## Complexity

- Time: O(N log N) — N is the total number of nodes; dominated by the sort.
- Space: O(N) — the values array plus N freshly allocated result nodes.
