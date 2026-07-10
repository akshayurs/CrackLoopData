You are given an array of non-negative integers `nums` and an integer `k`. Return `true` if `nums` contains a **good subarray**, and `false` otherwise.

A subarray is **good** if it has a length of at least two and the sum of its elements is a multiple of `k`. A number `x` counts as a multiple of `k` when `x = n * k` for some integer `n`, so a subarray summing to `0` is always a multiple of `k`.

## Examples

```text
Input:  nums = [23, 2, 4, 6, 7], k = 6
Output: true          # [2, 4] has length 2 and sums to 6 = 1 * 6
```

```text
Input:  nums = [23, 2, 6, 4, 7], k = 6
Output: true          # the whole array sums to 42 = 7 * 6
```

```text
Input:  nums = [23, 2, 6, 4, 7], k = 13
Output: false         # no length-2+ subarray sums to a multiple of 13
```

## Constraints

- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= sum(nums) <= 2^31 - 1
- 1 <= k <= 2^31 - 1

## Follow-up

The brute force checks every subarray in O(n²). Can you decide it in a single pass using the remainders of prefix sums?
