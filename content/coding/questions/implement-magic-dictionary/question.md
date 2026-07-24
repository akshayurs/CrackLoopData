Design a data structure that supports building a dictionary from a list of words and then checking whether a query word can be turned into some word already in the dictionary by changing **exactly one** letter (to a different letter — the result must still be a real word already in the dictionary, and the query must be the same length as it).

Implement the class `MagicDictionary`:

- `MagicDictionary()` initializes the object.
- `buildDict(words)` builds the dictionary from an array of distinct lowercase words. This is called exactly once, before any `search` call.
- `search(word)` returns `true` if changing exactly one character of `word` produces a word that exists in the dictionary, and `false` otherwise.

## Examples

```text
Input:
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]

Output:
[null, null, false, true, false, false]

# hello -> already in the dictionary, but 0 letters change -> false
# hhllo -> change index 1 'h'->'e' to get "hello"       -> true
# hell  -> length 4, no dictionary word has length 4     -> false
# leetcoded -> length 9, no dictionary word has length 9 -> false
```

```text
Input:
["MagicDictionary", "buildDict", "search", "search"]
[[], [["a", "b"]], ["a"], ["b"]]

Output:
[null, null, true, true]

# "a" -> change its only letter to get "b" -> true
# "b" -> change its only letter to get "a" -> true
```

## Constraints

- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of lowercase English letters only.
- All words in `words` are distinct.
- 1 <= word.length <= 100
- word consists of lowercase English letters only.
- buildDict is called exactly once before search is called.
- At most 100 calls to search.
