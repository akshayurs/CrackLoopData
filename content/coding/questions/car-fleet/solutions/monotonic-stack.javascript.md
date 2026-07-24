The only thing that decides whether two cars merge is *arrival time*. A car behind catches the one ahead exactly when it would otherwise reach the destination sooner — so compute each car's time to the target, `(target - position) / speed`, and reason about who arrives when.

Process cars from the one nearest the destination backwards. Keep a stack of fleet arrival times. If the current car would arrive *later* than the fleet directly ahead, it can never catch up, so it starts its own fleet and is pushed. Otherwise it catches that fleet and is absorbed — nothing is pushed. The stack size is the fleet count.

```javascript
function carFleet(target, position, speed) {
  const cars = position.map((p, i) => [p, speed[i]]);
  cars.sort((a, b) => b[0] - a[0]);
  const stack = [];
  for (const [pos, spd] of cars) {
    const time = (target - pos) / spd;
    if (stack.length === 0 || time > stack[stack.length - 1]) {
      stack.push(time);
    }
  }
  return stack.length;
}
```

## Why it works

Sorting by position descending means we always look at cars in the order they sit on the road, front to back. The top of the stack is the arrival time of the fleet immediately ahead. A trailing car whose `time` is `<=` that value reaches the target no later than the fleet, so it bunches up behind it and inherits the slower time — we drop it. A car with a strictly larger time is too slow to catch anyone ahead and forms a fresh fleet. Every push corresponds to exactly one fleet that arrives independently.

## Complexity

- Time: O(n log n) — dominated by sorting the cars by position.
- Space: O(n) — the stack of arrival times.
