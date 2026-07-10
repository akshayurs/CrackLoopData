To beat O(n²), stop comparing pairs directly and instead build a binary trie over the 32-bit representation of every number, branching on bits from most significant to least significant. For each number, walk the trie greedily choosing, at every level, the child that holds the *opposite* bit — that path always exists as long as the trie already contains at least one other number, and it maximizes the XOR contributed by that bit position.

Insert numbers one at a time and query right after inserting each one, so every pairing is checked against numbers already in the trie without ever comparing the same pair twice.

```javascript
function maxXor(nums) {
  const bits = 31;
  const root = {};

  function insert(num) {
    let node = root;
    for (let b = bits; b >= 0; b--) {
      const bit = (num >> b) & 1;
      if (!(bit in node)) node[bit] = {};
      node = node[bit];
    }
  }

  function query(num) {
    let node = root;
    let xorVal = 0;
    for (let b = bits; b >= 0; b--) {
      const bit = (num >> b) & 1;
      const toggled = 1 - bit;
      if (toggled in node) {
        xorVal |= (1 << b);
        node = node[toggled];
      } else {
        node = node[bit];
      }
    }
    return xorVal >>> 0;
  }

  insert(nums[0]);
  let best = 0;
  for (let i = 1; i < nums.length; i++) {
    best = Math.max(best, query(nums[i]));
    insert(nums[i]);
  }
  return best;
}
```

## Why it works

XOR is maximized bit by bit, from the top: a `1` at a given position beats any combination of lower bits, so the greedy choice — always prefer the opposite bit if the trie has it — never gives up a higher bit for a lower one. Querying a number against everything inserted so far, then inserting it, covers every unordered pair exactly once.

## Complexity

- Time: O(n) — each of the n numbers does one O(32) insert and one O(32) query.
- Space: O(n) — up to 32n trie nodes in the worst case.
