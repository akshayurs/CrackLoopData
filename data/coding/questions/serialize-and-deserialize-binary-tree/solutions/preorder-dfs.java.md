Walk the tree in preorder — root, then left, then right — and append every value to a string as you visit it, writing `"#"` wherever a child is missing. That single string captures the whole shape: preorder always visits a node before its subtrees, so replaying the same tokens in the same order rebuilds the tree exactly.

Deserializing reverses the walk. Split the string into tokens and pull them off a queue one at a time; `"#"` means that subtree is `null`, otherwise build a node and recursively fill its left and right children from the same queue, in the same left-then-right order they were written.

```java
import java.util.*;

class Codec {
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        dfs(root, sb);
        return sb.toString();
    }

    private void dfs(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append("#,");
            return;
        }
        sb.append(node.val).append(",");
        dfs(node.left, sb);
        dfs(node.right, sb);
    }

    public TreeNode deserialize(String data) {
        Deque<String> tokens = new ArrayDeque<>(Arrays.asList(data.split(",")));
        return build(tokens);
    }

    private TreeNode build(Deque<String> tokens) {
        String val = tokens.poll();
        if (val.equals("#")) return null;
        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = build(tokens);
        node.right = build(tokens);
        return node;
    }
}
```

## Why it works

Preorder order is unambiguous: a node's token is always immediately followed by the complete encoding of its left subtree, then its right subtree. Because `build` polls tokens off the same deque in that exact order, each recursive call consumes the correct next token without tracking subtree sizes.

## Complexity

- Time: O(n) — serialize visits every node once; deserialize polls every token once.
- Space: O(n) — the token list holds one entry per node (plus nulls); the recursion stack is O(h).
