The key insight: if a newer element is larger than older ones still in the window, those older ones can never be the maximum again — they are dominated. So maintain a deque of indices whose values are strictly decreasing from front to back. The front always holds the current window's maximum.

For each element, pop smaller values off the back before pushing its index, and drop the front once it slides out of the window. Every index enters and leaves the deque exactly once, giving linear time.

```javascript
function maxSlidingWindow(nums, k) {
  const dq = []; // indices, values decreasing front→back
  let head = 0;
  const result = [];
  for (let i = 0; i < nums.length; i++) {
    while (dq.length > head && nums[dq[dq.length - 1]] <= nums[i]) dq.pop();
    dq.push(i);
    if (dq[head] <= i - k) head++;
    if (i >= k - 1) result.push(nums[dq[head]]);
  }
  return result;
}
```

## Why it works

`dq` holds indices in strictly decreasing value order, and `head` marks its logical front, so `nums[dq[head]]` is the largest candidate value. Popping the back while it is `<= nums[i]` removes dominated elements — anything smaller than the incoming value and to its left is useless. The front is advanced once its index is `<= i - k`, i.e. no longer inside the window. Once the first full window forms (`i >= k - 1`), the front is exactly that window's maximum.

## Complexity

- Time: O(n) — each index is pushed and dropped from the deque at most once.
- Space: O(k) — the live portion of the deque never exceeds one window.
