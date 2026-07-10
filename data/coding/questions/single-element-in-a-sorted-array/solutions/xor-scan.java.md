The simplest observation ignores the sorting entirely: XOR-ing a value with itself yields 0, and XOR is associative and commutative. So if you fold every element together with XOR, all the paired values cancel out and only the lone element survives.

Walk the whole array once, accumulating the running XOR. Whatever remains at the end is the answer.

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

Each paired value contributes `x ^ x == 0`, so the two copies annihilate each other regardless of where they sit. XOR with 0 is the identity, leaving the single element untouched. The final accumulator therefore equals exactly the one value that had no partner.

## Complexity

- Time: O(n) — one pass over the array.
- Space: O(1) — a single accumulator.
