Reach for binary search the moment a problem sounds like any of these:

- **"The array is sorted"** (or "rotated sorted") — direct search for a value, or for its insertion point, first/last occurrence, or a peak.
- **"Find the minimum/maximum X such that condition holds"** — Koko Eating Bananas ("minimum eating speed"), Capacity to Ship Packages ("minimum ship capacity"), Split Array Largest Sum ("minimize the largest subarray sum"), Minimum Days to Make Bouquets. This is binary search on the answer: the answer space (speed, capacity, days) is monotonic even though no array is sorted.
- **"Achieve O(log n)"** stated explicitly — a strong hint the intended solution isn't a linear scan.
- **"Find the boundary / first index where …"** — first true in a sorted true/false space, first bad version, insertion position.
- **Rotated or "almost sorted" arrays** — Search in Rotated Sorted Array, Find Minimum in Rotated Sorted Array: one half is still sorted at every step, which is what makes the halving safe.
- **2D matrices sorted row-wise and column-wise** — treat as a flattened sorted array, or walk from a corner.
- **"K-th smallest / closest"** across a value range rather than a single array — Kth Smallest in a Sorted Matrix, Find K Closest Elements.

Signal words: *"sorted"*, *"minimum/maximum value such that"*, *"O(log n)"*, *"rotated"*, *"first/last position"*, *"closest to"*. If your first instinct is a linear scan and the input is sorted (or the answer space is monotonic), that's the cue to binary-search instead.
