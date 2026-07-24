Design a class that watches a live feed of lowercase letters arriving one at a time and, after every new letter, reports whether the letters seen **so far** end with any word from a fixed dictionary.

Implement `StreamChecker`:

- `StreamChecker(words)` — initializes the object with the dictionary of words.
- `query(letter)` — appends `letter` to the stream and returns `true` if some suffix of the stream (read left to right, most recent letter last) exactly equals one of the dictionary words, otherwise `false`.

The stream only grows — letters are never removed — and `query` may be called tens of thousands of times, so each call must be fast regardless of how long the stream has become.

## Examples

```text
Input:
  words  = ["cd", "f", "kl"]
  stream = "abcdefghijkl"   # one query() call per character, in order

Output: [false, false, false, true, false, true, false, false, false, false, false, true]
# after 'd' -> "...cd" ends with "cd"        -> true
# after 'f' -> "...def" ends with "f"        -> true
# after 'l' -> "...kl" ends with "kl"        -> true
```

```text
Input:
  words  = ["ab", "ba"]
  stream = "aabb"

Output: [false, false, true, false]
# after "a"    -> no suffix matches
# after "aa"   -> no suffix matches
# after "aab"  -> ends with "ab" -> true
# after "aabb" -> ends with "bb", not "ab" or "ba" -> false
```

```text
Input:
  words  = ["a"]
  stream = "a"

Output: [true]
```

## Constraints

- 1 <= words.length <= 2000
- 1 <= words[i].length <= 200
- words[i] consists of lowercase English letters only.
- letter passed to query is a single lowercase English letter.
- At most 4 * 10^4 total calls to query.
