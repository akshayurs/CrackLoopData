An anagram is defined purely by letter frequencies, so build a 26-slot frequency signature for `p` once and compare it against the signature of every length-`|p|` window in `s`. Identical counts mean one string is an anagram of the other.

This version recomputes the window's counts from scratch at each position — simple to follow, and a natural starting point before optimizing.

```javascript
function findAnagrams(s, p) {
  const m = p.length;
  if (m > s.length) return [];
  const count = (str) => {
    const c = new Array(26).fill(0);
    for (const ch of str) c[ch.charCodeAt(0) - 97]++;
    return c;
  };
  const target = count(p);
  const result = [];
  for (let i = 0; i + m <= s.length; i++) {
    const w = count(s.slice(i, i + m));
    if (w.every((v, j) => v === target[j])) result.push(i);
  }
  return result;
}
```

## Why it works

The `count` helper maps a string to how many of each of the 26 lowercase letters it holds. A substring is an anagram of `p` exactly when its count array equals `target`. Testing every window of width `m` finds all matches, and scanning left to right yields the indices in ascending order.

## Complexity

- Time: O(n * m) — for each of the ~n start positions we build and compare a count over m characters.
- Space: O(1) — each count array holds 26 fixed slots.
