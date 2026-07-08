The only days worth testing are the days on which some flower blooms — between two such days nothing changes. So collect the distinct bloom days, sort them, and try each in increasing order, returning the first day on which `m` bouquets are possible.

Checking a single day is a linear scan: count runs of already-bloomed adjacent flowers, and every full run of length `k` yields one bouquet. If `m * k` exceeds the number of flowers, no day can ever work, so bail out with `-1`.

```java
import java.util.Arrays;

class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        int n = bloomDay.length;
        if ((long) m * k > n) return -1;
        int[] days = Arrays.stream(bloomDay).distinct().sorted().toArray();
        for (int day : days) {
            if (canMake(bloomDay, day, m, k)) return day;
        }
        return -1;
    }

    private boolean canMake(int[] bloomDay, int day, int m, int k) {
        int bouquets = 0, run = 0;
        for (int b : bloomDay) {
            if (b <= day) {
                if (++run == k) { bouquets++; run = 0; }
            } else {
                run = 0;
            }
        }
        return bouquets >= m;
    }
}
```

## Why it works

`canMake` walks left to right, growing a run of consecutive bloomed flowers and cutting one bouquet each time the run hits `k` (resetting so flowers are not reused). Since feasibility only ever changes on a day that some flower blooms, testing the sorted distinct bloom days in order finds the smallest feasible one. The `m * k > n` guard catches the impossible case up front.

## Complexity

- Time: O(n^2) — up to n distinct days, each checked in O(n).
- Space: O(n) — the array of distinct bloom days.
