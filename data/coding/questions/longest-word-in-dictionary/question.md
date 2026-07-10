You are given an array of lowercase words. Call a word **buildable** if you can type it out one letter at a time such that every prefix you pass through along the way — including the finished word itself, but not counting the empty string — also appears somewhere in the array. Return the longest buildable word. If two or more buildable words tie for the longest length, return the lexicographically smallest of them. If no word is buildable, return an empty string.

## Examples

```text
Input:  words = ["w", "wo", "wor", "worl", "world"]
Output: "world"        # each prefix w, wo, wor, worl is also in the array
```

```text
Input:  words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"        # "apply" and "apple" are both buildable and length 5; "apple" sorts first
```

```text
Input:  words = ["abc", "bc", "ab", "a"]
Output: "abc"          # "bc" is stuck — "b" alone is missing, so it can never be built
```

## Constraints

- 1 <= words.length <= 1000
- 1 <= words[i].length <= 30
- words[i] consists only of lowercase English letters.
- All words are distinct.
