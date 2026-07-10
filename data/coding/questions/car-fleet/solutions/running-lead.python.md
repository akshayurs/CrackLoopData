The stack in the previous approach only ever grows — a car is compared against the fleet directly ahead, and once it merges it never affects anyone behind it. That means we never need the full stack: a single scalar holding the arrival time of the frontmost fleet so far is enough.

Sort by position descending and sweep. Track `lead_time`, the arrival time of the current lead fleet. Any car that would arrive strictly later than `lead_time` cannot catch up, so it becomes the new lead fleet and we bump the count; everything with `time <= lead_time` is absorbed and ignored.

```python
def car_fleet(target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)
    fleets = 0
    lead_time = 0.0
    for pos, spd in cars:
        time = (target - pos) / spd
        if time > lead_time:
            fleets += 1
            lead_time = time
    return fleets
```

## Why it works

Walking front to back, the fleet a car might join is always the most recent one that arrived latest — precisely `lead_time`. A larger `time` means the car trails behind and reaches the target on its own, so it opens a new fleet and raises the lead. A smaller-or-equal `time` means it catches the lead fleet and merges silently. Because arrival times of new fleets are strictly increasing along the sweep, one running maximum captures every merge decision the stack made.

## Complexity

- Time: O(n log n) — the sort dominates.
- Space: O(1) — only two scalars beyond the sort.
