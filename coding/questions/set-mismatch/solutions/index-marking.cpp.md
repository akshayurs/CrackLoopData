The values themselves are indices in disguise: value `v` corresponds to slot `v - 1`. So we can use the array as its own bookkeeping. Walk each element, jump to the slot its value points at, and flip that slot's sign to mark "this value has been seen". If the slot is already negative, the value that led us there is the duplicate.

After the marking pass, every value that truly appeared has left exactly one negative mark — so the one slot that is still positive names the value that never showed up. This needs only the array we were given plus a couple of variables, satisfying the O(1) extra-space follow-up.

```cpp
#include <vector>
#include <cstdlib>
using namespace std;

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int duplicated = -1;
        for (int x : nums) {
            int idx = abs(x) - 1;
            if (nums[idx] < 0) duplicated = abs(x);
            else nums[idx] = -nums[idx];
        }
        int missing = -1;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (nums[i] > 0) missing = i + 1;
        }
        return {duplicated, missing};
    }
};
```

## Why it works

Reading `abs(x)` shields us from signs we flipped earlier, so each original value is honored exactly once. Slot `abs(x) - 1` acts as a "seen" flag for that value; the second time the duplicate arrives, its flag is already negative and we catch it. Every value present flips its slot negative, so the lone slot left positive is the one whose value never appeared — that index plus one is the missing number.

## Complexity

- Time: O(n) — one pass to mark, one pass to locate the positive slot.
- Space: O(1) — signs are stored inside the input array; no auxiliary structure.
</content>
