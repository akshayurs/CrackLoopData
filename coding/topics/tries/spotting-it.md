Reach for a trie the moment a problem is really about **prefixes**, not just membership:

- **"Implement a dictionary / autocomplete"** — `insert`, `search`, `startsWith` are the textbook trie API (Implement Trie).
- **"Search with wildcards"** — a `.` that matches any character needs a trie walk with backtracking/DFS at wildcard nodes (Design Add and Search Words).
- **"Find all words on a grid/board"** — combine a trie of the dictionary with DFS/backtracking on the board so you can prune a branch the instant no word shares that prefix (Word Search II).
- **"Replace each word with its shortest root"** — walk the trie of roots and stop at the first `isEnd` (Replace Words).
- **"Suggest words as the user types"** — the state at each keystroke is exactly a trie node; re-walking on every character is the naive version, tracking the node as you go is the optimized one (Search Suggestions System).
- **"Longest word built one character at a time from other words in the dictionary"** — needs every prefix along the way to also be a valid word, a natural trie DFS (Longest Word in Dictionary).
- **"Sum of all values whose key has a given prefix"** — a trie storing values at end nodes, prefix-summed on insert or on query (Map Sum Pairs).
- **Maximum XOR of two numbers** — a **binary trie** over 32-bit representations; signal words are "maximum XOR", "pairwise XOR", not obviously about strings at all.

Signal words: *"prefix"*, *"starts with"*, *"dictionary"*, *"autocomplete"*, *"suggestions"*, *"root word"*, *"wildcard search"*. If a hash set almost works but keeps failing on "does anything start with…" questions, that gap is the tell you need a trie instead.
