Reach for pointer manipulation on a singly (or doubly) linked list the moment a problem sounds like any of these:

- **"Reverse the list"** — fully, or "in groups of k", or "between positions m and n". Always a `prev`/`curr` rewiring exercise.
- **"Does the list have a cycle?" / "Where does the cycle begin?"** — Floyd's fast/slow pointer, and the entry-point trick after the first meeting.
- **"Find the middle node"** — fast/slow pointers, no length pre-count needed.
- **"Merge two (or k) sorted lists"** — walk both, splice the smaller head each time; a min-heap generalizes this to k lists.
- **"Remove the nth node from the end"** — two pointers offset by n, moved together.
- **"Is it a palindrome?"** — find the middle, reverse the second half, compare.
- **"Reorder / interleave the list"** (e.g. L0→Ln→L1→Ln-1…) — split, reverse the tail half, merge alternately.
- **"Deep copy a list with a random pointer"** — needs an old-node → new-node map (or interleaving trick) since `next` alone doesn't capture the extra edges.
- **"Add two numbers represented as lists"** — digit-by-digit walk with carry, building a new list.

Signal words: *"node"*, *"pointer"*, *"next"*, *"cycle"*, *"in-place"*, *"without extra space"*, *"k-th from the end"*. If the input is described as a chain of nodes rather than an indexable array, and the ask involves rearranging structure rather than just reading values, this is the pattern.
