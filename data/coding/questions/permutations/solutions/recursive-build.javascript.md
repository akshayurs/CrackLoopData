The most direct way to think about permutations: pick each element in turn to go first, then glue it onto every permutation of whatever's left. That "whatever's left" is a smaller version of the same problem, so the natural tool is recursion — with a single element as the base case.

It's a clean, honest first pass, though rebuilding a shorter array at every step isn't free.

```javascript
function permute(nums) {
  function helper(arr) {
    if (arr.length <= 1) return [arr.slice()];
    const perms = [];
    for (let i = 0; i < arr.length; i++) {
      const rest = arr.slice(0, i).concat(arr.slice(i + 1));
      for (const p of helper(rest)) {
        perms.push([arr[i], ...p]);
      }
    }
    return perms;
  }

  const result = helper(nums);
  result.sort((a, b) => {
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) return a[i] - b[i];
    }
    return 0;
  });
  return result;
}
```

## Why it works

`helper` returns every permutation of `arr`. For each index `i`, `arr[i]` is fixed as the head and `rest` (everything else) is recursively permuted; prepending `arr[i]` to each of those sub-permutations accounts for every arrangement that starts with `arr[i]`. Looping `i` over every position covers every possible head, so nothing is missed and nothing repeats. Since the problem doesn't fix an output order, the result is sorted lexicographically before returning so it's identical no matter how the recursion built it up.

## Complexity

- Time: O(n² · n!) — there are n! permutations, and building the `rest` array costs O(n) at each of the roughly n · n! recursive calls.
- Space: O(n²) auxiliary — recursion depth n, each level holding an O(n)-sized array, on top of the O(n · n!) needed to store the output itself.
