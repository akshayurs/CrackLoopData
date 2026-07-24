The plainest way to answer "which value repeats and which is gone" is to interrogate every candidate. For each number `v` from `1` to `n`, count how many times it appears in the array: a count of `2` marks the duplicate, a count of `0` marks the missing value.

No extra structures, just a scan per candidate. It is the honest baseline you would state before reaching for something faster.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = (int)nums.size();
        int duplicated = -1, missing = -1;
        for (int v = 1; v <= n; v++) {
            int count = 0;
            for (int x : nums) {
                if (x == v) count++;
            }
            if (count == 2) duplicated = v;
            else if (count == 0) missing = v;
        }
        return {duplicated, missing};
    }
};
```

## Why it works

Every value in a healthy set `1..n` appears exactly once. The corruption changes exactly two of those counts: the duplicate rises to `2` and the missing one drops to `0`. Counting each candidate's occurrences surfaces both anomalies directly, and every other value keeps its count of `1` and is ignored.

## Complexity

- Time: O(n²) — for each of the n candidates we rescan all n elements.
- Space: O(1) — only a running count and two answer slots.
</content>
