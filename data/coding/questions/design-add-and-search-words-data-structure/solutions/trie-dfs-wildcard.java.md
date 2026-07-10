Build a real trie so `addWord` shares structure between words the way a plain `Trie.insert` does: each node holds 26 child slots, one per lowercase letter, plus a flag marking whether a word ends there. Adding a word walks down one character at a time, creating child nodes as needed.

The wildcard is what makes `search` more than a plain trie walk. At an ordinary letter, follow the single matching child, exactly as before. At a `.`, the query doesn't commit to one branch — it means "try every child here and succeed if any of them lead to a match," so `search` becomes a small depth-first exploration that only branches at dots and stays a single path everywhere else.

```java
class WordDictionary {
    private static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isWord = false;
    }

    private final TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            int idx = ch - 'a';
            if (node.children[idx] == null) node.children[idx] = new TrieNode();
            node = node.children[idx];
        }
        node.isWord = true;
    }

    public boolean search(String word) {
        return dfs(root, word, 0);
    }

    private boolean dfs(TrieNode node, String word, int i) {
        if (node == null) return false;
        if (i == word.length()) return node.isWord;
        char ch = word.charAt(i);
        if (ch != '.') return dfs(node.children[ch - 'a'], word, i + 1);
        for (TrieNode child : node.children) {
            if (dfs(child, word, i + 1)) return true;
        }
        return false;
    }
}
```

## Why it works

Each `TrieNode` groups the 26 possible next letters, so words sharing a prefix share the same chain of nodes. `dfs` advances one query character per call: a concrete letter narrows the search to exactly one child, while `.` fans out over every non-null child and returns as soon as any branch reaches the end of `word` on a node flagged as a word ending. Returning `false` on a `null` node prunes dead branches immediately instead of exploring further. Because dots only appear a handful of times per query (bounded by the constraints), the fan-out stays cheap in practice even though it is exponential in the dot count.

## Complexity

- Time: O(L) for `addWord`. `search` is O(26^d * L) in the worst case, where L is the word length and d is the number of dots; with few dots this is close to O(L).
- Space: O(total characters added), since each new character can create one new node; shared prefixes reuse existing nodes.
