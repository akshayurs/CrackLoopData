The simplest possible trie "implementation" doesn't build a tree at all — it just keeps every inserted word in a list. `search` checks for an exact match; `startsWith` checks whether any stored word begins with the prefix.

This is the honest baseline: correct, easy to write under pressure, but it re-scans everything stored so far on every query.

```java
import java.util.ArrayList;
import java.util.List;

class Trie {
    private List<String> words;

    public Trie() {
        words = new ArrayList<>();
    }

    public void insert(String word) {
        words.add(word);
    }

    public boolean search(String word) {
        return words.contains(word);
    }

    public boolean startsWith(String prefix) {
        for (String w : words) {
            if (w.startsWith(prefix)) {
                return true;
            }
        }
        return false;
    }
}
```

## Why it works

`words` is just a record of everything inserted, duplicates and all. `search` asks whether `word` appears verbatim in that record via `contains`. `startsWith` walks the record and returns as soon as one entry has `prefix` as its first characters. Nothing here depends on shared structure between words, so correctness is immediate, but so is the cost of re-checking every stored word on every call.

## Complexity

- Time: O(L) for `insert`; O(n * L) for `search` and `startsWith`, where n is the number of inserted words and L is the average word length.
- Space: O(n * L) to store every inserted word.
