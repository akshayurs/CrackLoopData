The most literal reading: for every value in the array, pretend it is the start of a run and keep asking "is the next integer here too?" Each lookup scans the whole array, and we grow the run one step at a time until the next value is missing.

No extra data structures, no sorting — just repeated linear searches. It is the honest baseline you would state before reaching for something faster.

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        int best = 0;
        for (int start : nums) {
            if (contains(nums, start - 1)) continue;
            int length = 1;
            while (contains(nums, start + length)) length++;
            best = Math.max(best, length);
        }
        return best;
    }

    private boolean contains(int[] nums, int value) {
        for (int n : nums) if (n == value) return true;
        return false;
    }
}
```

## Why it works

A value only begins a run if `start - 1` is absent, so we skip interior values and only count each run from its true left end. From a start we walk `start + 1`, `start + 2`, … using linear `contains` checks, extending `length` until the chain breaks. The largest length seen wins. Each `contains` scans the whole array, which is what makes this slow.

## Complexity

- Time: O(n³) — for each of n values we may walk a run of length up to n, and every `contains` check scans the n-element array.
- Space: O(1) — only counters, no auxiliary structure.
