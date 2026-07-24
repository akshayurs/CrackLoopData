A **trie** (prefix tree) is a tree where each edge is labeled with one character, and every root-to-node path spells out a prefix. Words that share a prefix share the same path, so all common prefixes are stored exactly once. A boolean flag (`isEnd`) on a node marks that the path down to it is a complete word, not just a prefix of a longer one.

Each node holds a small map (or fixed-size array for lowercase letters: `children[26]`) from the next character to the next node. Insert, search, and prefix-check all walk the tree one character at a time — **O(L)** time, where L is the word length, completely independent of how many other words are stored.

That is the superpower: a hash set can tell you if a *whole* word exists, but it cannot answer "does any word start with `ca`?" without scanning everything. A trie answers that in O(L) because prefixes are first-class citizens of the structure.

A typical shape:

```
insert(word):
    node = root
    for ch in word:
        if ch not in node.children:
            node.children[ch] = new TrieNode()
        node = node.children[ch]
    node.isEnd = true

search(word):
    node = walk(word)          # follow children char by char
    return node exists and node.isEnd

startsWith(prefix):
    node = walk(prefix)
    return node exists
```

Beyond dictionaries, tries generalize: a **binary trie over bit representations** of numbers supports maximum-XOR queries in O(32) per number, and tries augmented with word references (storing the string or an index at the end node) power word-search-on-a-board and autocomplete-style problems.
