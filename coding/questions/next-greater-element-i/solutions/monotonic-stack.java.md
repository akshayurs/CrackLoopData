Precompute the next greater element for *every* value in `nums2` in a single pass, then answer each query with a lookup. Sweep `nums2` while keeping a stack of values that are still waiting for a greater neighbour, kept in decreasing order from bottom to top. When the current value is larger than the stack's top, it is that top's next greater element — pop and record it, repeating until the top outranks the current value.

Store each resolved pair in a `HashMap` keyed by value; anything left on the stack at the end never found a greater element and defaults to `-1`.

```java
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> nextGreater = new HashMap<>();
        Deque<Integer> stack = new ArrayDeque<>();
        for (int n : nums2) {
            while (!stack.isEmpty() && n > stack.peek()) {
                nextGreater.put(stack.pop(), n);
            }
            stack.push(n);
        }
        int[] ans = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            ans[i] = nextGreater.getOrDefault(nums1[i], -1);
        }
        return ans;
    }
}
```

## Why it works

The stack holds values whose next greater element is still unknown, always decreasing top-to-bottom. A new value `n` greater than the top resolves that top (and any others below it that it also exceeds), since `n` is the first larger value to appear to their right. Values that survive to the end had nothing larger after them, so their lookup falls back to `-1`. Distinct values guarantee each key maps unambiguously.

## Complexity

- Time: O(n + m) — every element of `nums2` is pushed and popped at most once, then each of the n queries is an O(1) map lookup.
- Space: O(m) — the stack and map together hold up to m entries.
