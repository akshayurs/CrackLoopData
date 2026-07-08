You are given an integer array `nums`. Return a new array `answer` where `answer[i]` is the product of every element of `nums` **except** `nums[i]`.

The answer for each position is guaranteed to fit in a 32-bit integer. Solve it **without using the division operator**.

## Examples

```text
Input:  nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]     # 2·3·4, 1·3·4, 1·2·4, 1·2·3
```

```text
Input:  nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]    # only index 2 avoids the zero factor
```

```text
Input:  nums = [2, 3]
Output: [3, 2]
```

## Constraints

- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of `nums` fits in a 32-bit integer.
- You must not use the division operator.

## Follow-up

Can you achieve O(n) time using only O(1) extra space, not counting the output array?
