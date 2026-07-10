The hash-set DP keeps carving and hashing overlapping substrings, which is wasted effort. Building a trie from every word lets each candidate walk character-by-character instead, checking node-by-node whether the current position ends some dictionary word — nothing is ever substring-copied.

The DP boundary logic is identical to the hash-set version, just discovered while walking the trie rather than via repeated set lookups.

```java
import java.util.*;

class Solution {
    static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd = false;
    }

    public List<String> findConcatenatedWords(String[] words) {
        TrieNode root = new TrieNode();
        for (String w : words) {
            TrieNode node = root;
            for (char ch : w.toCharArray()) {
                int idx = ch - 'a';
                if (node.children[idx] == null) node.children[idx] = new TrieNode();
                node = node.children[idx];
            }
            node.isEnd = true;
        }

        List<String> result = new ArrayList<>();
        for (String word : words) {
            int n = word.length();
            boolean[] dp = new boolean[n + 1];
            dp[0] = true;
            for (int i = 0; i < n; i++) {
                if (!dp[i]) continue;
                TrieNode node = root;
                for (int j = i + 1; j <= n; j++) {
                    int idx = word.charAt(j - 1) - 'a';
                    if (node.children[idx] == null) break;
                    node = node.children[idx];
                    if (node.isEnd && !(i == 0 && j == n)) dp[j] = true;
                }
            }
            if (dp[n]) result.add(word);
        }
        Collections.sort(result);
        return result;
    }
}
```

## Why it works

Walking the trie one character at a time from every reachable boundary `i` visits the same "is this chunk a word?" facts the hash-set version checked via substring lookups, but each character is examined once per walk instead of being copied into a fresh string. A node with `isEnd` true means `word.substring(i, j)` is a dictionary word, making `dp[j]` reachable; skipping `i == 0 && j == n` still blocks the trivial self-match.

## Complexity

- Time: O(n · L²) — n words, each with up to L trie walks of length up to L, no substring allocation.
- Space: O(n · L) — the trie holds at most that many characters.
