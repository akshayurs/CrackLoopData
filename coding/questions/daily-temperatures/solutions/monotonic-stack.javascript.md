The wasteful part of the brute force is re-scanning days that are colder than something we already passed. Instead, keep a stack of days that are still *waiting* for a warmer temperature, holding their indices in decreasing-temperature order. When today is warmer than the day on top of the stack, today is exactly the warmer day that day was waiting for — so pop it and record the gap.

Each day is pushed once and popped at most once, so the whole scan is linear. The stack always stays sorted by temperature because any day it would break that order for has already been resolved and removed.

```javascript
function dailyTemperatures(temperatures) {
    const n = temperatures.length;
    const answer = new Array(n).fill(0);
    const stack = []; // indices of days awaiting a warmer day
    for (let i = 0; i < n; i++) {
        while (stack.length && temperatures[stack[stack.length - 1]] < temperatures[i]) {
            const prev = stack.pop();
            answer[prev] = i - prev;
        }
        stack.push(i);
    }
    return answer;
}
```

## Why it works

The stack holds indices whose warmer day has not yet arrived, and their temperatures decrease from bottom to top. When day `i` is warmer than the top day `prev`, `i` is the nearest later day that beats `prev` (everything between them was colder, or it would have popped `prev` earlier), so `answer[prev] = i - prev`. Days left on the stack at the end never found a warmer day and keep their `0`.

## Complexity

- Time: O(n) — each index is pushed and popped at most once.
- Space: O(n) — the stack can hold every day in a strictly decreasing run.
