The most literal reading of the problem: for each position, multiply together every *other* element with a fresh inner loop. No prefix bookkeeping, no division — just two nested passes.

It is the honest baseline you would state first in an interview, before reaching for something linear. Zeros need no special handling; they simply enter the product like any other factor.

```javascript
function productExceptSelf(nums) {
  const n = nums.length;
  const answer = new Array(n).fill(1);
  for (let i = 0; i < n; i++) {
    let product = 1;
    for (let j = 0; j < n; j++) {
      if (j !== i) {
        product *= nums[j];
      }
    }
    answer[i] = product;
  }
  return answer;
}
```

## Why it works

The outer loop fixes the index to exclude; the inner loop multiplies every element whose position differs from `i`. That matches the definition of `answer[i]` exactly, so the output is correct by construction — including when `nums` contains zeros, which just become one of the factors.

## Complexity

- Time: O(n²) — for each of n positions we scan all n elements.
- Space: O(1) — ignoring the output array, only a running product is kept.
