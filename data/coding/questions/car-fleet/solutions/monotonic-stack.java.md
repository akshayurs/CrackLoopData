The only thing that decides whether two cars merge is *arrival time*. A car behind catches the one ahead exactly when it would otherwise reach the destination sooner — so compute each car's time to the target, `(target - position) / speed`, and reason about who arrives when.

Process cars from the one nearest the destination backwards. Keep a stack of fleet arrival times. If the current car would arrive *later* than the fleet directly ahead, it can never catch up, so it starts its own fleet and is pushed. Otherwise it catches that fleet and is absorbed. The stack size is the fleet count.

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
        double[] stack = new double[n];
        int top = 0;
        for (int[] car : cars) {
            double time = (double) (target - car[0]) / car[1];
            if (top == 0 || time > stack[top - 1]) {
                stack[top++] = time;
            }
        }
        return top;
    }
}
```

## Why it works

Sorting by position descending walks the cars front to back. `stack[top - 1]` is the arrival time of the fleet immediately ahead. A trailing car whose `time` is `<=` that value reaches the target no later than the fleet, so it bunches up behind and inherits the slower time — we skip it. A car with a strictly larger time is too slow to catch anyone ahead and forms a fresh fleet. Each stored entry is one independently arriving fleet.

## Complexity

- Time: O(n log n) — dominated by sorting the cars by position.
- Space: O(n) — the stack of arrival times.
