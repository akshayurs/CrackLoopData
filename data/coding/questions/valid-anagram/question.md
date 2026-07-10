Given two strings `s` and `t`, decide whether `t` is an anagram of `s`. An anagram uses exactly the same letters as the original, just rearranged — so `t` must contain every character of `s` the same number of times, and nothing more.

Return `true` when `t` is an anagram of `s`, and `false` otherwise.

## Examples

```text
Input:  s = "listen", t = "silent"
Output: true          # same letters, reordered
```

```text
Input:  s = "rat", t = "car"
Output: false         # 'r','a','t' vs 'c','a','r' — different letters
```

```text
Input:  s = "anagram", t = "nagaram"
Output: true          # each letter appears the same number of times
```

## Constraints

- 1 <= s.length, t.length <= 5 * 10^4
- `s` and `t` consist of lowercase English letters.

## Follow-up

What if the strings could contain arbitrary Unicode characters? How would your solution adapt?
