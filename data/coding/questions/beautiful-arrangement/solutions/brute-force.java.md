The definition talks about permutations, so the most literal solution is to generate every permutation of `1..n` and test each one against the divisibility rule.

There is no cleverness here — build permutations with in-place swaps, and whenever a full ordering is assembled, scan it once to check the rule at every position.

```java
class Solution {
    public int countArrangement(int n) {
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = i + 1;
        return permute(nums, 0);
    }

    private int permute(int[] arr, int k) {
        if (k == arr.length) {
            return isBeautiful(arr) ? 1 : 0;
        }
        int count = 0;
        for (int i = k; i < arr.length; i++) {
            swap(arr, k, i);
            count += permute(arr, k + 1);
            swap(arr, k, i);
        }
        return count;
    }

    private boolean isBeautiful(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int pos = i + 1, val = arr[i];
            if (val % pos != 0 && pos % val != 0) return false;
        }
        return true;
    }

    private void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
```

## Why it works

`permute` builds every ordering of `arr` by swapping each remaining value into slot `k` and recursing, then swapping back so sibling branches see the original order. Once `k` reaches the end, `arr` holds one full permutation, and `isBeautiful` checks the rule at every 1-indexed position.

## Complexity

- Time: O(n! * n) — n! permutations, each checked in O(n).
- Space: O(n) — recursion depth for the swap-based generator.
