Given an integer array `nums`, find every unique triplet `[nums[i], nums[j], nums[k]]` with distinct indices `i`, `j`, `k` whose values sum to zero. Two triplets are the same if they contain the same three numbers, so the answer must not list a triplet more than once.

Return the triplets in **canonical form**: each triplet sorted in ascending order, and the list of triplets sorted in ascending order as well. This keeps the output deterministic regardless of the order in which triplets are discovered.

## Examples

```text
Input:  nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
```

```text
Input:  nums = [0, 1, 1]
Output: []        # no three values add up to 0
```

```text
Input:  nums = [0, 0, 0]
Output: [[0, 0, 0]]
```

## Constraints

- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

## Follow-up

The naive answer checks every triple in O(n³). Can you reach O(n²) time using sorting and two pointers?
