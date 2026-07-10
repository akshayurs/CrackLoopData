Design a dictionary of words that supports adding new words and searching for a word, where the search can include the wildcard character `.` to mean "any single letter." Implement the `WordDictionary` class:

- `WordDictionary()` initializes an empty dictionary.
- `void addWord(String word)` adds `word` to the dictionary.
- `boolean search(String word)` returns `true` if there is any previously added word that matches `word`, where `.` in `word` may stand in for any one letter, and `false` otherwise.

## Examples

```text
Input:
  addWord("bad")
  addWord("dad")
  addWord("mad")
  search("pad")   -> false
  search("bad")   -> true
  search(".ad")   -> true
  search("b..")   -> true
```

```text
Input:
  addWord("a")
  search(".")     -> true
  search("aa")    -> false
  addWord("aa")
  search("aa")    -> true
```

```text
Input:
  addWord("at")
  addWord("and")
  search("a.")    -> true
  search("a..")   -> false   # no 3-letter word starts with "a"
  search("...")   -> true    # matches "and"
```

## Constraints

- 1 <= word.length <= 25
- `word` in `addWord` consists of lowercase English letters only.
- `word` in `search` consists of `'.'` or lowercase English letters.
- At most 2 dots appear in any single `search` call.
- At most 10^4 calls are made in total to `addWord` and `search`.
