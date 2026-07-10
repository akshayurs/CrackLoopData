Start with the simplest thing that works: keep the values in one ordinary stack. Push, pop, and top are trivial deque operations. The only interesting method is `getMin`, and the naive answer is to walk everything currently stored and take the smallest.

This is easy to reason about and obviously correct, but it pays for that simplicity on every `getMin` call — scanning the whole stack means the minimum query is linear, not constant.

```java
import java.util.ArrayDeque;
import java.util.Deque;

class MinStack {
    private final Deque<Integer> stack = new ArrayDeque<>();

    public void push(int val) {
        stack.push(val);
    }

    public void pop() {
        stack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        int min = Integer.MAX_VALUE;
        for (int v : stack) {
            min = Math.min(min, v);
        }
        return min;
    }
}
```

## Why it works

An `ArrayDeque` used as a stack gives O(1) `push`, `pop`, and `peek`, so the LIFO behaviour is exactly right. `getMin` iterates over every element still on the stack, keeping the smallest seen — by definition the current minimum. Nothing extra is tracked, so there is no bookkeeping to get wrong.

## Complexity

- Time: O(1) for `push`, `pop`, `top`; O(n) for `getMin` — it inspects every element.
- Space: O(n) — the single stack holds all pushed values.
