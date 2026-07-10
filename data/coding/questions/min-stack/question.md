Design a stack that, on top of the usual push and pop, can report its smallest element at any moment — all in constant time. Implement the `MinStack` class:

- `MinStack()` creates an empty stack.
- `push(val)` places `val` on top of the stack.
- `pop()` removes the element on top of the stack.
- `top()` returns the element on top of the stack.
- `getMin()` returns the minimum element currently in the stack.

Every operation, including `getMin`, must run in O(1) time.

## Examples

```text
Input:
  ops  = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
  args = [[],         [-2],   [0],    [-3],   [],       [],    [],    []]
Output: [null, null, null, null, -3, null, 0, -2]

# push -2, push 0, push -3
# getMin -> -3   (smallest so far)
# pop            (removes -3)
# top    -> 0
# getMin -> -2   (smallest of what remains)
```

```text
Input:
  ops  = ["MinStack", "push", "push", "getMin", "pop", "getMin"]
  args = [[],         [5],    [5],    [],        [],    []]
Output: [null, null, null, 5, null, 5]

# duplicate minimums: popping one 5 must keep 5 as the min
```

## Constraints

- -2^31 <= val <= 2^31 - 1
- `pop`, `top`, and `getMin` are only called on a non-empty stack.
- At most 3 * 10^4 calls are made in total across all four methods.

## Follow-up

Can you support `getMin` in O(1) without scanning the stack on every call?
