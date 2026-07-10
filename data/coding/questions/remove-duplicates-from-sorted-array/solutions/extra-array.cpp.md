The most direct reading of the problem: collect the distinct values, then write them back to the front of the array. Because the input is sorted, a value is new exactly when it differs from the last value you kept, so a single scan builds the unique list.

Copy those values back over the first slots of `nums` and return the count. It costs a second vector, but it maps cleanly onto the problem statement.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> unique;
        for (int n : nums) {
            if (unique.empty() || unique.back() != n) {
                unique.push_back(n);
            }
        }
        for (int i = 0; i < (int)unique.size(); i++) {
            nums[i] = unique[i];
        }
        return (int)unique.size();
    }
};
```

## Why it works

Duplicates in a sorted array are always adjacent, so comparing each element to the last one pushed is enough to filter repeats — `unique` ends up holding every distinct value in its original order. Writing those values back over `nums[0..k)` leaves the front of the array in the required state, and `k` is simply the count of distinct values.

## Complexity

- Time: O(n) — one pass to build the vector, one pass to copy it back.
- Space: O(n) — the auxiliary vector can hold up to n values.
