You are given an array of integers `stones`, where each value is the weight of one stone. Repeatedly pick the two heaviest stones and smash them together: if they are equal, both are destroyed; otherwise the lighter one is destroyed and the heavier one is replaced by the difference of their weights. Keep going until at most one stone is left, then return its weight (or `0` if none remain).

## Examples

```text
Input:  stones = [2, 7, 4, 1, 8, 1]
Output: 1        # 7&8 -> 1, 2&4 -> 2, 2&1 -> 1, 1&1 -> 0, remaining [1] -> 1
```

```text
Input:  stones = [1]
Output: 1        # only one stone, nothing to smash
```

```text
Input:  stones = [3, 3]
Output: 0        # equal stones smash each other into nothing
```

## Constraints

- 1 <= stones.length <= 30
- 1 <= stones[i] <= 1000
