Matching brackets is a last-in-first-out job: the bracket you must close next is always the one you opened most recently. That is exactly what a stack tracks. Push every opening bracket; when a closing bracket arrives, the top of the stack must be its partner — otherwise the string is invalid.

Map each closing bracket to the opener it expects so the check is a single comparison. If the stack is empty when a closer appears, there is nothing to match; if the stack is non-empty at the end, some opener was never closed.

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (ch == '(') stack.push(')');
            else if (ch == '[') stack.push(']');
            else if (ch == '{') stack.push('}');
            else if (stack.isEmpty() || stack.pop() != ch) return false;
        }
        return stack.isEmpty();
    }
}
```

## Why it works

For each opener we push the closer we expect to see next, so a closing bracket is valid only when it equals the top of the stack. That single comparison enforces both correct type and correct nesting order. A closer with an empty stack is an unmatched close, and a non-empty stack at the end is an unmatched open — both rejected.

## Complexity

- Time: O(n) — one pass over the string, O(1) work per character.
- Space: O(n) — the stack can hold up to n expected closers.
