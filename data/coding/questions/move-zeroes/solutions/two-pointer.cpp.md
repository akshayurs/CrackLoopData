Do it in place with two indices. Keep a slow pointer `insert` marking where the next non-zero value belongs, and a fast pointer `i` scanning the vector. Every time the scan finds a non-zero, swap it into the `insert` slot and advance `insert`.

Because `insert` only moves when a non-zero is placed, everything at or past it is either about to be overwritten or already a zero — so the zeros naturally collect at the tail with no extra memory.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> moveZeroes(vector<int>& nums) {
        int insert = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (nums[i] != 0) {
                swap(nums[insert], nums[i]);
                insert++;
            }
        }
        return nums;
    }
};
```

## Why it works

`insert` counts how many non-zeros have been fixed in place. When `i` reaches a non-zero, swapping with position `insert` puts it right after the previously placed non-zero, preserving order. The value moved back to `i` is whatever was at `insert` — always a zero once `i` is past `insert`. After the loop, indices `[insert, n)` are all zeros.

## Complexity

- Time: O(n) — a single scan.
- Space: O(1) — swaps happen in the original vector.
