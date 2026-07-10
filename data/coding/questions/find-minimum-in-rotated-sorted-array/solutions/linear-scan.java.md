The rotation hides the minimum somewhere in the array, but there is nothing subtle about finding the smallest value: just look at every element and keep the smallest one seen so far. This ignores the sorted structure entirely, which is why it is the baseline rather than the intended answer.

It is worth writing once to confirm the expected output before optimizing — a correct O(n) reference makes the O(log n) version easy to trust.

```java
class Solution {
    public int findMin(int[] nums) {
        int smallest = nums[0];
        for (int n : nums) {
            if (n < smallest) {
                smallest = n;
            }
        }
        return smallest;
    }
}
```

## Why it works

The minimum of a set is the smallest of all its elements regardless of order, so a single sweep that tracks the running minimum is guaranteed to return the correct value. Seeding `smallest` with `nums[0]` handles the single-element array cleanly.

## Complexity

- Time: O(n) — every element is inspected once.
- Space: O(1) — only the running minimum is stored.
