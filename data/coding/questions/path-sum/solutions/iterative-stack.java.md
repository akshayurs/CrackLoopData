Recursion works but risks a stack overflow on a deeply skewed tree, and it hides the traversal state inside the call stack. Make that state explicit: keep an ordinary stack of node/remaining pairs, where `remaining` is the sum still needed once every ancestor on the path from the root has been paid for. A small private record class holds each pair.

Pop one pair at a time. If the popped node is a leaf, check whether its own value finishes off `remaining`; if it does, the whole tree qualifies. Otherwise push each existing child with a `remaining` reduced by the current node's value, and keep going until the stack empties.

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    private record Frame(TreeNode node, int remaining) {}

    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        Deque<Frame> stack = new ArrayDeque<>();
        stack.push(new Frame(root, targetSum));
        while (!stack.isEmpty()) {
            Frame frame = stack.pop();
            int remaining = frame.remaining() - frame.node().val;
            if (frame.node().left == null && frame.node().right == null) {
                if (remaining == 0) return true;
                continue;
            }
            if (frame.node().left != null) stack.push(new Frame(frame.node().left, remaining));
            if (frame.node().right != null) stack.push(new Frame(frame.node().right, remaining));
        }
        return false;
    }
}
```

## Why it works

The stack simulates the same depth-first order recursion would use, just with the "amount still owed" carried alongside each node instead of being an implicit method argument. A leaf is only ever pushed once, is popped once, and is checked exactly like the recursive base case. Because every root-to-leaf path is eventually popped and tested, the loop finds a match if and only if one exists; exhausting the stack without a match proves none does.

## Complexity

- Time: O(n) — every node is pushed and popped exactly once.
- Space: O(h) — the stack holds at most one path's worth of pending siblings, up to O(n) for a skewed tree.
