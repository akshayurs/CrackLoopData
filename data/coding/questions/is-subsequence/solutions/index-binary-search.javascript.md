When many queries share the same `t`, the linear scan re-reads all of `t` every time — wasteful. Instead, preprocess `t` once into a map from each character to the sorted list of positions where it occurs. Then a query only touches positions relevant to `s`.

For each character of `s`, we need the earliest occurrence in `t` that comes *after* the position we matched last. Since each character's positions are sorted, a binary search (upper bound of the previous index) finds it in logarithmic time. If any character has no such later position, `s` cannot be embedded.

```javascript
function isSubsequence(s, t) {
    const positions = new Map();
    for (let i = 0; i < t.length; i++) {
        if (!positions.has(t[i])) positions.set(t[i], []);
        positions.get(t[i]).push(i);
    }
    let prev = -1;
    for (const c of s) {
        const idxs = positions.get(c);
        if (!idxs) return false;
        let lo = 0, hi = idxs.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (idxs[mid] <= prev) lo = mid + 1;
            else hi = mid;
        }
        if (lo === idxs.length) return false;
        prev = idxs[lo];
    }
    return true;
}
```

## Why it works

`positions.get(c)` lists, in increasing order, every index of `c` in `t`. Maintaining `prev` (the index we last consumed), the next character must land at some index strictly greater than `prev`; the binary search returns the first slot whose value exceeds `prev`. Advancing to the smallest valid index is the greedy choice — the same reasoning as the two-pointer scan — so it never rejects an embeddable string. Missing character or exhausted positions means no valid match remains.

## Complexity

- Time: O(n + m·log n) — building the index over `t` (length n), then each of the m = s.length characters does one binary search.
- Space: O(n) — every position of `t` is stored once.
