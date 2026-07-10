The most direct way to think about permutations: pick each element in turn to go first, then glue it onto every permutation of whatever's left. That "whatever's left" is a smaller version of the same problem, so the natural tool is recursion — with a single element as the base case.

It's a clean, honest first pass, though rebuilding a shorter list at every step isn't free.

```python
def permute(nums):
    def helper(arr):
        if len(arr) <= 1:
            return [arr[:]]
        perms = []
        for i in range(len(arr)):
            rest = arr[:i] + arr[i + 1:]
            for p in helper(rest):
                perms.append([arr[i]] + p)
        return perms

    result = helper(nums)
    result.sort()
    return result
```

## Why it works

`helper` returns every permutation of `arr`. For each index `i`, `arr[i]` is fixed as the head and `rest` (everything else) is recursively permuted; prepending `arr[i]` to each of those sub-permutations accounts for every arrangement that starts with `arr[i]`. Looping `i` over every position covers every possible head, so nothing is missed and nothing repeats. Since the problem doesn't fix an output order, the result is sorted lexicographically before returning so it's identical no matter how the recursion built it up.

## Complexity

- Time: O(n² · n!) — there are n! permutations, and building the `rest` slice costs O(n) at each of the roughly n · n! recursive calls.
- Space: O(n²) auxiliary — recursion depth n, each level holding an O(n)-sized slice, on top of the O(n · n!) needed to store the output itself.
