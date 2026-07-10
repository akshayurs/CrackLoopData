Build the dictionary into a 26-way trie once instead of rescanning it for every word. Each root's last character marks its node as a root-end; resolving a word is a single walk down the trie, stopping as soon as a root-end node is hit — that is always the shortest matching root.

A fixed-size `children[26]` array keeps every step a plain index lookup, no hashing needed.

```cpp
#include <string>
#include <vector>
#include <sstream>
using namespace std;

class Solution {
    struct TrieNode {
        TrieNode* children[26] = {};
        bool isRootEnd = false;
    };

    TrieNode trieRoot;

    string shortestRoot(const string& word) {
        TrieNode* node = &trieRoot;
        for (size_t i = 0; i < word.size(); i++) {
            int idx = word[i] - 'a';
            if (!node->children[idx]) return word;
            node = node->children[idx];
            if (node->isRootEnd) return word.substr(0, i + 1);
        }
        return word;
    }

public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        for (const string& root : dictionary) {
            TrieNode* node = &trieRoot;
            for (char ch : root) {
                int idx = ch - 'a';
                if (!node->children[idx]) node->children[idx] = new TrieNode();
                node = node->children[idx];
            }
            node->isRootEnd = true;
        }
        istringstream iss(sentence);
        string word;
        vector<string> result;
        while (iss >> word) result.push_back(shortestRoot(word));
        string out;
        for (size_t i = 0; i < result.size(); i++) {
            if (i) out += " ";
            out += result[i];
        }
        return out;
    }
};
```

## Why it works

Every root traces a unique path from `trieRoot`, ending at a node with `isRootEnd` set. Walking a word down the same trie follows the path spelled by its own characters, so the first `isRootEnd` node reached is, by construction, the shortest root prefixing the word. A missing child or no flagged node along the way means the word has no root and is returned unchanged.

## Complexity

- Time: O(R + wL) — R total characters across all roots, built once; each word of length L resolves in O(L).
- Space: O(R) — one trie node per distinct character position across all roots.
