Checking "does the stream end with any word" is the mirror image of "does the stream start with any word" — so reverse every dictionary word before inserting it into a trie. Then, to answer a query, walk that trie backwards from the newest letter toward older ones; a full path to a marked node means some word matches the current suffix.

Only the longest word's length worth of history can ever matter, so a fixed-size circular buffer replaces the unbounded stream from the brute-force version — memory per query stays bounded no matter how long the stream runs.

```java
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class StreamChecker {
    private static class Node {
        Map<Character, Node> children = new HashMap<>();
        boolean isWord = false;
    }

    private final Node root = new Node();
    private final Deque<Character> buffer = new ArrayDeque<>();
    private int maxLen = 0;

    public StreamChecker(List<String> words) {
        for (String word : words) {
            Node node = root;
            for (int i = word.length() - 1; i >= 0; i--) {
                node = node.children.computeIfAbsent(word.charAt(i), c -> new Node());
            }
            node.isWord = true;
            maxLen = Math.max(maxLen, word.length());
        }
    }

    public boolean query(char letter) {
        buffer.addLast(letter);
        if (buffer.size() > maxLen) buffer.removeFirst();

        Node node = root;
        for (Character ch : (Iterable<Character>) buffer::descendingIterator) {
            if (node.isWord) return true;
            node = node.children.get(ch);
            if (node == null) return false;
        }
        return node.isWord;
    }
}
```

## Why it works

Reversing every word before insertion turns "ends with word" into "starts with reversed word", which a trie answers naturally by walking from the root. Traversing the buffer newest-letter-first (via `descendingIterator`) retraces that reversed path; hitting `isWord` at any point means the letters consumed so far — read backwards, i.e. the actual suffix — spell a dictionary word. The buffer only needs to hold `maxLen` letters because no word longer than that could ever match.

## Complexity

- Time: O(L) per query, where L is the longest word length — the trie walk stops as soon as it runs out of buffer or matching edges. Building the trie is O(W * L) once.
- Space: O(W * L) for the trie plus O(L) for the buffer.
