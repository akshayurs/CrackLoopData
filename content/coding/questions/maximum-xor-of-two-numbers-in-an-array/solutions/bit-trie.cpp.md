To beat O(n²), stop comparing pairs directly and instead build a binary trie over the 32-bit representation of every number, branching on bits from most significant to least significant. For each number, walk the trie greedily choosing, at every level, the child that holds the *opposite* bit — that path always exists as long as the trie already contains at least one other number, and it maximizes the XOR contributed by that bit position.

Insert numbers one at a time and query right after inserting each one, so every pairing is checked against numbers already in the trie without ever comparing the same pair twice.

```cpp
#include <vector>
#include <algorithm>
#include <memory>
using namespace std;

class Solution {
    struct Node {
        unique_ptr<Node> children[2];
    };

    void insert(Node* root, int num, int bits) {
        Node* node = root;
        for (int b = bits; b >= 0; b--) {
            int bit = (num >> b) & 1;
            if (!node->children[bit]) node->children[bit] = make_unique<Node>();
            node = node->children[bit].get();
        }
    }

    int query(Node* root, int num, int bits) {
        Node* node = root;
        int xorVal = 0;
        for (int b = bits; b >= 0; b--) {
            int bit = (num >> b) & 1;
            int toggled = 1 - bit;
            if (node->children[toggled]) {
                xorVal |= (1 << b);
                node = node->children[toggled].get();
            } else {
                node = node->children[bit].get();
            }
        }
        return xorVal;
    }

public:
    int maxXor(vector<int>& nums) {
        int bits = 31;
        Node root;
        insert(&root, nums[0], bits);
        int best = 0;
        for (size_t i = 1; i < nums.size(); i++) {
            best = max(best, query(&root, nums[i], bits));
            insert(&root, nums[i], bits);
        }
        return best;
    }
};
```

## Why it works

XOR is maximized bit by bit, from the top: a `1` at a given position beats any combination of lower bits, so the greedy choice — always prefer the opposite bit if the trie has it — never gives up a higher bit for a lower one. Querying a number against everything inserted so far, then inserting it, covers every unordered pair exactly once.

## Complexity

- Time: O(n) — each of the n numbers does one O(32) insert and one O(32) query.
- Space: O(n) — up to 32n trie nodes in the worst case.
