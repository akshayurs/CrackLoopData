You are given a string `s` containing only the six bracket characters `()[]{}`. Determine whether the brackets are **properly balanced**.

A string is valid when every opening bracket is closed by a matching bracket of the same type, brackets close in the correct order (most-recently opened is closed first), and no bracket is left unmatched.

## Examples

```text
Input:  s = "()[]{}"
Output: true          # each pair opens and closes cleanly
```

```text
Input:  s = "(]"
Output: false         # ( is closed by the wrong bracket type
```

```text
Input:  s = "([)]"
Output: false         # ) closes before the inner ] — wrong order
```

## Constraints

- 1 <= s.length <= 10^4
- `s` consists only of the characters `'('`, `')'`, `'['`, `']'`, `'{'`, and `'}'`.

## Follow-up

Can you decide validity in a single left-to-right pass using O(n) time?
