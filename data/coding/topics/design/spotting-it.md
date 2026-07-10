Design problems announce themselves — the prompt literally reads like an API spec instead of a single question. Reach for this pattern when you see:

- **"Design a `X` class that supports..."** followed by a bulleted list of methods (`get`, `put`, `insert`, `remove`, `next`) — the classic signature of the whole family.
- **A per-operation complexity requirement**, e.g. "all operations in O(1)" or "average O(1) time" — this is the real constraint; it tells you which structures are even allowed and rules out the naive one.
- **"...with the least recently/frequently used..."** — LRU/LFU cache language, meaning hash map + linked list (or frequency buckets).
- **"...at random with equal probability..."** — GetRandom-style, meaning you need O(1) random access, which means an array is in the mix, not just a map.
- **"...ordered by time / return the value as of a given timestamp"** — Time-Based Key-Value Store, meaning binary search over a list of (timestamp, value) pairs per key.
- **"Implement an iterator for..."** — Flatten Nested List / Peeking Iterator, meaning you manage internal state (a stack or a buffered next) across repeated calls.
- **"Encode ... then decode back to the original"** — Encode/Decode strings or TinyURL, meaning a reversible mapping, often just a counter/hash map.

Signal words: *"design"*, *"implement a data structure"*, *"support the following operations"*, *"O(1)"*, *"as of time t"*, *"evict"*, *"capacity"*. If the problem gives you a *list* of methods to implement rather than one function to write, you are in design-pattern territory — start by writing down each method's required complexity before touching any code.
