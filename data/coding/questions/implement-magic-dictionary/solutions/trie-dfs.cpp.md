Store the dictionary in a trie so shared prefixes are explored once instead of per word. Then answer `search` with a depth-first walk that tracks a "mismatch budget" of exactly one: at each letter of the query you're either allowed to follow the matching child for free, or spend your one allowed substitution to step into a different child.

A query is a hit only if the walk reaches the end of the word with the mismatch budget spent exactly to zero remaining (i.e. used exactly once) and lands on a node marked as the end of a dictionary word.

```cpp
#include <string>
#include <vector>
using namespace std;

class MagicDictionary {
public:
    MagicDictionary() : root(new TrieNode()) {}

    void buildDict(vector<string> dictionary) {
        for (const string& word : dictionary) {
            TrieNode* node = root;
            for (char ch : word) {
                int idx = ch - 'a';
                if (!node->children[idx]) node->children[idx] = new TrieNode();
                node = node->children[idx];
            }
            node->isWord = true;
        }
    }

    bool search(string searchWord) {
        return dfs(root, searchWord, 0, 0);
    }

private:
    struct TrieNode {
        TrieNode* children[26] = {};
        bool isWord = false;
    };

    TrieNode* root;

    bool dfs(TrieNode* node, const string& word, int i, int mismatches) {
        if (i == (int)word.size()) return mismatches == 1 && node->isWord;
        int target = word[i] - 'a';
        for (int edge = 0; edge < 26; edge++) {
            if (!node->children[edge]) continue;
            int extra = edge == target ? 0 : 1;
            if (mismatches + extra > 1) continue;
            if (dfs(node->children[edge], word, i + 1, mismatches + extra)) return true;
        }
        return false;
    }
};
```

## Why it works

The trie lets one substitution be "spent" at any depth: following the edge equal to the query's current letter costs nothing, following any other edge costs the single mismatch we're allowed. Pruning as soon as `mismatches` would exceed 1 keeps the branching bounded — at most one extra edge is ever explored per level beyond the matching one. Requiring `mismatches == 1` at the end rejects exact matches (zero changes) exactly as the problem demands.

## Complexity

- Time: O(26·L) per search, where L is the query length — at each of the L levels at most 26 children are considered, and the mismatch budget stops runaway branching. Building the trie is O(N·L).
- Space: O(N·L) for the trie, where N is the number of words and L their average length.
