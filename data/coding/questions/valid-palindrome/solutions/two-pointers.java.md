To avoid building a second string, compare the ends of the original directly. Keep one pointer at the far left and one at the far right, skip anything that is not alphanumeric, and match the two characters they land on. Walk both inward until they meet.

This is the two-pointer template: a single scan from both sides, with case folding applied only at the moment of comparison, using no extra storage beyond two indices.

```java
class Solution {
    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) left++;
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) right--;
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
```

## Why it works

A palindrome must have matching characters at mirrored positions. The inner loops advance past punctuation and spaces so the pointers always rest on the characters that actually count. If any mirrored pair disagrees after lowercasing, the string cannot be a palindrome and we return early. If the pointers cross without a mismatch, every meaningful pair matched.

## Complexity

- Time: O(n) — each pointer moves inward at most n steps total.
- Space: O(1) — only two indices, regardless of input size.
