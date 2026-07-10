The simplest way to think about it: the answer is just "all the non-zero values, in order, followed by enough zeros to fill the rest." So build that up in a scratch array.

Walk the input, writing each non-zero value into the next free slot of a same-sized result array. Every slot left untouched is already `0` by default, so the tail is padded for free. Then copy back into `nums`.

```java
class Solution {
    public int[] moveZeroes(int[] nums) {
        int[] result = new int[nums.length];
        int idx = 0;
        for (int n : nums) {
            if (n != 0) result[idx++] = n;
        }
        for (int i = 0; i < nums.length; i++) nums[i] = result[i];
        return nums;
    }
}
```

## Why it works

Non-zero values are appended in the order they are seen, preserving their relative positions. A freshly allocated `int[]` in Java is zero-initialized, so the trailing slots the non-zeros never reached are already `0`. Copying `result` back into `nums` gives the caller the rearranged array.

## Complexity

- Time: O(n) — one pass to fill, one pass to copy back.
- Space: O(n) — the scratch array holds up to n elements.
