The simplest way to check for a palindrome is the way you'd check it on paper: write down the sequence, then compare it to its own reverse. Walk the list once, copying each `val` into a plain vector.

Once the values sit in a vector, the two-pointer palindrome check is trivial — compare the first and last, then step inward.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        vector<int> values;
        for (ListNode* node = head; node != nullptr; node = node->next) {
            values.push_back(node->val);
        }
        int i = 0, j = (int)values.size() - 1;
        while (i < j) {
            if (values[i] != values[j]) return false;
            i++;
            j--;
        }
        return true;
    }
};
```

## Why it works

The vector preserves the exact order the values appeared in the linked list. Walking two pointers inward from both ends compares every value at position `i` against its mirrored position; if any pair disagrees, the sequence cannot be a palindrome, and if the pointers cross without a mismatch, every pair agreed.

## Complexity

- Time: O(n) — one pass to copy, one pass to compare.
- Space: O(n) — the vector holds all n values.
