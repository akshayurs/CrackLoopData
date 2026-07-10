Insert every word into a trie, marking the node at the end of each word. Now "buildable" has a direct meaning on this structure: a node represents a buildable word exactly when every node on the path from the root down to it — not just the last one — is marked as an end-of-word. So a depth-first walk that only steps into children which are themselves end-of-word nodes visits precisely the set of buildable words, in one pass, without ever slicing a string to re-check a prefix.

Track the best word found during the walk the same way as before: longer wins, and a length tie goes to the lexicographically smaller string.

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    struct TrieNode {
        TrieNode* children[26] = {};
        bool isEnd = false;
    };

    string longestWord(vector<string>& words) {
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

        string best = "";
        vector<pair<TrieNode*, string>> stack;
        stack.push_back({&root, ""});
        while (!stack.empty()) {
            auto [node, prefix] = stack.back();
            stack.pop_back();
            for (int i = 0; i < 26; i++) {
                TrieNode* child = node->children[i];
                if (child && child->isEnd) {
                    string word = prefix + char('a' + i);
                    if (word.size() > best.size() || (word.size() == best.size() && word < best)) {
                        best = word;
                    }
                    stack.push_back({child, word});
                }
            }
        }
        return best;
    }
};
```

## Why it works

Each edge walked during the DFS corresponds to typing one more letter, and the walk only continues through children flagged `isEnd` — meaning the prefix formed so far is itself a real word. So every string the traversal reaches is guaranteed buildable, and since the trie is only as deep as the longest word, no candidate is ever missed. The length-then-lexicographic comparison at each visited node keeps the required best answer.

## Complexity

- Time: O(∑Lᵢ) — building the trie visits every character once; the traversal visits at most one node per character across all words.
- Space: O(∑Lᵢ) — trie nodes, one per distinct character position inserted.
