You are given two strings `s` and `t`. Each string is being typed into a text editor where the character `#` means a backspace, deleting the character immediately before it. Return `true` if the two strings produce the same final text once all backspaces are applied, and `false` otherwise.

A backspace on an already-empty text does nothing.

## Examples

```text
Input:  s = "ab#c", t = "ad#c"
Output: true          # both become "ac"
```

```text
Input:  s = "ab##", t = "c#d#"
Output: true          # both become ""
```

```text
Input:  s = "a#c", t = "b"
Output: false         # "c" != "b"
```

## Constraints

- 1 <= s.length, t.length <= 200
- `s` and `t` contain only lowercase letters and `#` characters.

## Follow-up

Can you compare the strings in O(1) extra space, without building the results?
