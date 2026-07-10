You are given an array of integers `nums`. Return `true` if any value appears **at least twice** in the array, and `false` if every element is distinct.

## Examples

```text
Input:  nums = [1, 2, 3, 1]
Output: true          # the value 1 appears at index 0 and index 3
```

```text
Input:  nums = [1, 2, 3, 4]
Output: false         # every element is unique
```

```text
Input:  nums = [2, 14, 2, 7, 8, 14]
Output: true          # both 2 and 14 repeat
```

## Constraints

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

## Follow-up

Can you decide in a single pass, without sorting the input?
