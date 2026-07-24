Process the asteroids left to right and keep the survivors on a stack. A right-moving asteroid (positive) can never collide with anything already settled, so it just goes on the stack. A left-moving asteroid (negative) is the only thing that starts a fight, and it only fights right-movers sitting on top of the stack.

For each incoming left-mover, repeatedly compare it against the stack top: if the top is smaller it pops (explodes) and the fight continues; if they tie, both die; if the top is larger, the incoming asteroid dies. If the left-mover survives an empty-or-left-moving top, it lands on the stack. One pass resolves everything because the stack always holds exactly the asteroids that could still be hit from the right.

```javascript
function asteroidCollision(asteroids) {
  const stack = [];
  for (const a of asteroids) {
    let alive = true;
    while (alive && a < 0 && stack.length && stack[stack.length - 1] > 0) {
      const top = stack[stack.length - 1];
      if (top < -a) {
        stack.pop();
      } else if (top === -a) {
        stack.pop();
        alive = false;
      } else {
        alive = false;
      }
    }
    if (alive) stack.push(a);
  }
  return stack;
}
```

## Why it works

The stack is an invariant: it stores the current survivors in order, and its right end is the only place a new left-mover can strike. A negative asteroid keeps popping positive tops smaller than it (each of those genuinely explodes), stops and dies if it meets an equal or larger top, and otherwise settles once the top is negative or the stack is empty. Positives never trigger collisions, so pushing them directly is correct.

## Complexity

- Time: O(n) — each asteroid is pushed and popped at most once.
- Space: O(n) — the stack in the worst case (all same direction).
