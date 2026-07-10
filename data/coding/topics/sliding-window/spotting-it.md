Reach for a sliding window the moment a problem is about a **contiguous** run and asks you to optimize or count over it:

- **"Longest/shortest substring or subarray that satisfies …"** — no repeating characters, at most k distinct characters, sum ≥ target. Grow the window until it breaks the rule, shrink until it's valid again.
- **"Maximum/minimum sum (or average) of a subarray of size k"** — the classic fixed-size window; slide one element at a time.
- **"Contains all characters of / is a permutation or anagram of another string"** — Permutation in String, Find All Anagrams — a fixed-size window with a frequency-count comparison.
- **"At most K …" / "exactly K …"** — exactly-K problems (e.g. Subarrays with K Different Integers) often decompose into `atMost(K) - atMost(K-1)`, two variable windows.
- **"Replace at most k characters to make it uniform"** — Longest Repeating Character Replacement — window valid while `(window length - count of majority char) <= k`.

Signal words: *"substring"*, *"subarray"*, *"contiguous"*, *"consecutive"*, *"window of size k"*, *"at most / exactly K"*, *"longest"*, *"shortest"*, *"smallest"* paired with a running constraint (sum, distinct count, character frequency).

The strongest tell is **contiguous** — if the problem instead allows picking non-adjacent elements or any subset, sliding window does not apply; look at DP or backtracking instead. If your first instinct is "check every subarray," that nested loop is exactly the redundant work a window removes, since neighboring subarrays share almost all of their elements.
