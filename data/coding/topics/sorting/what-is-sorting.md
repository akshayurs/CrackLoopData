**Sorting** means arranging elements into an order (numeric, lexicographic, or by a custom key) so that structure you couldn't see before — duplicates lining up, the smallest/largest sitting at the ends, matching pairs sitting next to each other — becomes visible and cheap to exploit.

Comparison sorts (merge sort, quicksort, heapsort) give you O(n log n) in general, and are the ones you should be able to *implement from memory*: partitioning for quicksort, the merge step for merge sort, sift-down for heapsort. Beyond them sit the non-comparison sorts — **counting sort**, **bucket sort**, **radix sort** — which beat the n log n bound to O(n + k) when your keys are bounded integers or can be bucketed.

A special case worth knowing by name is **cyclic sort**: when you're given an array containing exactly the numbers `1..n` (or `0..n-1`), you can place each value at its "home" index by swapping, in O(n) time and O(1) space — no comparisons needed. This is the array-as-hash-map trick: the index itself encodes the value.

```
i = 0
while i < n:
    correct = arr[i] - 1
    if arr[i] != arr[correct]:
        swap(arr[i], arr[correct])
    else:
        i += 1
```

After this pass, any index `i` where `arr[i] != i + 1` reveals a missing or duplicate number — read the answer straight off the array. **Quickselect**, a quicksort partition without recursing on both sides, gets you the k-th smallest/largest in expected O(n), which is often the real ask behind a sorting-flavored question.
