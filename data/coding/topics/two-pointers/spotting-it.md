Reach for two pointers the moment a problem sounds like any of these:

- **"The array is sorted"** — stated outright, or implied ("input array is sorted", "in non-decreasing order"). Sorted input is the single strongest signal — it is what makes pointer movement provably correct.
- **"Find a pair/triplet that sums to X"** on sorted data — Two Sum II, 3Sum, 3Sum Closest. Fix one index, converge the other two.
- **"Palindrome" checks** — compare characters from both ends inward, skip non-alphanumeric, bail on mismatch.
- **"Remove/move elements in place"** — Move Zeroes, Remove Duplicates from Sorted Array. A slow pointer marks the "write" position, a fast pointer scans.
- **"Container" / "area" / "capacity between two lines"** — Container With Most Water, Trapping Rain Water. The answer is bounded by the shorter of two ends, so move the shorter side inward.
- **"Merge two sorted …"** — merge sorted arrays/lists by walking both with a pointer each.
- **"Is X a subsequence of Y"** — one pointer per string, advance the second whenever characters match.

Signal words: *"sorted array"*, *"in place"*, *"O(1) extra space"*, *"palindrome"*, *"pair sums to"*, *"merge"*, *"subsequence"*. If a problem gives you a sorted array and asks for a pair or triplet, two pointers should be your first instinct over hashing — it hits the same answer without the extra memory.

A useful gut check: if your first idea is a hash set/map and the array is *already sorted* and space is called out as a constraint, that is the cue to switch to two pointers instead.
