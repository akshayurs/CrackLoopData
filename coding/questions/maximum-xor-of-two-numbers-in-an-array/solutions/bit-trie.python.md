To beat O(n²), stop comparing pairs directly and instead build a binary trie over the 32-bit representation of every number, branching on bits from most significant to least significant. For each number, walk the trie greedily choosing, at every level, the child that holds the *opposite* bit — that path always exists as long as the trie already contains at least one other number, and it maximizes the XOR contributed by that bit position.

Insert numbers one at a time and query right after inserting each one, so every pairing is checked against numbers already in the trie without ever comparing the same pair twice.

```python
class TrieNode:
    def __init__(self):
        self.children = {}

def max_xor(nums):
    bits = 31
    root = TrieNode()
    best = 0

    def insert(num):
        node = root
        for b in range(bits, -1, -1):
            bit = (num >> b) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def query(num):
        node = root
        xor_val = 0
        for b in range(bits, -1, -1):
            bit = (num >> b) & 1
            toggled = 1 - bit
            if toggled in node.children:
                xor_val |= (1 << b)
                node = node.children[toggled]
            else:
                node = node.children[bit]
        return xor_val

    insert(nums[0])
    for num in nums[1:]:
        best = max(best, query(num))
        insert(num)
    return best
```

## Why it works

XOR is maximized bit by bit, from the top: a `1` at a given position beats any combination of lower bits, so the greedy choice — always prefer the opposite bit if the trie has it — never gives up a higher bit for a lower one. Inserting a number before it can be queried against later numbers is unnecessary; querying against everything inserted so far already covers every unordered pair exactly once, since each number is queried against all numbers before it in the array.

## Complexity

- Time: O(n) — each of the n numbers does one O(32) insert and one O(32) query.
- Space: O(n) — up to 32n trie nodes in the worst case.
