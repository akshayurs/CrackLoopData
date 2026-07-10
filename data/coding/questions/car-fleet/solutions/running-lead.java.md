The stack in the previous approach only ever grows — a car is compared against the fleet directly ahead, and once it merges it never affects anyone behind it. That means we never need the full stack: a single scalar holding the arrival time of the frontmost fleet so far is enough.

Sort by position descending and sweep. Track `leadTime`, the arrival time of the current lead fleet. Any car that would arrive strictly later than `leadTime` cannot catch up, so it becomes the new lead fleet and we bump the count; everything with `time <= leadTime` is absorbed and ignored.

```java
import java.util.Arrays;

class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        int[][] cars = new int[n][2];
        for (int i = 0; i < n; i++) {
            cars[i][0] = position[i];
            cars[i][1] = speed[i];
        }
        Arrays.sort(cars, (a, b) -> b[0] - a[0]);
        int fleets = 0;
        double leadTime = 0.0;
        for (int[] car : cars) {
            double time = (double) (target - car[0]) / car[1];
            if (time > leadTime) {
                fleets++;
                leadTime = time;
            }
        }
        return fleets;
    }
}
```

## Why it works

Walking front to back, the fleet a car might join is always the most recent one that arrived latest — precisely `leadTime`. A larger `time` means the car trails behind and reaches the target on its own, so it opens a new fleet and raises the lead. A smaller-or-equal `time` means it catches the lead fleet and merges silently. Because arrival times of new fleets are strictly increasing along the sweep, one running maximum captures every merge decision the stack made.

## Complexity

- Time: O(n log n) — the sort dominates.
- Space: O(1) — only two scalars beyond the sort.
