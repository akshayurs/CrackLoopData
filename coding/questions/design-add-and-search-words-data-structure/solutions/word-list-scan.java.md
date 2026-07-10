The simplest dictionary "implementation" doesn't build any tree at all — it just remembers every added word in a list. `addWord` is a single append. `search` compares the query against every stored word of the same length, treating each `.` as an automatic match for whatever letter sits in that position.

This is the honest baseline: correct and easy to write under pressure, but it re-scans everything stored so far on every query, and the comparison itself costs a full pass over the word.

```java
import java.util.ArrayList;
import java.util.List;

class WordDictionary {
    private List<String> words;

    public WordDictionary() {
        words = new ArrayList<>();
    }

    public void addWord(String word) {
        words.add(word);
    }

    public boolean search(String word) {
        for (String w : words) {
            if (w.length() != word.length()) continue;
            boolean match = true;
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                if (c != '.' && c != w.charAt(i)) {
                    match = false;
                    break;
                }
            }
            if (match) return true;
        }
        return false;
    }
}
```

## Why it works

`words` records everything added, duplicates included. For a query to match a stored word they must first be the same length, since `.` stands for exactly one letter, never zero or many. The inner loop walks both strings position by position, and a mismatch only counts when the query character is a concrete letter that differs from the stored one — a `.` always passes. The first stored word that survives the whole walk makes `search` return `true` immediately.

## Complexity

- Time: O(1) for `addWord`; O(n * L) for `search`, where n is the number of stored words and L is the word length.
- Space: O(n * L) to store every added word.
