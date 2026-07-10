Rather than repeatedly slicing and hashing overlapping substrings, build a trie from every word once. Each candidate word then walks the trie a character at a time from every reachable boundary, checking node-by-node whether the current position ends some dictionary word — no substring is ever allocated.

The DP boundary logic mirrors the hash-set version; it is simply discovered while walking the trie instead of via repeated lookups.

```cpp
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct TrieNode {
    TrieNode* children[26] = {};
    bool isEnd = false;
};

class Solution {
public:
    vector<string> findConcatenatedWords(vector<string>& words) {
        TrieNode root;
        for (const string& w : words) {
            TrieNode* node = &root;
            for (char ch : w) {
                int idx = ch - 'a';
                if (!node->children[idx]) node->children[idx] = new TrieNode();
                node = node->children[idx];
            }
            node->isEnd = true;
        }

        vector<string> result;
        for (const string& word : words) {
            int n = word.size();
            vector<bool> dp(n + 1, false);
            dp[0] = true;
            for (int i = 0; i < n; i++) {
                if (!dp[i]) continue;
                TrieNode* node = &root;
                for (int j = i + 1; j <= n; j++) {
                    int idx = word[j - 1] - 'a';
                    if (!node->children[idx]) break;
                    node = node->children[idx];
                    if (node->isEnd && !(i == 0 && j == n)) dp[j] = true;
                }
            }
            if (dp[n]) result.push_back(word);
        }
        sort(result.begin(), result.end());
        return result;
    }
};
```

## Why it works

Walking the trie one character at a time from every reachable boundary `i` visits the same "is this chunk a word?" facts the hash-set version checked via substring lookups, but each character is examined once per walk instead of being copied into a fresh string. A node with `isEnd` true means `word.substr(i, j - i)` is a dictionary word, making `dp[j]` reachable; skipping `i == 0 && j == n` still blocks the trivial self-match.

## Complexity

- Time: O(n · L²) — n words, each with up to L trie walks of length up to L, no substring allocation.
- Space: O(n · L) — the trie holds at most that many characters.
