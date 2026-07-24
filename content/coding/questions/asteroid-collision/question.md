You are given an array `asteroids` of non-zero integers representing asteroids moving in a row. The absolute value is an asteroid's size and the sign is its direction: positive means moving right, negative means moving left. Every asteroid moves at the same speed.

When two asteroids meet, the smaller one explodes. If both are the same size, both explode. Two asteroids moving in the same direction never meet, and a left-moving asteroid to the left of a right-moving one never meets it either. Return the state of the asteroids after all collisions resolve, preserving their left-to-right order.

## Examples

```text
Input:  asteroids = [5, 10, -5]
Output: [5, 10]        # 10 and -5 collide; -5 explodes. 5 and 10 both move right.
```

```text
Input:  asteroids = [8, -8]
Output: []             # equal size, both explode.
```

```text
Input:  asteroids = [10, 2, -5]
Output: [10]           # 2 and -5 collide (2 explodes) → 10 and -5 collide (-5 explodes).
```

## Constraints

- 2 <= asteroids.length <= 10^4
- -1000 <= asteroids[i] <= 1000
- asteroids[i] != 0

## Follow-up

The naive fix-point scan re-checks the whole array after every explosion. Can you resolve all collisions in a single left-to-right pass?
