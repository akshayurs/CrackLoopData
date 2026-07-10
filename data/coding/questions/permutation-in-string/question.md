You are given two strings `s1` and `s2`. Return `true` if `s2` contains a permutation of `s1` as a contiguous substring, and `false` otherwise.

In other words, one of `s1`'s rearrangements must appear as a block of adjacent characters somewhere inside `s2`.

## Examples

```text
Input:  s1 = "ab", s2 = "eidbaooo"
Output: true          # s2 contains "ba", a permutation of "ab"
```

```text
Input:  s1 = "ab", s2 = "eidboaoo"
Output: false         # no window of s2 is a rearrangement of "ab"
```

```text
Input:  s1 = "adc", s2 = "dcda"
Output: true          # s2 contains "dcd"... "cda" is a permutation of "adc"
```

## Constraints

- 1 <= s1.length, s2.length <= 10^4
- `s1` and `s2` consist of lowercase English letters.

## Follow-up

Can you avoid re-scanning each window from scratch and keep the whole check to a single pass over `s2`?
