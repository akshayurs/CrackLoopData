You're given the head of a singly linked list where each node may loop back to an earlier node instead of ending in `null`. Find the node where the cycle begins and return it. If the list has no cycle, return `null`.

To describe the test cases without drawing pointers, each example gives `pos` — the zero-based index of the node the tail connects back to. A `pos` of `-1` means the list is a normal, cycle-free chain. `pos` only exists to build the example input; your function receives just `head` and must work it out from the pointers alone. The examples below report the answer as the **index of the cycle-start node** (or `-1`) since the node itself has no printable value of its own.

## Examples

```text
Input:  values = [3, 2, 0, -4], pos = 1
Output: 1        # tail (-4) connects back to node at index 1 (value 2)
```

```text
Input:  values = [1, 2], pos = 0
Output: 0        # tail (2) connects back to node at index 0 (value 1)
```

```text
Input:  values = [1], pos = -1
Output: -1       # no cycle
```

## Constraints

- 0 <= number of nodes <= 10^4
- -10^5 <= Node.val <= 10^5
- `pos` is -1 or a valid index into the list.
- Follow-up: solve it using O(1) extra space.
