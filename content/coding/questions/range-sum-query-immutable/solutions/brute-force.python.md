The literal reading of the problem: for each query, walk from `left` to `right` and add up the elements. No preprocessing, no extra memory beyond the answer list.

This is the honest baseline. It is fine when there are only a handful of queries, but it re-scans the array from scratch every time, so heavy querying makes it slow.

```python
def range_sum(nums, queries):
    answers = []
    for left, right in queries:
        total = 0
        for i in range(left, right + 1):
            total += nums[i]
        answers.append(total)
    return answers
```

## Why it works

Each query independently sums the contiguous slice `nums[left..right]`. Since the indices are inclusive, the inner loop runs through `right + 1` to include the last element. Nothing is cached between queries, so correctness is obvious — we simply add exactly the elements the query asks for.

## Complexity

- Time: O(q · n) — each of the `q` queries may scan up to `n` elements.
- Space: O(1) — ignoring the output list, only a running total is kept.
