The honest baseline: forget that the array is sorted and lean on a bit trick. XOR is its own inverse, so `x ^ x == 0` — every value that appears twice cancels itself out, and XOR-ing the whole array leaves only the lone element behind.

It is the first thing worth stating in an interview because it needs no case analysis and works even if the pairs weren't adjacent.

```java
class Solution {
    public int singleNonDuplicate(int[] nums) {
        int result = 0;
        for (int n : nums) {
            result ^= n;
        }
        return result;
    }
}
```

## Why it works

XOR is commutative and associative, so the order of the fold doesn't matter. Each paired value contributes `n ^ n = 0`, and `0 ^ x = x`, so after cancelling every duplicate the accumulator holds exactly the unpaired value.

## Complexity

- Time: O(n) — one pass over the array.
- Space: O(1) — a single accumulator.
