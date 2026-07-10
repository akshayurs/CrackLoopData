You are given an integer array `nums`. Pick two numbers `nums[i]` and `nums[j]` (`i != j`) and compute their bitwise XOR. Return the largest XOR value obtainable from any pair in the array.

The array has at least two elements, and every value fits in 32 bits.

## Examples

```text
Input:  nums = [3, 10, 5, 25, 2, 8]
Output: 28        # 5 XOR 25 = 28
```

```text
Input:  nums = [14, 70, 5, 92, 27, 49, 9]
Output: 119       # 70 XOR 49 = 119
```

```text
Input:  nums = [1, 2]
Output: 3         # 1 XOR 2 = 3
```

## Constraints

- 2 <= nums.length <= 2 * 10^5
- 0 <= nums[i] <= 2^31 - 1

## Follow-up

Can you avoid the O(n²) all-pairs scan and find the answer in roughly O(n) time using the bit structure of the numbers?
