Design a data structure that stores a set of strings and can quickly tell you whether a string was stored, or whether any stored string starts with a given prefix. This structure is called a **trie** (prefix tree).

Implement the `Trie` class:

- `Trie()` initializes an empty trie.
- `void insert(String word)` adds `word` to the trie.
- `boolean search(String word)` returns `true` if `word` was previously inserted, `false` otherwise.
- `boolean startsWith(String prefix)` returns `true` if any previously inserted word begins with `prefix`, `false` otherwise.

## Examples

```text
Input:
  insert("apple")
  search("apple")     -> true
  search("app")       -> false
  startsWith("app")   -> true
  insert("app")
  search("app")       -> true
```

```text
Input:
  insert("cat")
  insert("car")
  startsWith("ca")    -> true
  startsWith("cab")   -> false
  search("cat")       -> true
```

```text
Input:
  startsWith("a")     -> false   # nothing inserted yet
  insert("a")
  search("a")         -> true
  startsWith("a")     -> true
```

## Constraints

- 1 <= word.length, prefix.length <= 2000
- `word` and `prefix` consist only of lowercase English letters.
- At most 3 * 10^4 total calls will be made to `insert`, `search`, and `startsWith`.
