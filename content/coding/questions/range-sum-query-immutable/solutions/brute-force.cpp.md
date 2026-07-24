The literal reading of the problem: for each query, walk from `left` to `right` and add up the elements. No preprocessing, no extra memory beyond the answer vector.

This is the honest baseline. It is fine when there are only a handful of queries, but it re-scans the array from scratch every time, so heavy querying makes it slow.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> rangeSum(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> answers;
        for (auto& q : queries) {
            int total = 0;
            for (int i = q[0]; i <= q[1]; i++) {
                total += nums[i];
            }
            answers.push_back(total);
        }
        return answers;
    }
};
```

## Why it works

Each query independently sums the contiguous slice `nums[left..right]`. The inner loop uses `i <= right` so the last element is included. Nothing is cached between queries, so correctness is obvious — we add exactly the elements the query asks for.

## Complexity

- Time: O(q · n) — each of the `q` queries may scan up to `n` elements.
- Space: O(1) — ignoring the output vector, only a running total is kept.
