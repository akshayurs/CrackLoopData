You are given an array of integers `nums`. Rearrange it so that every `0` is moved to the end, while the relative order of the non-zero values stays exactly as it was.

Do this by modifying the array itself — you may return the same array after rearranging it.

## Examples

```text
Input:  nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]        # non-zeros keep their order, zeros pushed back
```

```text
Input:  nums = [0]
Output: [0]
```

```text
Input:  nums = [1, 2, 3]
Output: [1, 2, 3]               # no zeros, nothing moves
```

## Constraints

- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

## Follow-up

Can you do it in place using only O(1) extra space, and keep the number of writes as low as possible?
