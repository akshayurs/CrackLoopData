Keep every letter the stream has produced in a growing buffer. On each `query`, walk the dictionary and test whether the buffer's tail matches that word exactly.

This is easy to write correctly first, then optimize once it's clear where the time goes.

```java
import java.util.List;

class StreamChecker {
    private final List<String> words;
    private final StringBuilder stream = new StringBuilder();

    public StreamChecker(List<String> words) {
        this.words = words;
    }

    public boolean query(char letter) {
        stream.append(letter);
        int len = stream.length();
        for (String word : words) {
            int n = word.length();
            if (n <= len && stream.substring(len - n).equals(word)) {
                return true;
            }
        }
        return false;
    }
}
```

## Why it works

`stream` holds the full history in order, so `stream.substring(len - n)` is exactly the last `n` letters seen — comparing it to `word` directly answers "does the stream end with this word?". Checking every word on every call is correct because there is no shortcut yet for skipping non-matching prefixes.

## Complexity

- Time: O(Q * W * L) — Q queries, each scanning W words of average length L to build and compare a substring.
- Space: O(Q + W * L) — the buffer grows with the stream; the dictionary is stored as given.
