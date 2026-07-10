The path is a sequence of components separated by slashes, so split on `/` and process each component in order. A deque used as a stack mirrors the directory hierarchy: pushing a real name descends into it, and hitting `..` pops the most recent name to climb back to the parent.

Empty strings (from `//` or a trailing slash) and `.` carry no meaning, so skip them. When `..` appears with an empty stack you are already at the root and simply stay there. Joining what remains with single slashes yields the canonical path.

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public String simplifyPath(String path) {
        Deque<String> stack = new ArrayDeque<>();
        for (String part : path.split("/")) {
            if (part.isEmpty() || part.equals(".")) continue;
            if (part.equals("..")) {
                if (!stack.isEmpty()) stack.pollLast();
            } else {
                stack.offerLast(part);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (String dir : stack) sb.append('/').append(dir);
        return sb.length() == 0 ? "/" : sb.toString();
    }
}
```

## Why it works

The deque always holds the surviving directory names in first-to-last order. A normal name is appended; `..` removes the deepest name it can find, exactly matching "go to parent"; `.` and empty tokens are noise and dropped. Because `..` on an empty deque is ignored, the result can never rise above root. Rebuilding with a leading `/` before each name reconstructs the absolute path, and an empty deque degrades to just `"/"`.

## Complexity

- Time: O(n) — one split plus one pass over the components.
- Space: O(n) — the deque and split array hold up to n characters.
