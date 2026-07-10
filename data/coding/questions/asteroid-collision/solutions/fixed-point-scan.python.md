A collision only ever happens between adjacent asteroids where a right-mover sits directly left of a left-mover — a `+, -` pair. The most direct approach is to keep scanning the array for the first such pair, resolve it, and start over, repeating until a full pass finds nothing left to collide.

Each resolution removes one or both of the colliding asteroids, so the array only shrinks. When a pass completes without touching anything, the arrangement is stable and we return it. It is simple to reason about but wasteful: one explosion forces a re-scan from the beginning.

```python
def asteroid_collision(asteroids):
    arr = list(asteroids)
    stable = False
    while not stable:
        stable = True
        for i in range(len(arr) - 1):
            if arr[i] > 0 and arr[i + 1] < 0:
                stable = False
                right, left = arr[i], -arr[i + 1]
                if right < left:
                    del arr[i]
                elif right > left:
                    del arr[i + 1]
                else:
                    del arr[i:i + 2]
                break
    return arr
```

## Why it works

Only a `positive, negative` adjacency can collide; any other pair is stable. We always resolve the leftmost such pair, delete the loser (or both on a tie), then restart the scan because deleting an element can create a brand-new adjacency. The array shrinks on every non-trivial pass, so the loop terminates, and it exits exactly when no collidable pair remains.

## Complexity

- Time: O(n^2) — up to O(n) explosions, each triggering an O(n) rescan.
- Space: O(1) — resolved in place, ignoring the output copy.
