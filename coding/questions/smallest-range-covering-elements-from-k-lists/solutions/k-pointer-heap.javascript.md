Instead of sorting everything up front, walk all `k` lists in lockstep with one pointer each, always advancing whichever list currently holds the smallest pointed-to value. A min-heap gives that minimum in O(log k) instead of scanning all `k` pointers, and tracking the running maximum alongside it turns every heap pop into one candidate range.

At every step the heap's minimum and the tracked maximum define a range that already touches all `k` lists — one element per list is on the "table" at all times — so shrinking is really just advancing the smallest pointer and re-measuring. A tiny binary-heap class keeps this dependency-free.

```javascript
class MinHeap {
  constructor() {
    this.data = [];
  }
  push(item) {
    this.data.push(item);
    let i = this.data.length - 1;
    while (i > 0) {
      const parent = (i - 1) >> 1;
      if (this.data[parent][0] <= this.data[i][0]) break;
      [this.data[parent], this.data[i]] = [this.data[i], this.data[parent]];
      i = parent;
    }
  }
  pop() {
    const top = this.data[0];
    const last = this.data.pop();
    if (this.data.length) {
      this.data[0] = last;
      let i = 0;
      while (true) {
        const l = 2 * i + 1, r = 2 * i + 2;
        let smallest = i;
        if (l < this.data.length && this.data[l][0] < this.data[smallest][0]) smallest = l;
        if (r < this.data.length && this.data[r][0] < this.data[smallest][0]) smallest = r;
        if (smallest === i) break;
        [this.data[smallest], this.data[i]] = [this.data[i], this.data[smallest]];
        i = smallest;
      }
    }
    return top;
  }
}

function smallestRange(lists) {
  const heap = new MinHeap();
  let currentMax = -Infinity;
  lists.forEach((lst, i) => {
    heap.push([lst[0], i, 0]);
    currentMax = Math.max(currentMax, lst[0]);
  });

  let best = [heap.data[0][0], currentMax];

  while (true) {
    const [value, listI, elemI] = heap.pop();
    if (currentMax - value < best[1] - best[0]) best = [value, currentMax];

    if (elemI + 1 === lists[listI].length) return best;

    const nextValue = lists[listI][elemI + 1];
    currentMax = Math.max(currentMax, nextValue);
    heap.push([nextValue, listI, elemI + 1]);
  }
}
```

## Why it works

The heap always holds exactly one element per list, so its minimum and the tracked maximum bound the tightest range currently touching every list. Popping the minimum and advancing that list's pointer is the only way to shrink the range further, since raising the low end past any other pointer would drop that list out of coverage. The moment a list runs out of elements, no smaller range can be completed, so the best range found so far is final.

## Complexity

- Time: O(N log k) — N is the total number of elements; each of the N heap operations costs O(log k).
- Space: O(k) — the heap holds exactly one entry per list.
