You are given two strings `s` and `p`. Return the starting indices of every substring of `s` that is an anagram of `p` — that is, every window in `s` of length `|p|` that uses exactly the same letters as `p`, with the same counts.

Return the indices in ascending order.

## Examples

```text
Input:  s = "cbaebabacd", p = "abc"
Output: [0, 6]        # "cba" starts at 0, "bac" starts at 6
```

```text
Input:  s = "abab", p = "ab"
Output: [0, 1, 2]     # "ab", "ba", "ab" are all anagrams of "ab"
```

```text
Input:  s = "a", p = "aa"
Output: []            # p is longer than s, so no window can match
```

## Constraints

- 1 <= s.length, p.length <= 3 * 10^4
- `s` and `p` consist of lowercase English letters only.

## Follow-up

Each window differs from the previous one by just two characters. Can you avoid recounting the whole window every time and reach O(n)?
