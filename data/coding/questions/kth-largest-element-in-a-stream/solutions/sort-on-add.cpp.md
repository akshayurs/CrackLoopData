The simplest thing that could work: keep every number the stream has ever seen in a vector. Each time `add` is called, drop the new value in, sort the whole vector in descending order, and read off the element at index `k - 1`.

It never gets the ordering wrong, but re-sorting the entire history on every single call is wasteful once the stream grows long.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) : k(k), nums(nums) {}

    int add(int val) {
        nums.push_back(val);
        sort(nums.begin(), nums.end(), greater<int>());
        return nums[k - 1];
    }

private:
    int k;
    vector<int> nums;
};
```

## Why it works

Sorting the vector in descending order puts the largest value at index 0, the second largest at index 1, and so on — so the k-th largest always sits at index `k - 1`. Because we re-sort after every insertion, the answer reflects the full stream seen so far.

## Complexity

- Time: O(n log n) per call to `add`, where n is the number of elements seen so far.
- Space: O(n) — the vector stores every value ever added.
