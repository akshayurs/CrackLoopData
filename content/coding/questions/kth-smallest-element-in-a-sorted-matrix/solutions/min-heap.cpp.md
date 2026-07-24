Each row is already sorted, so the matrix is really `n` sorted lists to merge. This is the classic k-way merge: a min-heap holds the current front of each row, and popping the smallest `k` times reaches the answer without touching most of the matrix.

A `priority_queue` of `[value, row, col]` tuples, ordered as a min-heap via `greater<>`, does the work. Seed it with the first cell of each row; each time you pop a cell, push the cell to its right.

```cpp
#include <vector>
#include <queue>
#include <array>
using namespace std;

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        priority_queue<array<int, 3>, vector<array<int, 3>>, greater<>> heap;
        for (int r = 0; r < n; r++) {
            heap.push({matrix[r][0], r, 0});
        }
        int value = 0;
        for (int i = 0; i < k; i++) {
            auto cell = heap.top();
            heap.pop();
            value = cell[0];
            int r = cell[1], c = cell[2];
            if (c + 1 < n) {
                heap.push({matrix[r][c + 1], r, c + 1});
            }
        }
        return value;
    }
};
```

## Why it works

The min-heap always exposes the smallest value among the row fronts, so popping repeatedly produces values in global ascending order. Pushing the next cell of a popped row keeps every row represented, so after `k` pops the last value removed is exactly the `k`th smallest — equal values are separate entries, so duplicates count correctly.

## Complexity

- Time: O(k log n) — k pops, each a log-n heap operation; the heap never exceeds n entries.
- Space: O(n) — one entry per row.
