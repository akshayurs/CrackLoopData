You are given an array `temperatures` where `temperatures[i]` is the temperature recorded on day `i`. For each day, work out how many days you would have to wait until a warmer temperature appears.

Return an array `answer` such that `answer[i]` is the number of days after day `i` before a strictly warmer day. If no future day is warmer, set `answer[i]` to `0`.

## Examples

```text
Input:  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

```text
Input:  temperatures = [30, 40, 50, 60]
Output: [1, 1, 1, 0]
```

```text
Input:  temperatures = [30, 60, 90]
Output: [1, 1, 0]
```

## Constraints

- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

## Follow-up

The brute force scans forward from every day. Can you compute all answers in a single left-to-right pass in O(n) time?
