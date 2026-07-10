You are given an integer array `bloomDay`, where `bloomDay[i]` is the day on which the flower at position `i` blooms. You are also given two integers `m` and `k`.

To assemble one bouquet you must pick exactly `k` **adjacent** flowers that have already bloomed. Each flower can belong to at most one bouquet. Return the minimum number of days you must wait so that you can make `m` bouquets. If it is impossible to make that many bouquets at all, return `-1`.

## Examples

```text
Input:  bloomDay = [1, 10, 3, 10, 2], m = 3, k = 1
Output: 3        # by day 3 the flowers at 0, 2, 4 have bloomed → three 1-flower bouquets
```

```text
Input:  bloomDay = [1, 10, 3, 10, 2], m = 3, k = 2
Output: -1       # 3 bouquets × 2 flowers = 6 flowers needed, only 5 exist
```

```text
Input:  bloomDay = [7, 7, 7, 7, 12, 7, 7], m = 2, k = 3
Output: 12       # on day 12 all 7 flowers are open → two 3-flower bouquets
```

## Constraints

- 1 <= bloomDay.length <= 10^5
- 1 <= bloomDay[i] <= 10^9
- 1 <= m <= 10^6
- 1 <= k <= bloomDay.length

## Follow-up

The feasibility of "can I make `m` bouquets by day `d`?" is monotonic in `d`. Can you exploit that to avoid scanning every candidate day?
