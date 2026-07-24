The two auxiliary arrays are avoidable. Write the left-side (prefix) products directly into the output array in one forward pass. Then sweep backwards with a single running variable holding the right-side (suffix) product, multiplying it into each slot on the way.

The output array does double duty: after the forward pass it stores prefix products, and the backward pass folds in the suffix products in place. Nothing but one scalar of extra state is needed, which meets the follow-up's O(1) space bar.

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        answer[0] = 1;
        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= suffix;
            suffix *= nums[i];
        }
        return answer;
    }
}
```

## Why it works

After the forward loop, `answer[i]` equals the product of everything to the left of `i`. In the backward loop, `suffix` carries the product of everything to the right of the current index; multiplying it into `answer[i]` completes the "left times right" formula. Because `suffix` is updated *after* it is used, index `i` never includes `nums[i]` itself.

## Complexity

- Time: O(n) — two linear passes.
- Space: O(1) — only the running suffix variable, excluding the output array.
