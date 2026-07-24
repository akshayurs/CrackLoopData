Given an array of strings `words` and an integer `k`, return the `k` most frequent strings.

Sort the result by frequency from highest to lowest. If two words occur the same number of times, break the tie alphabetically — the lexicographically smaller word comes first.

## Examples

```text
Input:  words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]        # "i" and "love" both appear twice; "code" and "leetcode" trail at one each
```

```text
Input:  words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]        # counts: the=4, is=3, sunny=2, day=1
```

```text
Input:  words = ["a", "aa", "aaa"], k = 1
Output: ["a"]        # all three occur once; "a" wins the alphabetical tie-break
```

## Constraints

- 1 <= words.length <= 500
- 1 <= words[i].length <= 10
- `words[i]` consists of lowercase English letters only.
- `k` is between 1 and the number of distinct words in `words`.
- Answer is uniquely determined once ties are broken alphabetically.

## Follow-up

Can you avoid a full O(n log n) sort and get the answer in O(n + k log n) instead?
