You're given the head of a linked list where every node carries an integer `val` and two pointers: `next`, to the following node, and `random`, which may point to *any* node in the list — or to `null`.

Build a **deep copy** of the list: brand-new nodes with the same values, whose `next` and `random` pointers reproduce the original list's wiring exactly, but point only into the new list. The copy must be independent of the original — no shared node may appear in both.

## Examples

```text
Input:  head = [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
Output: [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
# Each pair is [val, randomIndex] — randomIndex is the position of the
# node .random points to (null if .random is None). Node 1 (val 13) has
# random -> node 0 (val 7); node 3 (val 10) has random -> node 2 (val 11).
```

```text
Input:  head = [[1, 1], [2, 1]]
Output: [[1, 1], [2, 1]]
# Both nodes' random pointers point at node 1 (val 2).
```

```text
Input:  head = [[3, null], [3, 0], [3, null]]
Output: [[3, null], [3, 0], [3, null]]
```

## Constraints

- 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- `Node.random` is `null` or points to some node in the list.

## Follow-up

Can you build the copy using only O(1) extra space, without a hash map?
