Instead of recursing, sweep the tree breadth-first with a queue. Every time a real node comes off the queue, record its value and push both children onto the queue — pushing `nullptr` for a missing child rather than skipping it, so the string also encodes exactly where the gaps are.

Deserializing mirrors the same sweep: split the string back into tokens and read them in the order they were written, attaching each one as the left or right child of the next node waiting in a queue, and only enqueuing the children that weren't `"#"`. Because both sides visit nodes level by level, left-to-right, the queues stay in lockstep the whole way through.

```cpp
#include <string>
#include <sstream>
#include <vector>
#include <queue>
using namespace std;

class Codec {
public:
    string serialize(TreeNode* root) {
        if (!root) return "#";
        string out;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* node = q.front(); q.pop();
            if (!node) {
                out += "#,";
                continue;
            }
            out += to_string(node->val) + ",";
            q.push(node->left);
            q.push(node->right);
        }
        return out;
    }

    TreeNode* deserialize(string data) {
        if (data == "#") return nullptr;
        vector<string> vals;
        stringstream ss(data);
        string tok;
        while (getline(ss, tok, ',')) vals.push_back(tok);
        TreeNode* root = new TreeNode(stoi(vals[0]));
        queue<TreeNode*> q;
        q.push(root);
        int i = 1;
        while (!q.empty()) {
            TreeNode* node = q.front(); q.pop();
            if (vals[i] != "#") {
                node->left = new TreeNode(stoi(vals[i]));
                q.push(node->left);
            }
            i++;
            if (vals[i] != "#") {
                node->right = new TreeNode(stoi(vals[i]));
                q.push(node->right);
            }
            i++;
        }
        return root;
    }
};
```

## Why it works

Both serialize and deserialize process nodes in identical breadth-first order, so the i-th "slot" written always corresponds to the i-th child position read back. Skipping the enqueue for `"#"` slots keeps the two queues synchronized without ever confusing a real node with a placeholder.

## Complexity

- Time: O(n) — every node and null placeholder is visited exactly once on each side.
- Space: O(n) — the queue holds up to one level's worth of nodes, and the token vector holds one entry per slot.
