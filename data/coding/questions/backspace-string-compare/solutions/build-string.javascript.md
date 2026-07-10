The most literal reading: actually type each string out. Walk left to right pushing letters onto a stack, and whenever a `#` appears, pop the last letter (if any). Whatever remains on the stack is the final text.

Do this for both strings and compare the results directly. It is the honest baseline you would describe first before worrying about extra space.

```javascript
function backspaceCompare(s, t) {
  const build = (str) => {
    const stack = [];
    for (const ch of str) {
      if (ch === '#') {
        if (stack.length) stack.pop();
      } else {
        stack.push(ch);
      }
    }
    return stack.join('');
  };

  return build(s) === build(t);
}
```

## Why it works

A stack mirrors the editor exactly: typing a letter pushes it, and a backspace removes the most recent letter — which is always the top of the stack. Guarding the pop with `stack.length` handles a backspace on empty text as a no-op. Two strings are equal after editing iff their reconstructed contents match character for character.

## Complexity

- Time: O(m + n) — each character of both strings is processed once.
- Space: O(m + n) — the two rebuilt strings are stored explicitly.
