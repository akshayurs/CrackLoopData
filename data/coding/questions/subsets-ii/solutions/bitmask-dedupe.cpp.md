Sort the array first so equal values sit next to each other and every subset comes out in ascending order. There are `2^n` possible subsets, so walk every integer mask from `0` to `2^n - 1`, treat each bit as "include this index," and build the subset that mask describes.

Duplicate values in `nums` mean different masks can build the exact same subset. Insert each subset into a `set<vector<int>>`, which both deduplicates and keeps everything in lexicographic (element-by-element, tuple-style) order for free.

```cpp
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int> sorted = nums;
        sort(sorted.begin(), sorted.end());
        int n = (int)sorted.size();
        set<vector<int>> unique;
        for (int mask = 0; mask < (1 << n); mask++) {
            vector<int> subset;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) subset.push_back(sorted[i]);
            }
            unique.insert(subset);
        }
        return vector<vector<int>>(unique.begin(), unique.end());
    }
};
```

## Why it works

Every mask from `0` to `2^n - 1` corresponds to exactly one way of including/excluding each index, so the loop enumerates every possible subset at least once. Because `sorted` is pre-sorted, two masks that pick the same multiset of values always build the identical vector, so the `set` collapses them. `set<vector<int>>` orders elements with `operator<` on `vector`, which compares element by element and treats a shorter, matching prefix as smaller — exactly the canonical order the examples use, with no extra sort needed.

## Complexity

- Time: O(n · 2^n · log(2^n)) — 2^n masks, each O(n) to build, plus set insertion cost.
- Space: O(n · 2^n) — up to 2^n subsets stored before deduping.
