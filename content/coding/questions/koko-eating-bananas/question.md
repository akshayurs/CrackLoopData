Koko has `n` piles of bananas, where `piles[i]` is the number of bananas in the i-th pile. A guard will return in `h` hours, and Koko wants to finish every pile before then.

She picks an eating speed of `k` bananas per hour. Each hour she chooses a single pile and eats up to `k` bananas from it; if that pile has fewer than `k` bananas left, she eats the whole pile and idles for the rest of the hour (she never starts a second pile in the same hour). Return the **smallest** integer speed `k` that lets her finish all the bananas within `h` hours.

## Examples

```text
Input:  piles = [3, 6, 7, 11], h = 8
Output: 4        # hours = 1 + 2 + 2 + 3 = 8
```

```text
Input:  piles = [30, 11, 23, 4, 20], h = 5
Output: 30       # only 5 hours for 5 piles, so k must clear the largest pile
```

```text
Input:  piles = [30, 11, 23, 4, 20], h = 6
Output: 23
```

## Constraints

- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9

## Follow-up

The hours Koko needs strictly decrease as `k` grows: every speed at or above the answer finishes in time, every speed below it does not. Can you exploit that monotonicity to avoid testing each candidate speed one by one?
