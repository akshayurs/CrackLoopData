Build the dictionary into a 26-way trie once instead of rescanning it for every word. Each root's final character marks its node as a root-end; resolving a word is then a single walk down the trie, stopping as soon as a root-end node is reached — that is always the shortest matching root.

Using a fixed-size `TrieNode[26]` array instead of a map keeps each step O(1) with no hashing overhead.

```java
import java.util.List;

class Solution {
    static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isRootEnd = false;
    }

    public String replaceWords(List<String> dictionary, String sentence) {
        TrieNode trieRoot = new TrieNode();
        for (String root : dictionary) {
            TrieNode node = trieRoot;
            for (char ch : root.toCharArray()) {
                int idx = ch - 'a';
                if (node.children[idx] == null) node.children[idx] = new TrieNode();
                node = node.children[idx];
            }
            node.isRootEnd = true;
        }

        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();
        for (int w = 0; w < words.length; w++) {
            if (w > 0) result.append(" ");
            result.append(shortestRoot(trieRoot, words[w]));
        }
        return result.toString();
    }

    private String shortestRoot(TrieNode trieRoot, String word) {
        TrieNode node = trieRoot;
        for (int i = 0; i < word.length(); i++) {
            int idx = word.charAt(i) - 'a';
            if (node.children[idx] == null) return word;
            node = node.children[idx];
            if (node.isRootEnd) return word.substring(0, i + 1);
        }
        return word;
    }
}
```

## Why it works

Every root traces a unique path from `trieRoot`, ending at a node flagged `isRootEnd`. Walking a word along the same trie follows the path spelled by its own letters, so the first `isRootEnd` node reached is, by construction, the shortest root prefixing the word. If a needed child is missing or no flagged node is ever reached, the word has no root and is returned unchanged.

## Complexity

- Time: O(R + wL) — R total characters across all roots, built once; each word of length L resolves in O(L).
- Space: O(R) — one trie node per distinct character position across all roots.
