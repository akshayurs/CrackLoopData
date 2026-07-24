You are given an array `people` where `people[i]` is the weight of the i-th person, and an integer `limit` for the maximum weight a single boat can carry. Each boat holds **at most two people**, provided their combined weight does not exceed `limit`.

Return the minimum number of boats needed to carry every person.

## Examples

```text
Input:  people = [1, 2], limit = 3
Output: 1        # both people share one boat (1 + 2 = 3)
```

```text
Input:  people = [3, 2, 2, 1], limit = 3
Output: 3        # boats: (1, 2), (2), (3)
```

```text
Input:  people = [3, 5, 3, 4], limit = 5
Output: 4        # no two people fit together, so everyone rides alone
```

## Constraints

- 1 <= people.length <= 5 * 10^4
- 1 <= people[i] <= limit <= 3 * 10^4

## Follow-up

Every person's weight is at most `limit`, so each person can always fit on some boat. Can you reach the minimum without trying every pairing?
