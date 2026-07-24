Instead of copying out a "remaining" list at every step, permute the array in place. Walk a `start` pointer left to right; at each position, swap in every candidate that hasn't been placed yet (everything from `start` onward), recurse on the rest of the array, then swap back so the next candidate sees the original order.

This is classic backtracking: choose, explore, un-choose. No extra list gets built until a full permutation is ready to be copied into the answer.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, result);
        result.sort((a, b) -> {
            for (int i = 0; i < a.size(); i++) {
                if (!a.get(i).equals(b.get(i))) return a.get(i) - b.get(i);
            }
            return 0;
        });
        return result;
    }

    private void backtrack(int[] nums, int start, List<List<Integer>> result) {
        if (start == nums.length) {
            List<Integer> perm = new ArrayList<>();
            for (int n : nums) perm.add(n);
            result.add(perm);
            return;
        }
        for (int i = start; i < nums.length; i++) {
            swap(nums, start, i);
            backtrack(nums, start + 1, result);
            swap(nums, start, i);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
```

## Why it works

`backtrack(start)` fixes the first `start` elements and tries every unused value in the remaining slice as the next one, via a swap with position `start`. Recursing on `start + 1` fills the rest; undoing the swap afterward restores `nums` so the loop's next iteration tries a different candidate from the same original state. When `start` reaches the array's length, every position is fixed and `nums` holds one complete permutation, which is copied into `result`. Because the problem doesn't fix an output order, the result is sorted lexicographically before returning so it matches regardless of the order swaps happened to produce.

## Complexity

- Time: O(n · n!) — n! permutations are generated, each finished with an O(n) copy into `result`.
- Space: O(n) auxiliary — recursion depth n and in-place swaps, on top of the O(n · n!) needed to store the output itself.
