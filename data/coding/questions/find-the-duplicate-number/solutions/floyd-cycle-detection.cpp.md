Treat each value as a pointer: from index `i`, "follow" to index `nums[i]`. Because every value is in `[1, n]` and there are `n + 1` slots, this function has no slot mapping to index `0`, but two different indices are forced to map to the same next index — exactly the setup for a cycle, and the node where two paths merge is the duplicated value. That turns the problem into "find the start of the cycle in a linked list," which Floyd's tortoise-and-hare solves in O(1) space.

First race a slow pointer (one step) against a fast pointer (two steps) until they meet inside the cycle. Then reset one pointer to the start and advance both one step at a time — they meet again exactly at the cycle's entrance, which is the duplicated value.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = nums[0];
        int fast = nums[0];
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
};
```

## Why it works

Reading `nums` as a function `f(i) = nums[i]` builds an implicit linked list starting at index `0`. Since a value repeats, at least two indices point into the same next index, guaranteeing a cycle — and the entrance to that cycle is the repeated value itself (it's the only value with two indices mapping to it). Floyd's algorithm finds a meeting point inside the cycle, then a second phase — restarting one pointer at the head and advancing both at equal speed — proves the two pointers meet exactly at the cycle's entrance, by the standard tortoise-and-hare distance argument.

## Complexity

- Time: O(n) — each phase visits at most a constant multiple of n nodes.
- Space: O(1) — only two pointers are used, and `nums` is never modified.
