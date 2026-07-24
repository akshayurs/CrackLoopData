The same idea in C++: keep every price seen so far in a vector, and on each call walk backwards from the newest entry, counting days whose price is `<= today` until a strictly larger price breaks the streak.

```cpp
#include <vector>
using namespace std;

class StockSpanner {
public:
    vector<int> prices;

    int next(int price) {
        prices.push_back(price);
        int span = 0;
        int i = (int)prices.size() - 1;
        while (i >= 0 && prices[i] <= price) {
            span++;
            i--;
        }
        return span;
    }
};
```

## Why it works

After pushing, the last index is today. The loop walks leftward while each price is `<= price`, incrementing `span` once per qualifying day, and stops the moment a larger price appears or the vector is exhausted. That stopping point marks exactly where the consecutive run ends, so `span` counts every day in the run including today.

## Complexity

- Time: O(n) per `next` — worst case rescans the whole history; O(n²) over n calls.
- Space: O(n) — every price is stored.
