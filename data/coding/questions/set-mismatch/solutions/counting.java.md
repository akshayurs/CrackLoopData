Rescanning the array for every candidate wastes work — the counts can all be gathered in a single sweep. Tally how often each value appears using a frequency array indexed by the value itself, then read off which count is `2` and which is `0`.

Because the values are guaranteed to live in `1..n`, a fixed-size array of counts is enough; no general hash map is required.

```java
class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        int[] counts = new int[n + 1];
        for (int x : nums) counts[x]++;
        int duplicated = -1, missing = -1;
        for (int v = 1; v <= n; v++) {
            if (counts[v] == 2) duplicated = v;
            else if (counts[v] == 0) missing = v;
        }
        return new int[]{duplicated, missing};
    }
}
```

## Why it works

The first pass records the exact multiplicity of every value in `O(1)` per element. In a correct set each slot would hold `1`; the single duplicate pushes one slot to `2` and steals the tally from another, leaving its slot at `0`. Scanning the counts once identifies both. The array of size `n + 1` lets us index by value directly and ignore slot `0`.

## Complexity

- Time: O(n) — one pass to count, one pass to inspect.
- Space: O(n) — the frequency array holds n + 1 slots.
</content>
