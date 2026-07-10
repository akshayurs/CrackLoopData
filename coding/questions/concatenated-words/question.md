You are given an array of unique lowercase words. Call a word "concatenated" if it can be built by joining two or more *other* words from the same array end-to-end, in order (a shorter word may be reused more than once inside the join). Return every concatenated word from the array, sorted alphabetically.

## Examples

```text
Input:  words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
Output: ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
# catsdogcats = cats + dog + cats
# dogcatsdog  = dog + cats + dog
# ratcatdogcat = rat + cat + dog + cat
```

```text
Input:  words = ["cat", "dog", "catdog"]
Output: ["catdog"]        # catdog = cat + dog
```

```text
Input:  words = ["a", "ab", "abc"]
Output: []                # no word can be rebuilt from two or more of the others
```

## Constraints

- 1 <= words.length <= 10^4
- 1 <= words[i].length <= 30
- words[i] consists of lowercase English letters only.
- All words are distinct.

## Follow-up

Can you avoid re-hashing substrings on every split check by walking the words character-by-character through a shared trie instead?
