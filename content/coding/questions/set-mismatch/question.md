You start with the set `{1, 2, ..., n}` stored in an array `nums`. Because of an error, one of the values got copied over another: as a result exactly one number appears **twice** and exactly one number from `1..n` is **missing**.

Given the corrupted array `nums`, return a two-element array `[duplicated, missing]` — the value that shows up twice and the value that no longer appears.

## Examples

```text
Input:  nums = [1, 2, 2, 4]
Output: [2, 3]        # 2 appears twice, 3 is missing
```

```text
Input:  nums = [1, 1]
Output: [1, 2]        # 1 appears twice, 2 is missing
```

```text
Input:  nums = [3, 2, 3, 4, 6, 5]
Output: [3, 1]        # 3 appears twice, 1 is missing
```

## Constraints

- 2 <= nums.length <= 10^4
- 1 <= nums[i] <= nums.length
- Exactly one value is duplicated and exactly one value from `1..n` is missing.

## Follow-up

Can you find both numbers in a single pass using only O(1) extra space?
</content>
</invoke>
