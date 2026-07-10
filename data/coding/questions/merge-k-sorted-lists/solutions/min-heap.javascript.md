Each of the k lists is already sorted, so the smallest value not yet placed in the answer is always sitting at the front of one of them. Keep the current front node of every list in a min-heap, keyed by value; the heap top is always the global minimum. Pop it, attach it to the result, and if the list it came from has more nodes, push its new front back in.

JavaScript has no built-in priority queue, so a tiny binary min-heap over the nodes themselves (compared by `val`) does the job.

```javascript
class MinHeap {
  constructor() { this.data = []; }
  size() { return this.data.length; }
  push(node) {
    this.data.push(node);
    let i = this.data.length - 1;
    while (i > 0) {
      const parent = (i - 1) >> 1;
      if (this.data[parent].val <= this.data[i].val) break;
      [this.data[parent], this.data[i]] = [this.data[i], this.data[parent]];
      i = parent;
    }
  }
  pop() {
    const top = this.data[0];
    const last = this.data.pop();
    if (this.data.length > 0) {
      this.data[0] = last;
      let i = 0;
      while (true) {
        let smallest = i, left = 2 * i + 1, right = 2 * i + 2;
        if (left < this.data.length && this.data[left].val < this.data[smallest].val) smallest = left;
        if (right < this.data.length && this.data[right].val < this.data[smallest].val) smallest = right;
        if (smallest === i) break;
        [this.data[i], this.data[smallest]] = [this.data[smallest], this.data[i]];
        i = smallest;
      }
    }
    return top;
  }
}

function mergeKLists(lists) {
  const heap = new MinHeap();
  for (const node of lists) if (node) heap.push(node);

  const dummy = new ListNode(0);
  let tail = dummy;
  while (heap.size() > 0) {
    const node = heap.pop();
    tail.next = node;
    tail = tail.next;
    if (node.next) heap.push(node.next);
  }
  return dummy.next;
}
```

## Why it works

At any point the heap holds at most one candidate node per still-active list — its unconsumed front — because each list is sorted, so that front is that list's smallest remaining value. The true global minimum across all lists must therefore be one of those fronts, which is exactly what the heap top gives you. Popping it and pushing its successor keeps the invariant true for the next round, and splicing the popped node directly onto `tail` reuses the original nodes instead of copying values.

## Complexity

- Time: O(N log k) — N total nodes, each causing one push and one pop on a heap of size at most k.
- Space: O(k) — the heap never holds more than one node per list.
