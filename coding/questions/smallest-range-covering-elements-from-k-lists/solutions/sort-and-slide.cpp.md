Flatten the problem: tag every value with which list it came from, then sort all of those `(value, list)` pairs together. Any range that covers all `k` lists now corresponds to a contiguous window of this sorted sequence that contains every list tag at least once — a classic "smallest window with all tags" sliding-window problem.

Slide the window's right edge forward, and whenever all `k` tags are present, shrink from the left as far as possible while keeping that property, checking each valid window against the best range seen so far.

```cpp
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& lists) {
        vector<pair<int, int>> merged;
        for (int i = 0; i < (int)lists.size(); i++) {
            for (int value : lists[i]) merged.push_back({value, i});
        }
        sort(merged.begin(), merged.end());

        int k = (int)lists.size();
        unordered_map<int, int> count;
        int formed = 0, left = 0;
        vector<int> best = {merged.front().first, merged.back().first};

        for (int right = 0; right < (int)merged.size(); right++) {
            int tag = merged[right].second;
            if (++count[tag] == 1) formed++;

            while (formed == k) {
                int lo = merged[left].first;
                int hi = merged[right].first;
                if (hi - lo < best[1] - best[0]) best = {lo, hi};
                int leftTag = merged[left].second;
                if (--count[leftTag] == 0) formed--;
                left++;
            }
        }
        return best;
    }
};
```

## Why it works

Sorting merges all `k` lists into one non-decreasing sequence while remembering each value's origin. A window covers every list exactly when its tags include all `k` list indices, so shrinking the window from the left while it stays valid finds the tightest such window. Because the sequence is sorted, the window's endpoints are the true `lo`/`hi` of the range, and the greedy shrink never skips a better answer.

## Complexity

- Time: O(N log N) — N is the total number of elements; dominated by the sort.
- Space: O(N) — the merged array and the tag-count map.
