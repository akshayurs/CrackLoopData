To beat O(n²), stop comparing pairs directly and instead build a binary trie over the 32-bit representation of every number, branching on bits from most significant to least significant. For each number, walk the trie greedily choosing, at every level, the child that holds the *opposite* bit — that path always exists as long as the trie already contains at least one other number, and it maximizes the XOR contributed by that bit position.

Insert numbers one at a time and query right after inserting each one, so every pairing is checked against numbers already in the trie without ever comparing the same pair twice.

```java
class Solution {
    static class Node {
        Node[] children = new Node[2];
    }

    public int maxXor(int[] nums) {
        int bits = 31;
        Node root = new Node();
        insert(root, nums[0], bits);
        int best = 0;
        for (int i = 1; i < nums.length; i++) {
            best = Math.max(best, query(root, nums[i], bits));
            insert(root, nums[i], bits);
        }
        return best;
    }

    private void insert(Node root, int num, int bits) {
        Node node = root;
        for (int b = bits; b >= 0; b--) {
            int bit = (num >> b) & 1;
            if (node.children[bit] == null) node.children[bit] = new Node();
            node = node.children[bit];
        }
    }

    private int query(Node root, int num, int bits) {
        Node node = root;
        int xorVal = 0;
        for (int b = bits; b >= 0; b--) {
            int bit = (num >> b) & 1;
            int toggled = 1 - bit;
            if (node.children[toggled] != null) {
                xorVal |= (1 << b);
                node = node.children[toggled];
            } else {
                node = node.children[bit];
            }
        }
        return xorVal;
    }
}
```

## Why it works

XOR is maximized bit by bit, from the top: a `1` at a given position beats any combination of lower bits, so the greedy choice — always prefer the opposite bit if the trie has it — never gives up a higher bit for a lower one. Querying a number against everything inserted so far, then inserting it, covers every unordered pair exactly once.

## Complexity

- Time: O(n) — each of the n numbers does one O(32) insert and one O(32) query.
- Space: O(n) — up to 32n trie nodes in the worst case.
