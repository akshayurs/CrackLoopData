The product of everything except `nums[i]` splits cleanly into two halves: the product of all elements to its *left* and the product of all elements to its *right*. If we precompute both, each answer is just one multiplication.

Build a `prefix` array where `prefix[i]` holds the product of everything before `i`, and a `suffix` array where `suffix[i]` holds the product of everything after `i`. Then `answer[i] = prefix[i] * suffix[i]`. Two linear sweeps replace the quadratic nested loop, and division never enters the picture.

```python
def product_except_self(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    return [prefix[i] * suffix[i] for i in range(n)]
```

## Why it works

`prefix[i]` accumulates the running product from the left up to but not including `i`; `suffix[i]` does the same from the right. Multiplying them covers every index except `i` itself, with no overlap and no gap. The boundary entries stay `1` (an empty product), so the ends are handled naturally.

## Complexity

- Time: O(n) — three separate linear passes.
- Space: O(n) — two auxiliary arrays of length n.
