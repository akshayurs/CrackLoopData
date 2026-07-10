Start with the simplest thing that works: keep the values in one ordinary array used as a stack. Push, pop, and top are trivial array operations. The only interesting method is `getMin`, and the naive answer is to look at everything currently stored and take the smallest.

This is easy to reason about and obviously correct, but it pays for that simplicity on every `getMin` call — scanning the whole stack means the minimum query is linear, not constant.

```javascript
class MinStack {
  constructor() {
    this.stack = [];
  }
  push(val) {
    this.stack.push(val);
  }
  pop() {
    this.stack.pop();
  }
  top() {
    return this.stack[this.stack.length - 1];
  }
  getMin() {
    return Math.min(...this.stack);
  }
}
```

## Why it works

A JavaScript array used as a stack gives O(1) `push`, `pop`, and last-element access, so the LIFO behaviour is exactly right. `getMin` spreads the array into `Math.min`, which returns the smallest value among everything still on the stack — by definition the current minimum. Nothing extra is tracked, so there is no bookkeeping to get wrong.

## Complexity

- Time: O(1) for `push`, `pop`, `top`; O(n) for `getMin` — it inspects every element.
- Space: O(n) — the single stack holds all pushed values.
