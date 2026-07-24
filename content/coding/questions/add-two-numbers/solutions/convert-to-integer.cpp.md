The simplest reading of the problem: rebuild the actual numbers the two lists represent, add them with ordinary arithmetic, then chop the result back into digit nodes. Since the lists store digits ones-first, reversing the digit string before adding gives the true number. C++ has no built-in arbitrary-precision integer, so the addition itself is done digit-by-digit over the reconstructed decimal strings.

This still sidesteps any carry bookkeeping tied to the *linked-list* structure — the strings are added independently of how the lists are shaped — at the cost of materializing the whole number twice as text.

```cpp
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        string sum = addStrings(toDigits(l1), toDigits(l2));
        ListNode dummy(0);
        ListNode* tail = &dummy;
        for (int i = (int)sum.size() - 1; i >= 0; i--) {
            tail->next = new ListNode(sum[i] - '0');
            tail = tail->next;
        }
        return dummy.next;
    }

private:
    string toDigits(ListNode* node) {
        string digits;
        while (node != nullptr) {
            digits.push_back(char('0' + node->val));
            node = node->next;
        }
        reverse(digits.begin(), digits.end());
        return digits;
    }

    string addStrings(const string& a, const string& b) {
        string result;
        int i = (int)a.size() - 1, j = (int)b.size() - 1, carry = 0;
        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;
            if (i >= 0) sum += a[i--] - '0';
            if (j >= 0) sum += b[j--] - '0';
            result.push_back(char('0' + sum % 10));
            carry = sum / 10;
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
```

## Why it works

`toDigits` walks a list front-to-back, collecting digits in ones-first order, then reverses them into most-significant-first order — exactly reconstructing the decimal string each list encodes. `addStrings` performs textbook long addition from the last character of each string toward the front, carrying into the next column exactly as on paper, so it produces the correct sum regardless of how many digits either number has. Reversing that sum back to ones-first order gives the digits the output list needs.

## Complexity

- Time: O(m + n) — building both digit strings and adding them are each linear passes.
- Space: O(m + n) — the digit strings and the sum string hold as many characters as there are input digits.
