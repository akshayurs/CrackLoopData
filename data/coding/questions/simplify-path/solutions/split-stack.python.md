The path is a sequence of components separated by slashes, so split on `/` and process each component in order. A stack mirrors the directory hierarchy: pushing a real name descends into it, and hitting `..` pops the most recent name to climb back to the parent.

Empty strings (from `//` or a trailing slash) and `.` carry no meaning, so skip them. When `..` appears with an empty stack you are already at the root and simply stay there. Joining what remains with single slashes yields the canonical path.

```python
def simplify_path(path):
    stack = []
    for part in path.split('/'):
        if part == '' or part == '.':
            continue
        if part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack)
```

## Why it works

The stack always holds the surviving directory names in top-to-bottom order. A normal name is pushed; `..` cancels the deepest name it can find, exactly matching "go to parent"; `.` and empty tokens are noise and dropped. Because `..` on an empty stack is ignored, the result can never rise above root. Prefixing a single `/` and joining reconstructs the absolute path, and an empty stack degrades to just `"/"`.

## Complexity

- Time: O(n) — one split plus one pass over the components.
- Space: O(n) — the stack and split list hold up to n characters.
