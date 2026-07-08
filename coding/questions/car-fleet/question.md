There are `n` cars driving toward the same destination along a one-lane road. The destination is `target` miles away. Car `i` starts at `position[i]` miles from the start and travels at `speed[i]` miles per hour.

A faster car can never pass a slower one ahead of it — when it catches up, it slows down and the two travel bumper-to-bumper as a single **fleet**. Cars that reach the destination at the same moment as the car in front also count as one fleet. Return the number of distinct car fleets that arrive at the destination.

## Examples

```text
Input:  target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]
Output: 3        # fleets: {10,8}, {5,3}, {0}
```

```text
Input:  target = 10, position = [3], speed = [3]
Output: 1        # a single car is one fleet
```

```text
Input:  target = 100, position = [0, 2, 4], speed = [4, 2, 1]
Output: 1        # the slow front car bunches everyone behind it
```

## Constraints

- 1 <= n == position.length == speed.length <= 10^5
- 0 <= position[i] < target <= 10^6
- 0 < speed[i] <= 10^6
- All values in `position` are distinct.

## Follow-up

Can you avoid the explicit stack and answer in O(1) extra space beyond the sort?
