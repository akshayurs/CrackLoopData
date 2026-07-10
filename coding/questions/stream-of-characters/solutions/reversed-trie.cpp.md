Checking "does the stream end with any word" is the mirror image of "does the stream start with any word" — so reverse every dictionary word before inserting it into a trie. Then, to answer a query, walk that trie backwards from the newest letter toward older ones; a full path to a marked node means some word matches the current suffix.

Only the longest word's length worth of history can ever matter, so a small deque used as a sliding buffer replaces the unbounded stream from the brute-force version — memory per query stays bounded no matter how long the stream runs.

```cpp
#include <deque>
#include <string>
#include <unordered_map>
#include <vector>

class StreamChecker {
public:
    StreamChecker(std::vector<std::string> words) {
        for (const std::string& word : words) {
            Node* node = &root;
            for (auto it = word.rbegin(); it != word.rend(); ++it) {
                if (!node->children.count(*it)) node->children[*it] = Node{};
                node = &node->children[*it];
            }
            node->isWord = true;
            maxLen = std::max(maxLen, (int)word.size());
        }
    }

    bool query(char letter) {
        buffer.push_back(letter);
        if ((int)buffer.size() > maxLen) buffer.pop_front();

        Node* node = &root;
        for (auto it = buffer.rbegin(); it != buffer.rend(); ++it) {
            if (node->isWord) return true;
            auto found = node->children.find(*it);
            if (found == node->children.end()) return false;
            node = &found->second;
        }
        return node->isWord;
    }

private:
    struct Node {
        std::unordered_map<char, Node> children;
        bool isWord = false;
    };

    Node root;
    std::deque<char> buffer;
    int maxLen = 0;
};
```

## Why it works

Reversing every word before insertion turns "ends with word" into "starts with reversed word", which a trie answers naturally by walking from the root. Traversing the buffer newest-letter-first retraces that reversed path; hitting `isWord` at any point means the letters consumed so far — read backwards, i.e. the actual suffix — spell a dictionary word. The buffer only needs to hold `maxLen` letters because no word longer than that could ever match.

## Complexity

- Time: O(L) per query, where L is the longest word length — the trie walk stops as soon as it runs out of buffer or matching edges. Building the trie is O(W * L) once.
- Space: O(W * L) for the trie plus O(L) for the buffer.
