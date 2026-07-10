Trade memory for speed. Walk the vector once, and for each number ask whether the value that completes the pair has already been seen. An `unordered_map` answers that in O(1), removing the inner loop.

Record each value's index as you go, so the complement's later appearance yields both positions immediately.

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < (int)nums.size(); i++) {
            int complement = target - nums[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};
```

## Why it works

`seen` maps a value to the index where it appeared. For the current number, its partner must be `target - nums[i]`; if that partner is already a key, the pair is found. Inserting the current value only *after* the check prevents pairing an element with itself, and one pass suffices because a partner is always an earlier element.

## Complexity

- Time: O(n) — one pass; each `unordered_map` lookup and insert is O(1) on average.
- Space: O(n) — the map holds up to n entries.
