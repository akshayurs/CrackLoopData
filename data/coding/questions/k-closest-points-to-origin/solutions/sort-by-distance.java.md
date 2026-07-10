The simplest correct approach: compute every point's squared distance to the origin, sort the whole array by that distance, and take the first `k`. Squared distance avoids a needless square root and preserves ordering.

Ties are broken by `x` then `y` so the output is deterministic regardless of the input order.

```java
import java.util.Arrays;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int[][] ordered = points.clone();
        Arrays.sort(ordered, (a, b) -> {
            long d = dist(a) - dist(b);
            if (d != 0) return Long.signum(d);
            if (a[0] != b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });
        return Arrays.copyOfRange(ordered, 0, k);
    }

    private long dist(int[] p) {
        return (long) p[0] * p[0] + (long) p[1] * p[1];
    }
}
```

## Why it works

Squared distance is a monotonic function of true distance, so sorting by it yields the same order as sorting by actual distance without a `sqrt` call. Once every point is ordered nearest-to-farthest (with the x/y tiebreak applied when distances match), the first `k` entries are exactly the `k` closest points.

## Complexity

- Time: O(n log n) — one full sort of all points.
- Space: O(n) — the cloned array plus sort overhead.
