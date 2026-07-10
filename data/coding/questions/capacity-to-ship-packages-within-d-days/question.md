A conveyor belt carries a queue of packages that must all be shipped within `days` days. The `i`-th package has weight `weights[i]`. Every day, the ship is loaded with packages **in the given order** — you may not reorder them. The total weight loaded on any single day may not exceed the ship's capacity.

Return the **minimum** ship capacity that still lets you deliver every package within `days` days.

## Examples

```text
Input:  weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5
Output: 15
# Day 1: 1,2,3,4,5   Day 2: 6,7   Day 3: 8   Day 4: 9   Day 5: 10
# A capacity below 15 cannot fit the first five packages in one day.
```

```text
Input:  weights = [3, 2, 2, 4, 1, 4], days = 3
Output: 6
# Day 1: 3,2   Day 2: 2,4   Day 3: 1,4
```

```text
Input:  weights = [1, 2, 3, 1, 1], days = 4
Output: 3
# Day 1: 1,2   Day 2: 3   Day 3: 1,1   (uses 3 days, within the limit)
```

## Constraints

- 1 <= days <= weights.length <= 5 * 10^4
- 1 <= weights[i] <= 500

## Follow-up

The number of days needed decreases monotonically as capacity grows. Can you exploit that monotonicity instead of trying every capacity one by one?
