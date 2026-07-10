You are given an array `nums` of unique integers. Return every possible subset (the power set) — no duplicate subsets, in any order internally, but the grader expects the final list sorted first by subset length, then lexicographically by contents.

## Examples

```text
Input:  nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

```text
Input:  nums = [0]
Output: [[], [0]]
```

```text
Input:  nums = [1, 2]
Output: [[], [1], [2], [1, 2]]
```

## Constraints

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All elements of `nums` are distinct.

## Follow-up

Can you generate the subsets without recursion, using bitmasks instead?
