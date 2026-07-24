The most direct way to think about permutations: pick each element in turn to go first, then glue it onto every permutation of whatever's left. That "whatever's left" is a smaller version of the same problem, so the natural tool is recursion — with a single element as the base case.

It's a clean, honest first pass, though rebuilding a shorter list at every step isn't free.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<Integer> arr = new ArrayList<>();
        for (int n : nums) arr.add(n);
        List<List<Integer>> result = helper(arr);
        result.sort((a, b) -> {
            for (int i = 0; i < a.size(); i++) {
                if (!a.get(i).equals(b.get(i))) return a.get(i) - b.get(i);
            }
            return 0;
        });
        return result;
    }

    private List<List<Integer>> helper(List<Integer> arr) {
        if (arr.size() <= 1) {
            List<List<Integer>> base = new ArrayList<>();
            base.add(new ArrayList<>(arr));
            return base;
        }
        List<List<Integer>> perms = new ArrayList<>();
        for (int i = 0; i < arr.size(); i++) {
            List<Integer> rest = new ArrayList<>(arr);
            int head = rest.remove(i);
            for (List<Integer> p : helper(rest)) {
                List<Integer> withHead = new ArrayList<>();
                withHead.add(head);
                withHead.addAll(p);
                perms.add(withHead);
            }
        }
        return perms;
    }
}
```

## Why it works

`helper` returns every permutation of `arr`. For each index `i`, `arr.get(i)` is fixed as the head and `rest` (everything else) is recursively permuted; prepending the head to each sub-permutation accounts for every arrangement that starts with it. Looping `i` over every position covers every possible head, so nothing is missed and nothing repeats. Since the problem doesn't fix an output order, the result is sorted lexicographically before returning so it's identical no matter how the recursion built it up.

## Complexity

- Time: O(n² · n!) — there are n! permutations, and building `rest` costs O(n) at each of the roughly n · n! recursive calls.
- Space: O(n²) auxiliary — recursion depth n, each level holding an O(n)-sized list, on top of the O(n · n!) needed to store the output itself.
