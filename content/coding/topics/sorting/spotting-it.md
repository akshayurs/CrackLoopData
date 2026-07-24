Reach for a sorting-family technique the moment a problem sounds like any of these:

- **"Sort this array/list"** — directly asks you to implement or apply a sort. If they say "without using the built-in sort," they want you to write merge/quick/heap sort by hand.
- **"Array contains numbers from 1 to n" / "0 to n-1"** — the index-as-hash signal for **cyclic sort**: find missing number, find duplicate, find all duplicates, first missing positive.
- **"K-th largest/smallest" / "top-K"** — quickselect or a heap; if they emphasize O(n) average, they want quickselect specifically.
- **"Sort by a custom rule"** — colors/categories (Dutch national flag), frequency (bucket sort by count), or a comparator that isn't plain numeric order (largest number formed by concatenation, custom string order).
- **"Count pairs/inversions where earlier > later"** — merge sort augmented to count cross-pairs while merging (reverse pairs, count of smaller numbers after self).
- **"Nearly sorted" / "sorted except a few elements"** — wiggle sort, pancake sort, or gap-based questions like Maximum Gap where a linear-time bucket approach beats comparison sort.
- **"Merge two sorted things in place"** — merge sorted array, working from the back to avoid overwriting.

Signal words: *"k-th"*, *"missing"*, *"duplicate"*, *"in-place"*, *"custom order"*, *"contains 1 to n"*, *"without extra space"*. If the input is already sorted or nearly sorted and the ask is about relative order or gaps, sorting-based reasoning is almost always the intended path.
