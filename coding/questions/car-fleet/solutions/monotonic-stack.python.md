The only thing that decides whether two cars merge is *arrival time*. A car behind catches the one ahead exactly when it would otherwise reach the destination sooner — so compute each car's time to the target, `(target - position) / speed`, and reason about who arrives when.

Process cars from the one nearest the destination backwards. Keep a stack of fleet arrival times. If the current car would arrive *later* than the fleet directly ahead, it can never catch up, so it starts its own fleet and is pushed. Otherwise it catches that fleet and is absorbed — nothing is pushed. The stack size is the fleet count.

```python
def car_fleet(target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)
    stack = []
    for pos, spd in cars:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)
    return len(stack)
```

## Why it works

Sorting by position descending means we always look at cars in the order they sit on the road, front to back. `stack[-1]` is the arrival time of the fleet immediately ahead. A trailing car with `time <= stack[-1]` reaches the target no later than that fleet, so it bunches up behind it and inherits the fleet's slower time — we simply drop it. A car with a strictly larger time is too slow to catch anyone ahead and forms a fresh fleet. Every push corresponds to exactly one fleet that arrives independently.

## Complexity

- Time: O(n log n) — dominated by sorting the cars by position.
- Space: O(n) — the stack of arrival times.
