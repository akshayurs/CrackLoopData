The stack in the previous approach only ever grows — a car is compared against the fleet directly ahead, and once it merges it never affects anyone behind it. That means we never need the full stack: a single scalar holding the arrival time of the frontmost fleet so far is enough.

Sort by position descending and sweep. Track `leadTime`, the arrival time of the current lead fleet. Any car that would arrive strictly later than `leadTime` cannot catch up, so it becomes the new lead fleet and we bump the count; everything with `time <= leadTime` is absorbed and ignored.

```javascript
function carFleet(target, position, speed) {
  const cars = position.map((p, i) => [p, speed[i]]);
  cars.sort((a, b) => b[0] - a[0]);
  let fleets = 0;
  let leadTime = 0;
  for (const [pos, spd] of cars) {
    const time = (target - pos) / spd;
    if (time > leadTime) {
      fleets++;
      leadTime = time;
    }
  }
  return fleets;
}
```

## Why it works

Walking front to back, the fleet a car might join is always the most recent one that arrived latest — precisely `leadTime`. A larger `time` means the car trails behind and reaches the target on its own, so it opens a new fleet and raises the lead. A smaller-or-equal `time` means it catches the lead fleet and merges silently. Because arrival times of new fleets are strictly increasing along the sweep, one running maximum captures every merge decision the stack made.

## Complexity

- Time: O(n log n) — the sort dominates.
- Space: O(1) — only two scalars beyond the sort.
