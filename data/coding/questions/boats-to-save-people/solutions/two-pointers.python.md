The brute-force scan repeats work: after sorting, the lightest available person is always at the front and the heaviest at the back, so there is no need to search for a partner. Keep one pointer at each end.

Look at the heaviest person. If the lightest remaining person can share their boat, seat both and move both pointers inward; otherwise the heavy person goes alone and only the back pointer moves. Either way one boat launches per step, and the pointers converge in a single pass.

```python
def num_rescue_boats(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    boats = 0
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        boats += 1
    return boats
```

## Why it works

Sorting lets the two pointers name the lightest (`i`) and heaviest (`j`) unplaced people in O(1). The heaviest person must board some boat now; pairing them with the lightest that fits is never worse than any other pairing, because any partner who fits the heaviest also fits every lighter anchor. When the lightest cannot join the heaviest, no one can, so `j` sails solo. Each iteration launches exactly one boat and removes at least one person, so the count is minimal.

## Complexity

- Time: O(n log n) — dominated by the sort; the scan itself is O(n).
- Space: O(1) — only two indices beyond the sort.
