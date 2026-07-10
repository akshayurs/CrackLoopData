Instead of re-scanning the whole catalog for every prefix, build the answer once while inserting the products into a trie. Sort the catalog first, then insert products in that order; at every node along a word's path, append the word to that node's own suggestion list as long as it has fewer than three entries. Because insertion happens in sorted order, each node's list ends up already sorted — no extra work needed later.

Answering the query is now just a walk down the trie one character at a time: at each step read the current node's cached list. The moment a character has no matching child, every remaining prefix is a dead end and gets an empty list.

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    private static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        List<String> suggestions = new ArrayList<>();
    }

    public List<List<String>> searchSuggestions(String[] products, String searchWord) {
        Arrays.sort(products);
        TrieNode root = new TrieNode();
        for (String word : products) {
            TrieNode node = root;
            for (char ch : word.toCharArray()) {
                int idx = ch - 'a';
                if (node.children[idx] == null) node.children[idx] = new TrieNode();
                node = node.children[idx];
                if (node.suggestions.size() < 3) node.suggestions.add(word);
            }
        }

        List<List<String>> result = new ArrayList<>();
        TrieNode node = root;
        boolean dead = false;
        for (char ch : searchWord.toCharArray()) {
            if (!dead) {
                node = node == null ? null : node.children[ch - 'a'];
                dead = node == null;
            }
            result.add(node == null ? new ArrayList<>() : node.suggestions);
        }
        return result;
    }
}
```

## Why it works

Inserting products in sorted order means the first (at most) three words that ever pass through a node are, by construction, the three lexicographically smallest words sharing that node's prefix — exactly the suggestions the problem wants, already in order. Once the trie is built, each query character is a single array lookup, so producing all `m` answer lists costs only O(m) node visits plus the O(1) cost of copying each cached list.

## Complexity

- Time: O(N log N + S + m) — sorting the catalog (N products), building the trie over S total characters, then O(m) to answer the query.
- Space: O(S) — the trie holds every character of every product, each node caching at most 3 strings.
