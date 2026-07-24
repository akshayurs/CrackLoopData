The wasted work in the brute force is that every element rescans the array. A monotonic stack removes it: keep a stack of indices whose next greater element is still unknown, in decreasing order of value. When a new, larger value arrives, it resolves every smaller index sitting on top of the stack at once.

To handle the circular wrap, iterate `2n` times over indices `i % n`. Two loops around are enough — any index that hasn't found a larger value after a full extra pass never will.

```java
import java.util.Arrays;
import java.util.Deque;
import java.util.ArrayDeque;

class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        Arrays.fill(result, -1);
        Deque<Integer> stack = new ArrayDeque<>();
        for (int k = 0; k < 2 * n; k++) {
            int i = k % n;
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i]) {
                result[stack.pop()] = nums[i];
            }
            if (k < n) stack.push(i);
        }
        return result;
    }
}
```

## Why it works

The stack holds indices whose answer is pending, with strictly decreasing values from bottom to top. A value `nums[i]` greater than the top resolves that index and pops it, then keeps popping while the invariant holds — so each index is pushed once and popped at most once. We only push during the first `n` steps; the second pass exists purely to give early indices a chance to be resolved by elements that wrap around. Anything still on the stack at the end has no greater element and keeps its `-1`.

## Complexity

- Time: O(n) — each index is pushed and popped at most once across the 2n iterations.
- Space: O(n) — the stack holds up to n indices.
