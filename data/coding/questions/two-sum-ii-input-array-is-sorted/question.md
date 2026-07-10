You are given an array of integers `numbers` sorted in **non-decreasing order** and an integer `target`. Find the two numbers that add up to `target` and return their positions as `[index1, index2]`, where `1 <= index1 < index2 <= numbers.length`.

Positions are **1-indexed**. Each input has **exactly one** solution, and you may not use the same element twice.

## Examples

```text
Input:  numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]        # numbers[1] + numbers[2] = 2 + 7 = 9
```

```text
Input:  numbers = [2, 3, 4], target = 6
Output: [1, 3]        # numbers[1] + numbers[3] = 2 + 4 = 6
```

```text
Input:  numbers = [-1, 0], target = -1
Output: [1, 2]
```

## Constraints

- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- Exactly one valid pair exists.

## Follow-up

The array is already sorted. Can you use that to solve it in O(1) extra space and better than O(n²) time?
