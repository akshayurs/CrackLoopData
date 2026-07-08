A **heap** (binary heap) is a complete binary tree stored in an array, kept in **partial order**: every parent is smaller (min-heap) or larger (max-heap) than its children. It is not fully sorted — only the root is guaranteed to be the smallest (or largest) element.

A **priority queue** is the abstract interface heaps implement: insert an item, and always pop the "highest priority" one next, in **O(log n)** per operation. Peeking at the top is O(1). That is the whole superpower — you never need to re-scan or re-sort the collection to find the current best.

This beats sorting when you only ever care about the extreme end of a changing collection. Sorting the full list is O(n log n) up front and gives you no way to cheaply insert new elements afterward. A heap keeps "what's the min/max right now" instantly available while items stream in and out.

The classic shape for "keep the k best":

```
heap = empty (size-k min-heap for "k largest")
for each element x:
    push x onto heap
    if heap size > k:
        pop the smallest
answer = heap now holds the k largest elements
```

Two closely related uses:

- **Top-K / kth-largest streaming**: bound the heap to size k so it only ever holds the candidates that matter.
- **Merge k sorted things**: push the head of each list/stream with its source tag; pop the min, push that source's next element. This drives merge-k-lists and "smallest range across k lists" problems.
- **Two heaps for median**: a max-heap for the lower half and a min-heap for the upper half, kept balanced, gives O(log n) insert and O(1) median lookup.
