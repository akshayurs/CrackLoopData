Every subset of an `n`-element array corresponds to one of the `2^n` binary strings of length `n` — bit `i` set means "include `nums[i]`". Loop a counter from `0` to `2^n - 1` and read off its bits to build each subset directly, with no recursion at all.

It's the most mechanical way to enumerate a power set, and a good baseline before reaching for backtracking.

```python
def subsets(nums):
    n = len(nums)
    result = []
    for mask in range(1 << n):
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)
    result.sort(key=lambda s: (len(s), s))
    return result
```

## Why it works

Each of the `2^n` values of `mask` is a unique bit pattern, and each bit pattern selects a unique combination of elements — so the loop visits every subset exactly once. Sorting by `(length, contents)` afterward just fixes a canonical order; it doesn't change which subsets are found.

## Complexity

- Time: O(n * 2^n) — 2^n masks, each scanned in O(n) to build its subset (plus an O(2^n log 2^n) sort).
- Space: O(n * 2^n) — the output holds all subsets, each up to length n.
