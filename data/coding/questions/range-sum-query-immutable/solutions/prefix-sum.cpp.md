Because the array never changes, do the summing work once up front. Build a `prefix` vector where `prefix[i]` holds the sum of the first `i` elements. Then the sum of any window `[left, right]` is just `prefix[right + 1] - prefix[left]` — one subtraction, no scanning.

The extra offset (a leading zero at `prefix[0]`) is what lets the formula handle `left = 0` without a special case.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> rangeSum(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> prefix(nums.size() + 1, 0);
        for (size_t i = 0; i < nums.size(); i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        vector<int> answers;
        for (auto& q : queries) {
            answers.push_back(prefix[q[1] + 1] - prefix[q[0]]);
        }
        return answers;
    }
};
```

## Why it works

`prefix[i]` equals `nums[0] + ... + nums[i-1]`. Subtracting the sum up to `left` from the sum up to `right + 1` cancels everything before `left` and keeps exactly `nums[left..right]`. The leading zero makes `prefix[left]` well defined even when `left` is 0. Preprocessing is a single pass; every query is then constant work.

## Complexity

- Time: O(n + q) — one pass to build the prefix vector, then O(1) per query.
- Space: O(n) — the prefix vector holds n + 1 sums.
