Suppose an array sorted in strictly ascending order is rotated at some unknown pivot between `0` and `n - 1` times. For example, `[1, 2, 3, 4, 5]` might become `[3, 4, 5, 1, 2]` after three rotations. Given such a rotated array `nums` with all-distinct values, return its **minimum** element.

You must design an algorithm that runs in `O(log n)` time.

## Examples

```text
Input:  nums = [3, 4, 5, 1, 2]
Output: 1        # original array was [1, 2, 3, 4, 5], rotated 3 times
```

```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2]
Output: 0        # the pivot sits just before 0
```

```text
Input:  nums = [11, 13, 15, 17]
Output: 11       # rotated n times, effectively not rotated
```

## Constraints

- 1 <= nums.length <= 5000
- -5000 <= nums[i] <= 5000
- All integers in `nums` are unique.
- `nums` is a sorted ascending array that has been rotated between 0 and n times.

## Follow-up

The linear scan is trivial. Can you exploit the fact that the array is still "mostly sorted" to reach O(log n)?
