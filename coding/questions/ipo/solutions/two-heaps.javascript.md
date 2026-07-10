The brute force wastes time re-checking affordability from scratch every round. Instead, sort projects by `capital` once. Then, for each of the `k` rounds, move every project whose capital is now affordable into a max-heap keyed by profit (built here as a simple array-backed binary heap, since JS has no built-in one). The top of that max-heap is always the best project money can currently buy.

Once a round's candidates are moved into the max-heap, picking the winner is just popping the top — no rescanning, no re-checking "used" status, because a project only ever moves from the sorted list into the profit-heap once.

```javascript
function maxCapital(k, w, profit, capital) {
  const n = profit.length;
  const order = [...Array(n).keys()].sort((a, b) => capital[a] - capital[b]);
  const heap = []; // max-heap of profits

  const siftUp = (i) => {
    while (i > 0 && heap[(i - 1) >> 1] < heap[i]) {
      const p = (i - 1) >> 1;
      [heap[p], heap[i]] = [heap[i], heap[p]];
      i = p;
    }
  };
  const siftDown = () => {
    let i = 0;
    while (2 * i + 1 < heap.length) {
      let c = 2 * i + 1;
      if (c + 1 < heap.length && heap[c + 1] > heap[c]) c++;
      if (heap[i] >= heap[c]) break;
      [heap[i], heap[c]] = [heap[c], heap[i]];
      i = c;
    }
  };

  let money = w, pos = 0;
  for (let round = 0; round < k; round++) {
    while (pos < n && capital[order[pos]] <= money) {
      heap.push(profit[order[pos]]);
      siftUp(heap.length - 1);
      pos++;
    }
    if (heap.length === 0) break;
    money += heap[0];
    const last = heap.pop();
    if (heap.length) {
      heap[0] = last;
      siftDown();
    }
  }

  return money;
}
```

## Why it works

Sorting by capital lets each project be "unlocked" exactly once, in order, as `money` grows — no project is ever re-examined after it enters the profit max-heap. Within a round, taking the globally best-profit affordable project is safe: money is monotonically non-decreasing, so any project affordable now stays affordable later, meaning deferring a cheap high-profit pick can never help and greedily taking the max is optimal for that round.

## Complexity

- Time: O(n log n + k log n) — sorting once, then each of the n pushes and up to k pops costs O(log n).
- Space: O(n) — the capital ordering and the profit heap.
