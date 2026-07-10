The same idea in C++: keep the stones in a `vector<int>` and sort it before every smash so the two heaviest values land at the back. Pop them off, and if a remainder is left, push it back for the next round.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        vector<int> arr(stones);
        while (arr.size() > 1) {
            sort(arr.begin(), arr.end());
            int heaviest = arr.back(); arr.pop_back();
            int second = arr.back(); arr.pop_back();
            if (heaviest != second) {
                arr.push_back(heaviest - second);
            }
        }
        return arr.empty() ? 0 : arr[0];
    }
};
```

## Why it works

Sorting ascending before each round moves the two largest weights to the end of the vector, so the two pops always take the current two heaviest stones. Pushing back the difference (when the stones aren't equal) keeps the invariant true for the next pass. The loop ends with at most one stone, which is the answer.

## Complexity

- Time: O(n² log n) — up to n rounds, each paying O(n log n) to re-sort.
- Space: O(n) — the working vector of stones.
