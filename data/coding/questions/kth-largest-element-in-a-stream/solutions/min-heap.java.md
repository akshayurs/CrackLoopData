You never need the full sorted history — only the k largest values matter, and among those only the smallest one (the k-th largest overall). Keep a min-heap capped at size k: whenever it grows past k, pop the smallest, since anything smaller than the current k-th largest can never become the answer again.

After seeding the heap with the initial array (trimmed to its k largest), every `add` is a single push, and possibly one pop, followed by peeking at the heap's root.

```java
import java.util.PriorityQueue;

class KthLargest {
    private final int k;
    private final PriorityQueue<Integer> heap;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.heap = new PriorityQueue<>();
        for (int n : nums) {
            heap.offer(n);
            if (heap.size() > k) {
                heap.poll();
            }
        }
    }

    public int add(int val) {
        heap.offer(val);
        if (heap.size() > k) {
            heap.poll();
        }
        return heap.peek();
    }
}
```

## Why it works

A min-heap of size k always holds exactly the k largest values seen so far, with the smallest of that group at the root. Pushing a new value and evicting the root when the heap overflows keeps that invariant intact, so the root is always the k-th largest element after every `add`.

## Complexity

- Time: O(log k) per call to `add` — one offer and at most one poll on a heap of size k.
- Space: O(k) — the heap only ever holds the k largest values.
