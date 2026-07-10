Given a string `s`, return the length of the longest contiguous substring that contains no repeated characters.

A substring is a run of consecutive characters from `s`. Two characters count as repeated only if they are exactly equal, so casing and whitespace matter.

## Examples

```text
Input:  s = "abcabcbb"
Output: 3        # "abc" is the longest window with all-unique characters
```

```text
Input:  s = "bbbbb"
Output: 1        # every window longer than "b" repeats a character
```

```text
Input:  s = "pwwkew"
Output: 3        # "wke" wins; "pwke" is not a substring because it skips a 'w'
```

## Constraints

- 0 <= s.length <= 5 * 10^4
- `s` consists of English letters, digits, symbols, and spaces.

## Follow-up

Can you do it in a single pass over `s`, in O(n) time?
