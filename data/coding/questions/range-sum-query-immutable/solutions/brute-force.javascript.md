The literal reading of the problem: for each query, walk from `left` to `right` and add up the elements. No preprocessing, no extra memory beyond the answer list.

This is the honest baseline. It is fine when there are only a handful of queries, but it re-scans the array from scratch every time, so heavy querying makes it slow.

```javascript
function rangeSum(nums, queries) {
  const answers = [];
  for (const [left, right] of queries) {
    let total = 0;
    for (let i = left; i <= right; i++) {
      total += nums[i];
    }
    answers.push(total);
  }
  return answers;
}
```

## Why it works

Each query independently sums the contiguous slice `nums[left..right]`. The inner loop uses `i <= right` so the last element is included. Nothing is cached between queries, so correctness is obvious — we add exactly the elements the query asks for.

## Complexity

- Time: O(q · n) — each of the `q` queries may scan up to `n` elements.
- Space: O(1) — ignoring the output array, only a running total is kept.
