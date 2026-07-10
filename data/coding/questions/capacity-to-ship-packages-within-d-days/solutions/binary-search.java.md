Feasibility is monotonic: if capacity `c` ships everything in time, so does every capacity larger than `c`, and every smaller one is no better. That "false, false, …, true, true" shape over the capacity axis is exactly what binary search exploits — instead of scanning capacities one at a time, halve the search range each step.

The range is fixed: the smallest usable capacity is `max(weights)` (a day must hold the heaviest package) and the largest ever needed is `sum(weights)` (ship it all in one day). Binary search that range, testing the midpoint with the same greedy day-count simulation, and converge on the smallest feasible capacity.

```java
class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int lo = 0, hi = 0;
        for (int w : weights) {
            lo = Math.max(lo, w);
            hi += w;
        }
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (daysNeeded(weights, mid) <= days) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private int daysNeeded(int[] weights, int cap) {
        int used = 1, load = 0;
        for (int w : weights) {
            if (load + w > cap) {
                used++;
                load = 0;
            }
            load += w;
        }
        return used;
    }
}
```

## Why it works

`daysNeeded` returns how many days the greedy loading takes at a given capacity. Because that count never increases as capacity grows, the feasible capacities form a suffix of the range. The loop keeps `[lo, hi]` bracketing the answer: when `mid` is feasible we discard everything above it (`hi = mid`), otherwise the answer must be larger (`lo = mid + 1`). The invariant collapses `lo` and `hi` onto the smallest feasible capacity.

## Complexity

- Time: O(n · log S) — each of the O(log S) binary-search steps runs an O(n) feasibility check, where S is the total weight.
- Space: O(1) — only a few counters.
