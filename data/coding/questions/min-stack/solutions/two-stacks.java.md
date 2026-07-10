The insight is that the minimum only ever changes at push and pop boundaries, so you can precompute it. Alongside the main stack, keep a second "min stack" whose top always holds the minimum of everything below and including the current top of the main stack. When you push `val`, push `min(val, previousMin)` onto the min stack; when you pop, pop both in lockstep.

Now `getMin` is just reading the top of the min stack — no scan. Because the two stacks grow and shrink together, the min stack's top is always in sync with the current contents, which turns the linear query into a constant-time lookup.

```java
import java.util.ArrayDeque;
import java.util.Deque;

class MinStack {
    private final Deque<Integer> stack = new ArrayDeque<>();
    private final Deque<Integer> mins = new ArrayDeque<>();

    public void push(int val) {
        stack.push(val);
        int curMin = mins.isEmpty() ? val : Math.min(val, mins.peek());
        mins.push(curMin);
    }

    public void pop() {
        stack.pop();
        mins.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return mins.peek();
    }
}
```

## Why it works

The top of `mins` is invariant: it equals the minimum of every value currently on the main stack. On push, the new minimum is either the new value or the old minimum, so `Math.min(val, mins.peek())` maintains it. On pop, removing the top of both stacks restores the exact state that existed one push earlier — including the correct minimum. Duplicate minimums are handled naturally: each push records its own min entry, so popping one copy leaves the other's entry intact.

## Complexity

- Time: O(1) for every operation, including `getMin`.
- Space: O(n) — the auxiliary min stack mirrors the main stack's size.
