Reach for 1-D DP the moment a problem sounds like any of these:

- **"In how many distinct ways can you …"** — climb stairs, decode a string, make change, form a combination. Counting the ways almost always means summing over choices at each step.
- **"What is the minimum/maximum … to reach/achieve X?"** — minimum cost to climb stairs, fewest coins to make an amount, maximum money you can rob. Optimization over a sequence of decisions.
- **"Take it or skip it" / "can't pick two in a row / adjacent"** — House Robber-style constraints, where choosing element `i` restricts what you can choose next.
- **"Longest/longest increasing/longest valid … subsequence or subarray"** — the answer at index `i` depends on the best answer at some earlier index `j`.
- **A naive recursive brute force is obviously exponential** — if your first instinct is recursion with branching choices (`solve(i)` calling `solve(i-1)` and `solve(i-2)`, or trying every previous index), that recursion tree with repeated calls is the tell.

Signal words: *"number of ways"*, *"minimum/maximum cost"*, *"longest"*, *"can you reach"*, *"maximum sum/product subarray"*, *"non-adjacent"*, *"break into"*. If the input is a single array or string and the answer only cares about a prefix ending at each position, that single axis of movement is the "1-D" in 1-D DP — no second dimension (like a second string or a grid) is needed. If a second sequence or a 2-D grid enters the picture, it likely belongs to 2-D DP instead.
