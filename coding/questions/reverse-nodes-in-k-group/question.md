You're given the head of a singly linked list and an integer `k`. Reverse the nodes of the list `k` at a time and return the new head. If the number of nodes left over at the end is fewer than `k`, leave that final group exactly as it is.

## Examples

```text
Input:  head = [1, 2, 3, 4, 5], k = 2
Output: [2, 1, 4, 3, 5]        # last group [5] has < k nodes, left as-is
```

```text
Input:  head = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 4, 5]        # last group [4, 5] has < k nodes, left as-is
```

```text
Input:  head = [1, 2, 3, 4, 5, 6], k = 4
Output: [4, 3, 2, 1, 5, 6]        # last group [5, 6] has < k nodes, left as-is
```

## Constraints

- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

## Follow-up

The array-based approach below uses O(n) extra memory. Can you reverse each group of k nodes by only re-pointing `next` references, using O(1) additional space?
