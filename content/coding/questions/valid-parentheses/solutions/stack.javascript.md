Matching brackets is a last-in-first-out job: the bracket you must close next is always the one you opened most recently. That is exactly what a stack tracks. Push every opening bracket; when a closing bracket arrives, the top of the stack must be its partner — otherwise the string is invalid.

Map each closing bracket to the opener it expects so the check is a single comparison. If the stack is empty when a closer appears, there is nothing to match; if the stack is non-empty at the end, some opener was never closed.

```javascript
function isValid(s) {
  const pairs = { ')': '(', ']': '[', '}': '{' };
  const stack = [];
  for (const ch of s) {
    if (ch in pairs) {
      if (stack.pop() !== pairs[ch]) {
        return false;
      }
    } else {
      stack.push(ch);
    }
  }
  return stack.length === 0;
}
```

## Why it works

Each opener is pushed and waits for its closer. When a closer arrives, the only bracket that can legally precede it is the matching opener on top; popping enforces both the correct type and the correct nesting order in one step. Popping an empty stack yields `undefined`, which never equals a real opener, so an unmatched close is rejected; a non-empty stack at the end means an unmatched open.

## Complexity

- Time: O(n) — one pass over the string, O(1) work per character.
- Space: O(n) — the stack can hold up to n opening brackets.
