Reach for greedy when a problem asks for an **optimum built from a sequence of independent local decisions**, especially:

- **"Can you reach the end?" / "Minimum jumps to reach the end"** — track the furthest index reachable so far as you scan (Jump Game, Jump Game II).
- **"Can you complete the circuit / never go negative?"** — a running total that resets when it dips below zero (Gas Station).
- **"Assign / match items to satisfy the most people"** — sort both sides and match greedily (Assign Cookies).
- **"Split into groups of consecutive/equal values"** — sort or count first, then greedily extend groups (Hand of Straights).
- **"Partition a string/array so each part is as small as possible while keeping some constraint together"** — track the last-seen position of each element (Partition Labels).
- **"Build a target by combining candidates piece by piece"** — take any candidate that doesn't overshoot the target (Merge Triplets to Form Target Triplet).
- **"Validate with wildcards/choices" using a range of possibilities** — track a `[low, high]` range of open counts instead of branching (Valid Parenthesis String).

Signal words: *"minimum number of…"*, *"maximum number of…"*, *"as many as possible"*, *"can you reach/complete"*, *"assign"*, *"partition into the fewest/most"*. If the problem also mentions "any order" or "choose optimally at each step," that's a strong greedy tell.

The trap is that these phrasings overlap heavily with DP. Ask yourself: does an earlier choice ever need to be *undone* based on something you learn later? If yes, it's DP. If the best local move is always safe to commit to, it's greedy — often the same problem family (e.g., interval scheduling) has both a greedy O(n log n) solution and a slower DP one, and the interviewer wants you to notice the cheaper path.
