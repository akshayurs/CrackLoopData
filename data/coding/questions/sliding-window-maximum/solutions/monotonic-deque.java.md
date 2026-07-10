The key insight: if a newer element is larger than older ones still in the window, those older ones can never be the maximum again — they are dominated. So maintain a deque of indices whose values are strictly decreasing from front to back. The front always holds the current window's maximum.

For each element, pop smaller values off the back before pushing its index, and drop the front once it slides out of the window. Every index enters and leaves the deque exactly once, giving linear time.

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] result = new int[n - k + 1];
        Deque<Integer> dq = new ArrayDeque<>(); // indices, values decreasing front→back
        for (int i = 0; i < n; i++) {
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();
            dq.offerLast(i);
            if (dq.peekFirst() <= i - k) dq.pollFirst();
            if (i >= k - 1) result[i - k + 1] = nums[dq.peekFirst()];
        }
        return result;
    }
}
```

## Why it works

The deque holds indices in strictly decreasing value order, so `nums[dq.peekFirst()]` is the largest candidate value. Removing the back while it is `<= nums[i]` discards dominated elements — anything smaller than the incoming value and to its left is useless. The front is dropped once its index is `<= i - k`, i.e. no longer inside the window. Once the first full window forms (`i >= k - 1`), the front is exactly that window's maximum.

## Complexity

- Time: O(n) — each index is offered and removed from the deque at most once.
- Space: O(k) — the deque never holds more than one window of indices.
