Walk the tree in preorder — root, then left, then right — and append every value to a string as you visit it, writing `"#"` wherever a child is missing. That single string captures the whole shape: preorder always visits a node before its subtrees, so replaying the same tokens in the same order rebuilds the tree exactly.

Deserializing reverses the walk. Split the string into tokens and read them one at a time using a shared index; `"#"` means that subtree is `nullptr`, otherwise build a node and recursively fill its left and right children from the same token vector, in the same left-then-right order they were written.

```cpp
#include <string>
#include <sstream>
#include <vector>
using namespace std;

class Codec {
public:
    string serialize(TreeNode* root) {
        string out;
        dfs(root, out);
        return out;
    }

    TreeNode* deserialize(string data) {
        vector<string> tokens;
        stringstream ss(data);
        string tok;
        while (getline(ss, tok, ',')) tokens.push_back(tok);
        int idx = 0;
        return build(tokens, idx);
    }

private:
    void dfs(TreeNode* node, string& out) {
        if (!node) {
            out += "#,";
            return;
        }
        out += to_string(node->val) + ",";
        dfs(node->left, out);
        dfs(node->right, out);
    }

    TreeNode* build(vector<string>& tokens, int& idx) {
        string val = tokens[idx++];
        if (val == "#") return nullptr;
        TreeNode* node = new TreeNode(stoi(val));
        node->left = build(tokens, idx);
        node->right = build(tokens, idx);
        return node;
    }
};
```

## Why it works

Preorder order is unambiguous: a node's token is always immediately followed by the complete encoding of its left subtree, then its right subtree. Because `build` advances a shared index into the same token vector, each recursive call reads the correct next token without storing subtree sizes.

## Complexity

- Time: O(n) — serialize visits every node once; deserialize consumes every token once.
- Space: O(n) — the token vector holds one entry per node (plus nulls); the recursion stack is O(h).
