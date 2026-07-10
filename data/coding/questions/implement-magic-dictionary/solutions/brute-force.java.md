The simplest reading of the rule "changing exactly one character" is to just check it directly against every stored word: same length, and exactly one position differs. No trie, no preprocessing beyond keeping the list around.

It is the honest baseline you would state first in an interview before reaching for a trie.

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class MagicDictionary {
    private List<String> words = new ArrayList<>();

    public MagicDictionary() {}

    public void buildDict(String[] dictionary) {
        words = Arrays.asList(dictionary);
    }

    public boolean search(String searchWord) {
        for (String candidate : words) {
            if (candidate.length() != searchWord.length()) continue;
            int diff = 0;
            for (int i = 0; i < searchWord.length(); i++) {
                if (candidate.charAt(i) != searchWord.charAt(i)) diff++;
            }
            if (diff == 1) return true;
        }
        return false;
    }
}
```

## Why it works

`buildDict` just remembers the words. `search` scans every stored word, skips any whose length doesn't match (a length mismatch can never be a one-letter substitution), and counts differing positions. A candidate qualifies only if exactly one position differs — zero differences means the words are identical, not a genuine change.

## Complexity

- Time: O(N·L) — each search compares against up to N stored words of length up to L.
- Space: O(N·L) — storing all the words.
