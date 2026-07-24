The most literal reading of the problem: for each position, multiply together every *other* element with a fresh inner loop. No prefix bookkeeping, no division — just two nested passes.

It is the honest baseline you would state first in an interview, before reaching for something linear. Note that because zeros are handled by plain multiplication, this version needs no special casing.

```python
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
    for i in range(n):
        product = 1
        for j in range(n):
            if j != i:
                product *= nums[j]
        answer[i] = product
    return answer
```

## Why it works

The outer loop fixes the index to exclude; the inner loop multiplies every element whose position differs from `i`. That is exactly the definition of `answer[i]`, so the result is correct by construction — including when `nums` contains one or more zeros, since a zero simply becomes one of the factors.

## Complexity

- Time: O(n²) — for each of n positions we scan all n elements.
- Space: O(1) — ignoring the output array, only a running product is kept.
