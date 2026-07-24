The answer must be at least the heaviest single package (otherwise it can never be loaded) and at most the sum of all weights (one giant day). Any capacity in that window can be *tested* directly: greedily pour packages onto the current day until the next one would overflow, then start a new day, and count how many days that takes.

The simplest correct method is to try every candidate capacity starting from the heaviest package and walk upward, returning the first value that ships everything within `days`. Since the day count only ever drops as capacity rises, the first feasible capacity is the minimum.

```javascript
function shipWithinDays(weights, days) {
  const daysNeeded = (cap) => {
    let used = 1, load = 0;
    for (const w of weights) {
      if (load + w > cap) {
        used += 1;
        load = 0;
      }
      load += w;
    }
    return used;
  };

  const lo = Math.max(...weights);
  const hi = weights.reduce((a, b) => a + b, 0);
  for (let cap = lo; cap <= hi; cap++) {
    if (daysNeeded(cap) <= days) return cap;
  }
  return hi;
}
```

## Why it works

`daysNeeded(cap)` simulates the loading rule exactly: keep adding to today's load while it fits, otherwise open a new day. Scanning capacities from the heaviest package upward guarantees the first one that fits in `days` days is the smallest such capacity, because feasibility is monotonic — once a capacity works, every larger one also works.

## Complexity

- Time: O(S · n) — S is the width of the capacity range (up to the total weight), and each feasibility check scans all n packages.
- Space: O(1) — only counters are kept.
