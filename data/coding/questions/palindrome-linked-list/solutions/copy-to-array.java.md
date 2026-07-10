The simplest way to check for a palindrome is the way you'd check it on paper: write down the sequence, then compare it to its own reverse. Walk the list once, copying each `val` into a plain list.

Once the values sit in a list, the two-pointer palindrome check is trivial — compare the first and last, then step inward.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public boolean isPalindrome(ListNode head) {
        List<Integer> values = new ArrayList<>();
        ListNode node = head;
        while (node != null) {
            values.add(node.val);
            node = node.next;
        }
        int i = 0, j = values.size() - 1;
        while (i < j) {
            if (!values.get(i).equals(values.get(j))) return false;
            i++;
            j--;
        }
        return true;
    }
}
```

## Why it works

The list preserves the exact order the values appeared in the linked list. Walking two pointers inward from both ends compares every value at position `i` against its mirrored position; if any pair disagrees, the sequence cannot be a palindrome, and if the pointers cross without a mismatch, every pair agreed.

## Complexity

- Time: O(n) — one pass to copy, one pass to compare.
- Space: O(n) — the list holds all n values.
