Splitting first builds an intermediate array of every component. You can skip that allocation by scanning the string once, accumulating characters into a `StringBuilder` token and finalizing it each time you hit a slash. Treating the index just past the end as a virtual `/` flushes the last token without a special case.

The stack logic is identical to the split version — the only change is that tokens are produced on the fly instead of up front, which keeps peak extra memory to the deque alone.

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public String simplifyPath(String path) {
        Deque<String> stack = new ArrayDeque<>();
        StringBuilder token = new StringBuilder();
        for (int i = 0; i <= path.length(); i++) {
            char ch = i < path.length() ? path.charAt(i) : '/';
            if (ch == '/') {
                String part = token.toString();
                token.setLength(0);
                if (part.isEmpty() || part.equals(".")) continue;
                if (part.equals("..")) {
                    if (!stack.isEmpty()) stack.pollLast();
                } else {
                    stack.offerLast(part);
                }
            } else {
                token.append(ch);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (String dir : stack) sb.append('/').append(dir);
        return sb.length() == 0 ? "/" : sb.toString();
    }
}
```

## Why it works

Each character is either part of a name or a boundary. On a boundary the completed token is classified: empty and `.` are dropped, `..` pops the parent when one exists, anything else is a real directory that gets pushed. Running the index one past the end supplies a final virtual slash so the last segment is processed. Ignoring `..` on an empty deque prevents rising above root, and rebuilding under a leading `/` yields the canonical path.

## Complexity

- Time: O(n) — every character is visited once.
- Space: O(n) — the deque holds up to n characters; no split array is built.
