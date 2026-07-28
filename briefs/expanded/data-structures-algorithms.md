# Area: Data Structures & Algorithms (data-structures-algorithms)

## Group: Complexity & Big-O (complexity)

### Topic: What Big-O Actually Claims (what-big-o-actually-claims, beginner)
What Big-O, Big-Theta, and Big-Omega formally claim, and the most common way beginners misread the notation.
- [overview] What Big-O buys you: predicting behavior as input grows, not counting exact steps
- [concept] The formal claim: f(n) is O(g(n)) once n is large enough
- [diagram] Big-O visualized: f(n) trapped under c·g(n) past the crossover point
- [compare] O vs Θ vs Ω: upper, tight, and lower bounds — and why "O" in interviews usually means Θ
- [concept] Why constants and lower-order terms drop out of the notation
- [pitfall] "O(n) means exactly n operations" — a bound is not a count
- [pitfall] Assuming a smaller Big-O always wins at your input size, ignoring the hidden constant

### Topic: The Growth-Rate Ladder (the-growth-rate-ladder, beginner)
The standard complexity classes from O(1) to O(n!), the code shapes that produce each, and how they compare at real input sizes.
- [overview] The ladder from O(1) to O(n!): the classes you must instantly recognize
- [concept] Constant, logarithmic, and linear: what code shape produces each
- [concept] Linearithmic, quadratic, and cubic: nested loops and divide-and-conquer signatures
- [concept] Exponential and factorial: when branching or permutations take over
- [diagram] All seven growth curves on one chart, and where they cross
- [compare] Same task, three complexities: scan every item O(n), halve the range each step O(log n), direct lookup O(1)
- [code] Spotting the complexity from code shape: five snippets, five classes
- [pitfall] O(log n) looks slow on paper but wins at n = 10^9 — why the crossover matters

### Topic: Best, Worst, and Average Case (best-worst-average-case, beginner)
Why a single Big-O answer is incomplete without naming which case — best, worst, or average — and how input shape changes it.
- [overview] Why "what's the Big-O" is an incomplete question without a case
- [concept] Best, worst, and average case: same algorithm, three different answers
- [compare] Linear search's three cases: O(1) best (found first), O(n) worst (not found), O(n) average
- [concept] Average case requires an assumption about input distribution — and that assumption can be wrong
- [pitfall] Quoting only the best case (or only average) when an interviewer wants the worst-case guarantee
- [concept] Input shape matters as much as input size: nearly-sorted, all-duplicates, and adversarial inputs
- [code] Tracing the same function on a best-case input and a worst-case input side by side
- [concept] Why interviewers often ask "can you guarantee that?" — worst-case guarantees vs typical performance

### Topic: Analyzing Code Line-by-Line (analyzing-code-line-by-line, intermediate)
The mechanical technique for deriving a function's Big-O straight from its source — sequential, nested, conditional, and called-function costs.
- [overview] Turning code into a complexity: four rules that cover most snippets
- [concept] Sequential statements add; the slowest one dominates the total
- [concept] Nested loops multiply: why two nested O(n) loops become O(n²)
- [concept] Conditionals take the worst-case branch, not the average of the two
- [code] Walking a real function line-by-line to derive its Big-O
- [concept] A called function's own complexity gets multiplied in, not ignored
- [pitfall] Hidden cost inside a "one-line" call: why `list.pop(0)` isn't O(1)
- [compare] Membership check cost: `x in list` at O(n) vs `x in set` at O(1)
- [pitfall] A loop that looks like O(n) but is bounded by a shrinking variable, not the input size

### Topic: Recursion, Recurrences, and the Recursion Tree (recursion-recurrences-and-the-recursion-tree, intermediate)
Setting up a recurrence relation for recursive code and solving it informally with the recursion tree and Master Theorem intuition.
- [overview] Why recursive code needs its own analysis technique: the recurrence relation
- [concept] Writing T(n): the work at this call, plus the cost of the calls it makes
- [diagram] The recursion tree: a single-branch shrink vs a two-branch split, side by side
- [concept] Solving by the recursion tree: sum the work per level, then sum the levels
- [concept] Master Theorem, informally: work-split rate vs branching rate
- [compare] Three recurrence shapes: T(n)=T(n/2)+O(1), T(n)=2T(n/2)+O(n), T(n)=2T(n-1)+O(1)
- [code] Deriving the recurrence directly from a recursive function's source
- [pitfall] Naive recursive Fibonacci: why T(n)=2T(n-1) is exponential, not linear
- [pitfall] Counting recursive calls instead of total work per call

### Topic: Amortized Analysis (amortized-analysis, intermediate)
Why a rare expensive operation doesn't ruin the average cost per call, using dynamic array resizing as the canonical case.
- [overview] Amortized O(1): why an occasional expensive operation can still average out cheap
- [concept] The dynamic array doubling trick: resize by 2x, not by a fixed amount
- [concept] Why doubling — not growing by a fixed increment — is what makes amortized O(1) possible
- [diagram] Charging the resize: spreading one O(n) copy across the n cheap pushes that earned it
- [concept] The aggregate method: total cost over m operations, divided by m
- [code] Simulating array doubling and counting total copy operations across n pushes
- [compare] Amortized O(1) vs worst-case O(1): why a single push can still cost O(n)
- [pitfall] "Amortized" doesn't mean "always fast" — one call in the sequence can still spike

### Topic: Space Complexity and the Call Stack (space-complexity-and-the-call-stack, intermediate)
What counts as space complexity, and why recursive calls carry a hidden O(depth) cost on the call stack.
- [overview] Space complexity: what actually counts as "extra" memory
- [concept] Auxiliary space vs total space: why the input itself usually isn't counted
- [concept] The call stack is memory too: every recursive call is a stack frame
- [diagram] Stack frames piling up during a depth-n recursive call
- [compare] An iterative O(1)-space loop vs a recursive version of the same logic at O(n) space
- [pitfall] "My recursive function has no extra variables, so it's O(1) space" — the stack disagrees
- [concept] Tail recursion in theory vs practice: why Python, JS, and Java don't optimize it away
- [code] Rewriting a linear-recursive function iteratively to drop space from O(n) to O(1)

### Topic: Space-Time Trade-Offs (space-time-tradeoffs, intermediate)
Deliberately spending memory to buy speed — memoization, precomputed tables, and hashing — as an explicit interview lever.
- [overview] Trading memory for speed: the most common lever in interview optimization
- [concept] Memoization: caching subproblem results to turn exponential time into polynomial
- [compare] Naive recursion vs memoized recursion: same code, O(2^n) time vs O(n) time and space
- [concept] Precomputed lookup tables: paying storage up front to make each query O(1)
- [concept] Hashing as a trade-off: extra memory for a hash table in exchange for O(1) average lookup
- [diagram] The trade-off spectrum: recompute every time vs cache everything, with the middle ground
- [pitfall] Treating "just use a hash map" as free, without naming what it costs in memory
- [concept] The reverse trade: shrinking memory by recomputing instead of storing

**Cross-links:** coding-interview-strategy (verbalizing complexity/trade-off reasoning live in an interview), dynamic-programming (memoization as a full technique with state design), hashing (the hash-table mechanics behind the O(1)-average lookup used here only as a trade-off example)

## Group: Arrays & Strings (arrays-strings)

### Topic: Arrays as Contiguous Memory (arrays-as-contiguous-memory, beginner)
Why array indexing is O(1), the difference between fixed and dynamic arrays, and why inserting or deleting away from the end costs O(n).
- [overview] The array mental model: one contiguous block, and what that buys you
- [concept] Why a[i] is O(1): base address plus i times element size
- [concept] Fixed-size arrays vs dynamic arrays: what Python's list, Java's ArrayList, and C++'s vector are underneath
- [diagram] A dynamic array's backing store: length vs capacity, and the gap between them
- [compare] Insert/delete at the end vs the front vs the middle: O(1) vs O(n) vs O(n)
- [concept] Why shifting is unavoidable: keeping the array contiguous after a middle insert or delete
- [pitfall] Treating `array.insert(0, x)` as free because it reads like one line of code
- [code] Counting element moves for an insert at index 0 vs index n-1

### Topic: String Immutability and the Cost of Concatenation (string-immutability-and-concatenation-cost, beginner)
Why strings are immutable in most languages, why that makes naive loop concatenation O(n²), and the buffer-based fix.
- [overview] Strings are usually immutable — every "modification" makes a new one
- [concept] What immutability means in memory: `s += x` allocates and copies, every time
- [diagram] Building a string with += in a loop: n allocations, each copying more than the last
- [concept] Why that adds up to O(n²): the triangular sum of copy costs
- [pitfall] Missing the O(n²) because each individual `+=` "looks like" O(1)
- [compare] `+=` in a loop vs a buffer joined once at the end
- [code] The same string-building loop: O(n²) with += vs O(n) with a join
- [concept] Why the buffer approach is O(n): appending to a mutable buffer is amortized O(1)
- [concept] Same fix, different name: Java/C# StringBuilder, Python list+join, JS array+join

### Topic: In-Place Reversal, Shifting, and Rotation (in-place-reversal-shifting-rotation, intermediate)
Rearranging an array's contents without allocating a second array: in-place reversal, shifting, and three approaches to rotation by k.
- [overview] In-place transformation: rearranging content within the same block of memory
- [concept] Reversing an array in place: swap from both ends toward the middle
- [concept] Shifting by k naively is O(n·k) — one step at a time, repeated k times
- [compare] Three ways to rotate by k: extra array, block-swap juggling, and the reversal trick
- [diagram] The reversal trick: reverse the whole array, then reverse each half
- [code] Rotating by k in O(n) time and O(1) space using the reversal trick
- [concept] Cyclic replacement: moving each element directly to its final position
- [pitfall] Rotating by k without taking k mod n first
- [pitfall] An "in-place" solution that quietly allocates a second array anyway

### Topic: Prefix Sums (prefix-sums, intermediate)
Precomputing cumulative sums so range-sum queries answer in O(1), extended to 2D and combined with a hash map for subarray-sum problems.
- [overview] Prefix sums: pay O(n) once so every range-sum query costs O(1)
- [concept] Building the array: prefix[i] = prefix[i-1] + arr[i]
- [concept] Answering a range query: sum(l, r) = prefix[r] - prefix[l-1]
- [diagram] Range sum as a subtraction of two prefix totals
- [pitfall] Off-by-one at the boundary: the l=0 case and the missing leading zero slot
- [concept] Extending to 2D: a matrix prefix sum for O(1) sub-rectangle totals
- [code] Building a 2D prefix sum and answering a sub-rectangle query
- [concept] Prefix sum plus a hash map: finding a subarray that sums to exactly k in O(n)
- [compare] Brute-force O(n²) range sums vs O(n) build + O(1) query
- [pitfall] Rebuilding the prefix array on every query instead of once up front

### Topic: Difference Arrays (difference-arrays, intermediate)
The inverse of a prefix sum: applying range increments in O(1) and materializing the result with a single prefix-sum pass.
- [overview] Difference arrays: turning O(n) range updates into O(1) marks
- [concept] Building it: diff[i] = arr[i] - arr[i-1]
- [concept] Applying a range update: +v at diff[l], -v at diff[r+1]
- [diagram] Marking a range increment as two point-edits on the difference array
- [concept] Recovering the final array: one prefix-sum pass over the difference array
- [code] Applying k range-increment operations, then reading back the final array
- [compare] Naive O(n) per update vs O(1) per update with O(n) total reconstruction
- [pitfall] Forgetting the -v at r+1, so the increment leaks past the intended range

### Topic: 2D Arrays and Matrices (2d-arrays-and-matrices, intermediate)
How a matrix is laid out in memory, why traversal order matters, and in-place transforms: transpose, 90° rotation, and spiral order.
- [overview] Matrices as arrays of arrays — and why traversal order matters
- [concept] Row-major layout: how a 2D index maps to one flat memory address
- [compare] Row-major traversal vs column-major traversal: same result, different cache behavior
- [concept] Transposing a matrix in place: swapping across the diagonal
- [diagram] Rotating a matrix 90° in place: transpose, then reverse each row
- [code] Implementing in-place 90° rotation for a square matrix
- [concept] Spiral traversal: walking the boundary layer by layer with shrinking bounds
- [pitfall] Rotating a non-square matrix "in place" — why that only works for square matrices
- [pitfall] Off-by-one boundary errors as spiral layers shrink

### Topic: Manual String Parsing and Conversion (manual-string-parsing-and-conversion, intermediate)
Hand-rolling a parser over a string without library helpers — the atoi pattern, manual tokenizing, and the edge cases interviewers probe.
- [overview] Parsing by hand: walking a string character by character to extract meaning
- [concept] The atoi pattern: skip whitespace, read an optional sign, consume digits, stop at the first non-digit
- [diagram] The atoi state machine: whitespace to sign to digits to done
- [pitfall] Integer overflow mid-parse: checking the bound before you multiply, not after
- [code] Implementing string-to-integer conversion with sign and overflow handling
- [concept] Manual tokenizing: splitting on a delimiter without calling split()
- [pitfall] Mishandling consecutive delimiters or a trailing delimiter as an empty token
- [compare] Single-pass manual parsing vs split()-then-process: when hand-rolling is actually asked for
- [concept] Validating format as you scan, instead of parsing first and checking after

### Topic: In-Place String Compression (in-place-string-compression, intermediate)
Encoding and decoding run-length compression directly into a mutable character buffer, using a read cursor and a lagging write cursor.
- [overview] Compressing runs in place: writing the encoded form back into the same buffer
- [concept] Converting an immutable string to a mutable char buffer before any in-place work
- [concept] Run-length encoding: counting consecutive repeats and writing char+count
- [diagram] A read cursor counting a run while a lagging write cursor encodes it
- [pitfall] A run of 10 or more writing a multi-digit count into single character slots
- [code] Implementing in-place run-length encoding with a read index and a write index
- [concept] The encoded form is only guaranteed shorter for long runs — know when to keep the original
- [pitfall] The write index overtaking the read index and overwriting unread characters
- [concept] Decoding back: expanding char+count pairs into the full run

### Topic: Dutch National Flag Partitioning (dutch-national-flag-partitioning, advanced)
Partitioning an array into three buckets around a fixed pivot value in one in-place pass, as a standalone array technique.
- [overview] The three-bucket problem: sorting an array of only 0s, 1s, and 2s in one pass
- [concept] Three markers, three regions: low, mid, and high sweeping toward each other
- [diagram] The invariant: before low is 0, between low and mid is 1, after high is 2
- [concept] Why swapping at low or high needs a different pointer rule than swapping at mid
- [code] Implementing the one-pass three-way partition
- [compare] One-pass partition, O(n)/O(1) space, vs counting values first and rewriting in two passes
- [pitfall] Advancing mid after every swap, even a swap with high whose new value is still unchecked
- [concept] Generalizing past 0/1/2: partitioning around any fixed pivot into less/equal/greater

**Cross-links:** two-pointers-sliding-window (the converging/read-write index as a general searching pattern — used here only as an implementation detail of in-place transforms; this group owns the full Dutch National Flag treatment, referenced there only as a same-direction-pointer variant), sorting-searching (comparison-sort partition schemes; the Dutch-flag 3-way partition is the same idea reused inside quicksort), intervals (event-based sweep-line range processing, the non-array-indexed cousin of difference arrays), hashing (hash-map mechanics used as a tool in the prefix-sum-equals-k pattern)

## Group: Hashing (hashing)

### Topic: Hash Table Internals & Mechanics (hash-table-mechanics, beginner)
How a hashmap/set actually works underneath — hash functions, buckets, load factor, resizing, and the two families of collision resolution.
- [overview] Why hashmaps turn O(n) lookups into O(1) — the core trade
- [concept] From key to index: what a hash function actually computes
- [diagram] Anatomy of a hash table: buckets, indices, and the backing array
- [concept] Load factor: the ratio that decides when a table resizes
- [diagram] Resizing and rehashing: doubling capacity and remapping every key
- [concept] Collision resolution 1: separate chaining with linked buckets
- [concept] Collision resolution 2: open addressing — linear, quadratic, and double hashing
- [compare] Chaining vs open addressing — cache locality, deletion, and worst-case behavior
- [pitfall] Why "hashmap lookup is O(1)" is only an average-case promise
- [pitfall] Using a mutable object as a key — why it silently breaks lookups after mutation
- [code] Building a minimal hash map with chaining from scratch

### Topic: Hash Sets: Membership, Dedup & Sequence Tricks (hash-sets-membership-dedup, beginner)
Using a hash set to replace linear scans with O(1) membership checks — dedup, set algebra, and the longest-consecutive-sequence trick.
- [concept] Membership testing: swapping a linear scan for a hash set lookup
- [code] Deduplicating a collection while preserving first-seen order
- [concept] Set algebra with hash sets: union, intersection, and difference in O(n)
- [diagram] Two-array intersection: hashing one array before scanning the other
- [concept] The "seen so far" pattern: single-pass detection of duplicates or repeats
- [code] Longest Consecutive Sequence: an O(n) trick using only sequence starts
- [pitfall] Checking `list.contains()` inside a loop and silently going O(n²)
- [compare] Hash set vs sorting for duplicate/intersection problems — when O(n log n) is fine

### Topic: Complement Lookup: The Two-Sum Pattern (complement-lookup-two-sum-pattern, beginner)
The single-pass complement-lookup pattern a hashmap enables — Two Sum and its pair/tuple-sum variants.
- [concept] The complement trick: turning "find a pair" into "have I seen its partner"
- [diagram] Two Sum walkthrough: what the hashmap holds at each step
- [code] Two Sum in one pass with a value-to-index map
- [pitfall] Reaching for nested loops first — and the rare case they're actually right
- [concept] Handling duplicate values and duplicate indices correctly
- [concept] Extending to pair-with-target-difference and count-of-pairs variants
- [compare] Hashmap complement lookup vs sorted two-pointers — when each wins
- [concept] Generalizing to 4Sum II: two pair-sum hashmaps combine for O(n²)

### Topic: Frequency Counting Patterns (frequency-counting-patterns, intermediate)
Counting occurrences with a hashmap to answer anagram, dominant-element, and top-frequency questions in one pass.
- [concept] Building a frequency table in a single pass
- [code] Valid Anagram: comparing two frequency tables
- [concept] Canonical signatures: when a sorted string or count-tuple means "the same"
- [concept] Majority Element via frequency counting — and its O(1)-space alternative
- [diagram] Top-K Frequent Elements: counts feeding a bucket array indexed by frequency
- [compare] Bucket-by-frequency vs a heap for Top-K — O(n) vs O(n log k)
- [pitfall] Re-scanning the input to look up a count you already computed
- [concept] First Unique Character: frequency counting plus an ordered second pass

### Topic: Grouping with Canonical Keys (grouping-with-canonical-keys, intermediate)
Mapping items into groups keyed by a computed signature, and telling a grouping problem apart from a counting one.
- [concept] The group-by pattern: a hashmap of key to list of items
- [code] Group Anagrams: a sorted string as the canonical key
- [compare] Sorted-string key vs 26-count-tuple key — correctness and cost
- [concept] Designing a canonical key for custom groupings (digit sum, shape, remainder)
- [diagram] How grouped buckets fill up over a single scan of the input
- [pitfall] Using a mutable list or an unhashable type directly as a map key
- [concept] Grouping vs counting — recognizing which one the question is really asking for

### Topic: Prefix Sums + Hashmaps for Subarray Problems (prefix-sum-hashmap-patterns, intermediate)
Combining a running prefix sum with a hashmap of seen sums to answer subarray-sum/XOR questions in O(n).
- [overview] Why "Subarray Sum Equals K" resists brute force but folds to O(n)
- [concept] Running prefix sum recap — the value this pattern builds on (see arrays-strings)
- [concept] The core insight: subarray(i, j) sums to K exactly when prefix[j] − prefix[i] = K
- [diagram] Walking the array while a hashmap tracks prefix-sum frequencies
- [code] Subarray Sum Equals K in one pass
- [pitfall] Forgetting to seed the map with prefix sum 0 — miscounting subarrays from index 0
- [concept] Same pattern, different key: counting subarrays with a given XOR
- [code] Continuous Subarray Sum divisible by K — storing remainders, not raw sums
- [compare] Prefix-sum-plus-hashmap vs sliding window — why negative values break the window

### Topic: LRU Cache Design (lru-cache-design, advanced)
Designing an O(1) get/put cache by pairing a hashmap with a doubly linked list — the hashmap is what makes it fast.
- [overview] Why LRU Cache is a favorite design question: two structures, one contract
- [concept] The requirement that rules out a plain hashmap or plain list alone
- [diagram] A hashmap of key to node, pointing into a doubly linked list ordered by recency
- [concept] Why doubly (not singly) linked — O(1) removal needs a back-pointer (see linked-lists)
- [code] get(key): hashmap lookup, then move the node to the front
- [code] put(key, value): insert-or-update, then evict the tail on overflow
- [diagram] Eviction walkthrough: capacity exceeded, tail node unlinked from both structures
- [pitfall] Updating the hashmap but forgetting to unlink the old node, or vice versa
- [compare] LRU vs LFU eviction — recency vs frequency, and LFU's second frequency map
- [pitfall] Off-by-one on capacity checks — evicting before vs after the new insert

**Cross-links:** tries-strings (rolling hash / Rabin-Karp string matching), linked-lists (doubly linked list splicing mechanics for LRU Cache — this group owns the full LRU Cache Design topic since the hashmap is what makes it O(1)), arrays-strings (prefix sum mechanics), heaps (heap-based alternative for top-K frequent elements)

## Group: Two Pointers & Sliding Window (two-pointers-sliding-window)

### Topic: Opposite-End Two Pointers (opposite-end-two-pointers, beginner)
Converging pointers from both ends of a sorted array or string to check or transform it in one O(n) pass.
- [overview] The two-pointer trade: an O(n²) pair check collapses to one O(n) sweep
- [concept] Converging from both ends: when left and right can safely close in
- [code] Reversing an array or string in place with two pointers
- [code] Palindrome check without extra space
- [diagram] Two Sum on a sorted array: why moving left up or right down is always safe
- [concept] The invariant that justifies convergence: what must stay true as pointers move
- [pitfall] Applying opposite-end pointers to an unsorted array and getting it wrong
- [compare] Two pointers vs hashmap complement lookup for pair-sum problems (see hashing)
- [concept] Skipping over duplicates, whitespace, or non-alphanumerics while scanning

### Topic: Two Pointers Across Two Sequences (two-pointers-on-two-sequences, beginner)
Two independent pointers advancing through two different sequences at once — merging, intersecting, or matching them.
- [concept] Two pointers, two sequences: always advancing whichever side is behind
- [diagram] Merging two sorted arrays with one pointer in each
- [code] Merge Sorted Array: merging from the back to avoid overwriting
- [concept] Intersection of two sorted arrays: advancing the smaller-value pointer
- [code] Is Subsequence: checking one string embeds in another in one pass
- [pitfall] Forgetting both sequences must be sorted before this pattern applies
- [compare] Two-pointer merge vs hash-set intersection — O(1) space vs unsorted input

### Topic: Same-Direction Pointers: In-Place Array Rewrites (same-direction-array-pointers, intermediate)
A fast read pointer and a slow write pointer compacting an array in place, plus Floyd's cycle trick reused on arrays.
- [concept] Slow writes, fast reads: compacting an array in place in one pass
- [code] Remove Duplicates from Sorted Array in place
- [code] Move Zeroes to the end while preserving the order of the rest
- [concept] Reusing Floyd's tortoise-and-hare on an array of indices to find a duplicate
- [diagram] Treating array values as "next" pointers to expose an implicit cycle
- [compare] This array-cycle trick vs linked-list cycle detection — same algorithm, different structure (see linked-lists)

(Three-way partitioning with a low/mid/high trio — Dutch National Flag — is also a same-direction-pointer technique; it gets full treatment under `arrays-strings` rather than being duplicated here.)

### Topic: Three & Four Pointer Extensions: kSum Family (three-and-four-pointer-extensions, intermediate)
Fixing one or two elements and two-pointering the rest of a sorted array — 3Sum, 3Sum Closest, and 4Sum.
- [concept] Fix one element, two-point the rest: extending pair-sum to triples
- [diagram] 3Sum walkthrough: an outer loop plus an inner converging pair search
- [code] 3Sum with duplicate-triplet skipping
- [pitfall] Skipping duplicates at the wrong point and missing or repeating triplets
- [concept] 3Sum Closest: tracking the best-so-far instead of exact matches
- [concept] Generalizing to 4Sum: one more fixed loop around the same converging core
- [compare] Sort-plus-two-pointers vs hashmap-based k-sum — time vs space
- [pitfall] Re-deriving 3Sum from scratch instead of recognizing sort + two pointers + a loop

### Topic: Greedy Two Pointers on Height Arrays (greedy-two-pointers-height-arrays, intermediate)
Converging pointers guided by a greedy safety proof on height/skyline arrays — container with most water and trapping rain water.
- [overview] Two problems, one skyline: container with most water and trapping rain water
- [concept] Container With Most Water: why the shorter wall is always safe to move
- [code] Container With Most Water in one pass
- [pitfall] Assuming moving the taller wall could ever help — and the proof it can't
- [concept] Trapping Rain Water: water above a cell depends on the shorter of both max walls
- [diagram] Two-pointer trapping walkthrough: left-max and right-max closing in
- [code] Trapping Rain Water with two pointers and O(1) space
- [compare] Two-pointer trapping vs precomputed max arrays vs a monotonic stack

### Topic: Fixed-Size Sliding Window (fixed-size-sliding-window, beginner)
Sliding a constant-width window across an array or string, updating an aggregate at the edges instead of recomputing it.
- [overview] Sliding a fixed window: recompute-from-scratch vs update-at-the-edges
- [concept] The core trick: subtract the outgoing element, add the incoming one
- [code] Maximum Sum Subarray of Size K
- [diagram] One slide of the window: which element leaves, which one enters
- [pitfall] Recomputing the whole window every step and losing the O(n) win
- [concept] Fixed windows over strings: checking every K-length substring for a property
- [compare] Fixed-size window vs a brute-force nested loop — where the speedup comes from

### Topic: Variable-Size Sliding Window (variable-size-sliding-window, intermediate)
Expanding and shrinking a window based on a condition, when the answer's size isn't fixed in advance.
- [overview] Growing and shrinking: when the window's size is the answer, not a given
- [concept] The expand-then-shrink loop: grow right until invalid, shrink left until valid
- [code] Longest Substring Without Repeating Characters
- [diagram] Window state as it expands past a repeat and then contracts
- [code] Smallest Subarray With a Sum At Least Target
- [concept] Longest Substring With At Most K Distinct Characters
- [pitfall] Shrinking the window one step too far, or forgetting to shrink at all
- [concept] Recognizing the signal: "contiguous" plus "longest/smallest/count" means window
- [compare] Variable window vs prefix-sum-plus-hashmap — why negative values break it (see hashing)

### Topic: Sliding Window with Hashmap State (sliding-window-with-hashmap-state, intermediate)
Pairing a variable window with a frequency map to match, cover, or permute a target pattern.
- [concept] Window plus a "need" map: tracking distance from a target multiset
- [diagram] Minimum Window Substring: need-map, have-count, and the shrink condition
- [code] Minimum Window Substring end to end
- [pitfall] Comparing whole hashmaps every step instead of one "satisfied count"
- [concept] Find All Anagrams in a String: a fixed-width window on the same need-map idea
- [code] Permutation in String: window matches a target's frequency signature
- [compare] Frequency-map window vs sorting each substring to compare — why sorting is too slow
- [concept] Deciding what the map counts: characters, parities, or category tags

### Topic: Sliding Window Extremes with a Monotonic Deque (sliding-window-with-monotonic-deque, advanced)
Maintaining a sliding window's max or min in O(1) amortized time with a monotonic deque of indices.
- [overview] Sliding Window Maximum: why recomputing the max every step is too slow
- [concept] The deque invariant: keep indices whose values decrease front-to-back
- [diagram] Deque contents as the window slides one step at a time
- [code] Sliding Window Maximum with a monotonic deque
- [pitfall] Storing values instead of indices — losing the ability to expire old entries
- [concept] Popping from the front once the window outgrows the oldest index
- [compare] Monotonic deque vs a heap for window max — O(n) amortized vs O(n log k)
- [concept] Deque push/pop invariant mechanics live in stacks-queues — this topic owns the windowing application

**Cross-links:** linked-lists (fast/slow pointer for actual linked-list cycle detection), stacks-queues (monotonic deque push/pop mechanics — this group owns the windowing application on top of them), hashing (complement lookup as an alternative to pair-sum two pointers; prefix-sum+hashmap as the go-to when window values can be negative), sorting-searching (3Sum/4Sum assume the array is already sorted), arrays-strings (Dutch National Flag three-way partitioning gets full treatment there)

## Group: Linked Lists (linked-lists)

### Topic: Linked List Fundamentals (linked-list-fundamentals, beginner)
Node structure, singly/doubly/circular variants, and the core insert/delete operations every list problem builds on.
- [overview] What a linked list gives you that a contiguous array can't
- [diagram] Node anatomy: how next and prev pointers chain into a list
- [compare] Singly vs doubly vs circular: memory cost, traversal direction, and when each wins
- [concept] The dummy head trick that eliminates head-of-list edge cases
- [code] Inserting a node before, after, and at the head in O(1)
- [code] Deleting a node when you're only given that node, not the head
- [pitfall] Rewiring `next` before saving it — the classic dangling-pointer bug
- [pitfall] A circular-list traversal loop that never terminates because it checks the wrong node
- [concept] Why linked lists trade O(1) insertion at a known node for O(n) random access
- [compare] Singly linked list vs dynamic array: what an interviewer is really testing when they ask you to choose

### Topic: Reversing Linked Lists (reversing-linked-lists, intermediate)
In-place reversal of a whole list, a sublist, and fixed-size groups — the pointer-rewiring skill every list interview probes first.
- [concept] The three-pointer walk — prev, curr, next — behind every in-place reversal
- [code] Iteratively reversing an entire singly linked list
- [code] Recursively reversing a list and what "the new head" means at each call
- [compare] Iterative vs recursive reversal: O(1) space vs a hidden O(n) call stack
- [concept] Reversing only a sublist between positions left and right in one pass
- [code] Reversing a linked list in groups of k
- [diagram] Pointer rewiring at each step of a k-group reversal
- [pitfall] Forgetting to reconnect a reversed group's tail to the next group's head
- [pitfall] Swapping next/prev on a doubly linked list but breaking traversal from the old head
- [concept] Reversal as a building block for palindrome checks and list reordering

### Topic: Fast & Slow Pointers on Lists (fast-slow-pointers-on-lists, intermediate)
Using two pointers at different speeds to find cycles, midpoints, and offsets in a single pass with no extra memory.
- [concept] Why moving two pointers at different speeds finds structure with zero extra memory
- [diagram] Floyd's tortoise and hare: why the two pointers are guaranteed to meet inside a cycle
- [code] Detecting a cycle with Floyd's tortoise and hare
- [code] Finding the exact start of a cycle by resetting one pointer to head
- [code] Finding the middle node of a list in a single pass
- [code] Finding the nth node from the end without a two-pass length count
- [concept] Checking whether a linked list is a palindrome in O(1) extra space
- [pitfall] Checking fast.next before fast itself and crashing on odd-length lists
- [code] Aligning two pointers across two different-length lists to find their intersection node
- [compare] Fast/slow pointers vs a hash-set of visited nodes: same answer, different space trade-off

### Topic: Merging & Sorting Linked Lists (merging-and-sorting-linked-lists, intermediate)
Merging sorted lists and adapting merge sort to a structure with no random access.
- [concept] Why merge sort — not quicksort — is the natural fit for sorting a linked list
- [code] Merging two already-sorted linked lists in place
- [code] Splitting a list into halves with slow/fast pointers, then merge-sorting each half
- [compare] Merge sort on a list vs on an array: what changes when you lose random access
- [pitfall] Why quicksort's partition step gets awkward without index-based access
- [concept] Merging k sorted lists: pairwise merging step-by-step
- [code] Removing duplicates from a sorted linked list in one pass
- [concept] Reordering a list end-to-end (L0→Ln→L1→Ln-1→…) by combining split, reverse, and merge

### Topic: Linked List Design Problems (linked-list-design-problems, advanced)
Classic system-style design questions — random-pointer copying, list flattening, digit-wise arithmetic — built entirely on list pointer manipulation. (LRU Cache's doubly-linked-list mechanics are covered under `hashing`, where the hashmap half of that design lives.)
- [overview] Why linked lists anchor some of the most-asked design questions in interviews
- [concept] Copying a list with random pointers using the interleave-then-split trick
- [compare] Hashmap approach vs interleaving trick for copying a list with random pointers
- [code] Flattening a multilevel doubly linked list into a single-level list
- [code] Adding two numbers stored as linked lists, digit by digit with carry
- [pitfall] Dropping the final leftover carry after the longer list runs out

**Cross-links:** `hashing` owns the full LRU Cache Design topic (this group's design problems cross-link there instead of duplicating it); `heaps` for the heap-based alternative to pairwise-merging k sorted lists.

## Group: Stacks & Queues (stacks-queues)

### Topic: Stack & Queue Fundamentals (stack-queue-fundamentals, beginner)
LIFO vs FIFO mechanics and how each is actually implemented over an array or linked list.
- [overview] LIFO and FIFO: the two access disciplines behind every stack and queue problem
- [diagram] Stack push/pop vs queue enqueue/dequeue: what moves where
- [compare] Array-backed vs linked-list-backed stacks: resizing cost vs pointer overhead
- [code] Implementing a stack with a dynamic array: push, pop, peek
- [pitfall] Popping or peeking an empty stack without checking first
- [concept] Why a naive array-based queue wastes space at the front after repeated dequeues
- [code] Implementing a queue with a circular buffer over a fixed-size array
- [compare] Reading a problem statement for the LIFO/FIFO signal it's actually asking for
- [pitfall] Using a list's "remove from front" as a queue dequeue and silently paying O(n)

### Topic: Stack Applications: Parentheses & Expressions (stack-applications-parentheses-expressions, beginner)
The first real patterns a stack unlocks: matching nested structures and evaluating expressions.
- [concept] Why a stack is the natural fit for matching nested, paired structures
- [code] Validating balanced parentheses with a stack
- [pitfall] Checking bracket counts instead of their order and type
- [concept] Finding the next greater element the brute-force way, and why it screams for a smarter stack-based approach
- [concept] Evaluating postfix (Reverse Polish) expressions with a single stack
- [code] Converting infix to postfix with an operator-precedence stack (shunting-yard)
- [code] Evaluating a basic calculator expression with +, -, *, / and parentheses
- [pitfall] Forgetting operator precedence and associativity when popping the operator stack
- [compare] Recursion vs an explicit stack for expression parsing: when you need the explicit version

### Topic: Monotonic Stack (monotonic-stack, intermediate)
Maintaining an ordered stack while scanning so every "next greater/smaller" style question resolves in one linear pass.
- [concept] What "monotonic" buys you: popping an element only once its answer is settled for good
- [diagram] How a monotonic stack grows and shrinks while scanning left to right
- [code] Finding the next greater element for every item in one O(n) pass
- [code] Solving daily temperatures with a monotonic stack of indices
- [concept] Why you push indices, not values, onto a monotonic stack
- [code] Largest rectangle in a histogram using a monotonic stack
- [pitfall] Forgetting to pad with a sentinel to flush the remaining stack at the end
- [concept] Trapping rain water with a monotonic stack, and where the two-pointer approach lives instead
- [compare] Monotonic stack vs brute-force nested loop: turning O(n²) into O(n) by never re-examining an element
- [pitfall] Choosing strictly-greater vs greater-or-equal comparisons and mishandling duplicates

### Topic: Monotonic Deque (monotonic-deque, advanced)
The deque-mechanics half of the monotonic-window pattern — maintaining an invariant while evicting from both ends (the sliding-window-max/min application itself lives in `two-pointers-sliding-window`).
- [concept] Why some problems need eviction from both ends, not just one — the case for a deque over a single-ended stack
- [code] Implementing a deque with O(1) push/pop from both ends over a doubly linked list or circular buffer
- [diagram] A monotonic deque shrinking from both ends as new elements arrive
- [concept] Monotonic deque as a generalization: the front answers the query, the back maintains the invariant
- [pitfall] Forgetting to evict front entries that have fallen outside the relevant range
- [compare] Monotonic deque vs monotonic stack — single-ended eviction vs eviction from both ends

### Topic: Queue-Stack Interconversion (queue-stack-interconversion, intermediate)
Building a queue out of two stacks (and vice versa) and reasoning about the amortized cost of doing so.
- [concept] Implementing a queue with two stacks: an in-stack and an out-stack
- [diagram] Elements flowing from the in-stack to the out-stack only when the out-stack is empty
- [code] Enqueue and dequeue for a two-stack queue
- [concept] Why each element moves at most twice: the amortized O(1) argument
- [code] Implementing a stack using two queues (or one queue with rotation)
- [compare] Two-stack queue vs two-queue stack: which operation absorbs the O(n) cost
- [pitfall] Charging every dequeue O(n) instead of recognizing the amortized cost
- [concept] Why interviewers ask this: it tests amortized reasoning, not just implementation

### Topic: Stack & Queue Design Problems (stack-queue-design-problems, intermediate)
Design questions that bolt an extra O(1) guarantee — minimum, capacity, bulk increment — onto a stack or queue.
- [overview] Why "design a stack or queue with an extra guarantee" is its own interview category
- [concept] Min-stack: tracking the running minimum without rescanning on every pop
- [code] Implementing min-stack by pushing (value, min-so-far) pairs
- [compare] Auxiliary min-stack vs storing pairs on the main stack: memory vs simplicity
- [code] Designing a circular queue with fixed capacity and O(1) enqueue/dequeue
- [pitfall] Distinguishing a full circular queue from an empty one when head equals tail
- [concept] Designing an increment-supporting stack by batching lazy updates instead of touching every element
- [pitfall] Popping from a min-stack after a batched "increment all" without adjusting the stored minimum correctly

**Cross-links:** `two-pointers-sliding-window` owns the sliding-window-max/min application built on this group's monotonic deque, and owns the index-pointer approach to problems like trapping rain water; `heaps` for the heap-based alternative to sliding-window maximum.

## Group: Trees & BSTs (trees-bst)

### Topic: Binary Tree Fundamentals (binary-tree-fundamentals, beginner)
Core vocabulary and shape/representation of binary trees that every later tree algorithm assumes.
- [overview] Binary trees at a glance: nodes, edges, and why they anchor half of DSA interviews
- [concept] Core vocabulary: height, depth, level, and ancestor/descendant
- [concept] Full, complete, perfect, and degenerate trees — recognizing shape from a picture
- [diagram] Indexing a complete binary tree in an array with 2i+1 / 2i+2
- [compare] Array-backed vs pointer-backed representations — memory, resizing, and cache behavior
- [concept] Why tree algorithms are naturally recursive: base case is null, recursive case is the subtrees
- [pitfall] "Balanced" does not mean "complete" — the shape guarantees interviewers actually test
- [concept] Computing height, counting nodes, and counting leaves in one recursive pass
- [pitfall] Height-as-edges vs height-as-nodes — the off-by-one that breaks base-case comparisons

### Topic: DFS Traversals: Recursive, Iterative, and Morris (dfs-traversals-recursive-and-iterative, beginner)
Preorder, inorder, and postorder — recursive, iterative, and O(1)-space (Morris) implementations.
- [overview] The three DFS orders and when each one is the right tool
- [concept] Preorder, inorder, and postorder — what each order is actually for (copy trees, BST sorted output, safe deletion)
- [code] Recursive preorder, inorder, and postorder in a few lines each
- [code] Iterative preorder and inorder with an explicit stack
- [pitfall] Iterative postorder is the hard one — why a single stack needs a "last visited" trick
- [compare] Recursive vs iterative traversal — call stack limits and when recursion blows up
- [diagram] Walking the stack state frame-by-frame for an inorder traversal
- [concept] Morris traversal: threading temporary links to get O(1) space inorder
- [code] Morris inorder traversal, and restoring the tree's original shape afterward
- [pitfall] Forgetting to remove Morris's temporary threads and corrupting the tree
- [concept] Choosing inorder-on-BST as the workhorse for "is this a valid BST" and "kth smallest"

### Topic: BFS and Level-Order Traversal (bfs-level-order-traversal, beginner)
Queue-driven level-by-level traversal and its zigzag/min-depth/next-pointer variants.
- [overview] Level-order traversal: processing a tree one BFS layer at a time
- [concept] Queue mechanics: why BFS needs a queue and DFS needs a stack
- [code] Level-order traversal that groups nodes by level using a level-size snapshot
- [concept] Zigzag (spiral) level order — alternating direction without extra passes
- [code] Zigzag level order using a deque or a reversal flag
- [concept] Minimum depth via BFS — why BFS beats DFS when you need the shortest path to a leaf
- [diagram] Queue state at each level while traversing a sample tree
- [pitfall] Snapshotting queue size before the inner loop — the bug that merges levels together
- [concept] Populating next-right pointers level by level in constant extra space

### Topic: Binary Search Trees (binary-search-trees, beginner)
The BST invariant and its search/insert/delete/validate/kth-element operations.
- [overview] The BST invariant and why it turns search into a decision tree
- [concept] Search and insert — following the invariant down to a null slot
- [code] Iterative BST search and insert
- [concept] Deletion's three cases: leaf, one child, two children
- [code] Deleting a two-child node via inorder successor (or predecessor) swap
- [pitfall] Validating a BST by checking only the immediate parent instead of the full ancestor range
- [code] Validating a BST correctly using a (min, max) bound passed down the recursion
- [concept] Kth smallest/largest via inorder traversal, and the early-exit optimization
- [concept] Floor, ceiling, successor, and predecessor without extra pointers
- [compare] BST vs sorted array vs hash map — when ordered operations justify the tree
- [pitfall] Sorted input degrading a BST's insert order into a linked list

### Topic: Vertical Order and Tree Views (vertical-order-and-tree-views, intermediate)
Reading a tree by direction or column — left/right/top/bottom view, vertical order, boundary, and diagonal traversal.
- [overview] The "view" family of problems: reading a tree from a direction instead of an order
- [concept] Right view and left view via BFS (last/first node per level) or DFS (depth-first-seen)
- [code] Right side view using level-order traversal
- [concept] Assigning (row, column) coordinates to enable top/bottom/vertical problems
- [diagram] Column and row coordinates overlaid on a sample tree for vertical-order grouping
- [code] Vertical order traversal with column-grouped BFS and stable tie-breaking
- [pitfall] Top view ties at the same column — why BFS order (not DFS) decides the correct answer
- [compare] Top view vs bottom view — same coordinates, opposite tie-breaking rule
- [concept] Boundary traversal: left edge + leaves + right edge, without double-counting corners
- [concept] Diagonal traversal: grouping nodes that share a diagonal slope
- [pitfall] Using DFS recursion depth as a stand-in for BFS level — where view answers silently break

### Topic: Tree Construction and Serialization (tree-construction-and-serialization, intermediate)
Rebuilding a unique tree from traversal pairs, and serializing/deserializing it losslessly.
- [overview] Rebuilding a tree from traversals, and why some pairs aren't enough
- [concept] Preorder + inorder: root from preorder, split boundary from inorder
- [diagram] Splitting an inorder array into left/right subtree ranges around the root found in preorder
- [code] Building a tree from preorder and inorder arrays in O(n) with an index map
- [concept] Postorder + inorder — same idea, root comes from the end
- [pitfall] Preorder + postorder alone can't reconstruct a unique tree without null markers
- [concept] Serialization formats: preorder-with-nulls vs level-order-with-nulls
- [code] Serializing and deserializing a binary tree using preorder and null sentinels
- [compare] Preorder-null serialization vs level-order-null serialization — size and simplicity trade-offs
- [pitfall] Duplicate values breaking naive index-lookup construction — needing position maps, not value maps

### Topic: Diameter, Height, and Path Sum Problems (diameter-height-and-path-sum-problems, intermediate)
The "return one value, track another" recursion pattern behind diameter, max path sum, and path-count problems.
- [overview] The pattern behind diameter, max path sum, and path-count problems: return one value, track another
- [concept] Diameter of a tree: the longest path measured in edges between any two nodes
- [code] Computing diameter and height together in a single post-order pass
- [pitfall] Recomputing height separately for every node — the O(n²) mistake
- [concept] Maximum path sum: a path can start and end anywhere, not just at the root
- [code] Max path sum using "best downward path" as the return value and a global max as a side channel
- [pitfall] Letting a path bend through both children when contributing to the parent's return value
- [concept] Root-to-leaf path sum vs any-node-to-any-node path sum — different problems, same tree
- [code] Path Sum III using prefix-sum counts propagated through the recursion
- [compare] Recursion-return-value pattern vs prefix-sum pattern — picking the right one per path-sum variant

### Topic: Lowest Common Ancestor (lowest-common-ancestor, intermediate)
Finding the lowest common ancestor in a general tree, a BST, and with parent pointers.
- [overview] LCA: the ancestor question that shows up disguised in a dozen tree problems
- [concept] Recursive LCA in a general binary tree — the "found in both subtrees" signal
- [diagram] How the "found" signal bubbles up from two target nodes to their split point
- [code] LCA of a binary tree in one recursive pass, no parent pointers needed
- [concept] LCA in a BST — using the ordering property to skip recursing into both sides
- [code] Iterative BST LCA in O(height) with no extra space
- [concept] LCA with parent pointers — turning it into a linked-list-intersection problem
- [pitfall] Assuming both nodes exist in the tree — LCA breaks silently if one node is missing
- [compare] General-tree LCA vs BST LCA vs parent-pointer LCA — picking the right one from the input shape
- [concept] LCA as a building block: distance between two nodes, and LCA of more than two nodes

### Topic: Self-Balancing Trees: AVL and Red-Black (self-balancing-trees-avl-and-red-black, advanced)
Why BSTs need rebalancing, and the rotation/invariant mechanics of AVL and red-black trees.
- [overview] Why BSTs need rebalancing, and the two classic answers: AVL and red-black
- [concept] AVL's balance factor and the height-difference invariant it enforces
- [diagram] The four rotation cases: LL, RR, LR, RL
- [code] Single rotation (LL/RR) and double rotation (LR/RL) mechanics
- [pitfall] Forgetting to update heights bottom-up after a rotation, leaving stale balance factors
- [concept] Red-black invariants: no two red nodes in a row, equal black-height on every root-to-null path
- [compare] AVL vs red-black — stricter balance and faster lookups vs fewer rotations and faster writes
- [concept] Where these live in practice: TreeMap/std::map as red-black trees under the hood
- [pitfall] Assuming "balanced tree" always means AVL-strict — most production trees favor red-black's looser balance
- [concept] Amortized rotation cost: why insert/delete stay O(log n) despite rebalancing

### Topic: Binary Lifting and Ancestor Queries (binary-lifting-and-ancestor-queries, advanced)
Precomputed 2^k-ancestor tables for O(log n) kth-ancestor and LCA queries on a static tree.
- [overview] Answering thousands of ancestor/LCA queries fast on a tree that never changes
- [concept] The doubling idea: precompute 2^k-th ancestors, then compose powers of two
- [diagram] The sparse table of 2^k-th ancestors for a small tree, column by column
- [code] Building the binary lifting table with a DP over (node, k)
- [code] Kth ancestor query by decomposing k into its binary representation
- [concept] LCA via binary lifting: lift the deeper node first, then binary-search the split point
- [code] LCA query using the precomputed table in O(log n) per query
- [pitfall] Forgetting to equalize depths before lifting both nodes together
- [compare] Binary lifting vs Euler tour + sparse-table RMQ — both O(log n) LCA, different constants and use cases
- [concept] When binary lifting earns its preprocessing cost: many queries on a static or append-only tree

### Topic: Segment Trees (segment-trees, advanced)
A recursive range-query/update structure supporting O(log n) queries after O(n) build, with lazy propagation.
- [overview] Segment trees: answering range queries in O(log n) after O(n) preprocessing
- [concept] The recursive structure: each node owns a range, split at the midpoint
- [diagram] Building a segment tree over an 8-element array and its node ranges
- [code] Building a segment tree and answering a range-sum query
- [code] Point update: propagating a single changed value back up to the root
- [pitfall] Off-by-one range splits (mid vs mid+1) that silently drop or double-count elements
- [concept] Lazy propagation: deferring range updates until a query actually needs that subtree
- [code] Range update with lazy propagation
- [compare] Segment tree vs Fenwick tree vs prefix-sum array — pick by update frequency and query type
- [concept] Beyond sum: adapting the same structure for range min, max, or GCD queries

### Topic: Fenwick Tree (Binary Indexed Tree) (fenwick-tree-binary-indexed-tree, advanced)
A compact array-based structure for O(log n) prefix-sum queries and point/range updates.
- [overview] Fenwick trees: prefix sums and point updates in O(log n) with a tiny array
- [concept] The lowbit trick: how index & (-index) encodes the tree's implicit structure
- [diagram] Visualizing which indices a Fenwick tree node is responsible for
- [code] Point update and prefix-sum query in a few lines each
- [pitfall] 0-indexed vs 1-indexed Fenwick trees — why the structure assumes 1-indexing
- [concept] Range sum query as a difference of two prefix sums
- [concept] Range update, point query — flipping the trick with a difference array
- [code] Range update, range query — the two-BIT trick for full generality
- [compare] Fenwick tree vs segment tree — less code and lower constant factor vs more query flexibility
- [concept] When a Fenwick tree is the right-sized tool: sum/count range problems without needing min/max

**Cross-links:** general (non-tree) graph DFS/BFS, connectivity, and shortest-path algorithms live in `graphs`.

## Group: Heaps & Priority Queues (heaps)

### Topic: Binary Heap Fundamentals (binary-heap-fundamentals, beginner)
The heap property and its array-based complete-tree representation.
- [overview] Binary heaps: the array-backed tree that powers every priority queue
- [concept] The heap property: min-heap and max-heap, and why it's weaker than a BST's full ordering
- [diagram] Storing a complete binary tree in a flat array — parent and child index formulas
- [compare] Heap vs BST — trading full ordering for O(1) peek and simpler rebalancing
- [pitfall] Expecting a heap array to read out in sorted order left to right
- [concept] Why a heap must be a complete tree — what that buys for the array trick
- [pitfall] Confusing "root is the min" with "every level is sorted" — siblings have no ordering relationship

### Topic: Heap Operations: Insert, Extract, and Build-Heap (heap-operations-insert-extract-and-build-heap, beginner)
Sift-up, sift-down, O(n) build-heap, and heap sort built from the same two primitives.
- [overview] The three moves that implement every heap: sift-up, sift-down, and build-heap
- [concept] Insert: append then sift-up to restore the heap property
- [code] Sift-up implementation with parent-index comparisons
- [concept] Extract-root: swap with the last element, shrink, then sift-down
- [code] Sift-down implementation, always swapping with the smaller (or larger) child
- [pitfall] Sifting down against the wrong child when only one child exists
- [concept] Build-heap in O(n): sifting down from the last internal node beats inserting one by one
- [compare] Build-heap O(n) vs n sequential inserts at O(log n) each — why the bound differs
- [code] Heap sort: repeatedly swap the root to the end and sift-down the shrinking heap
- [pitfall] Heap sort's in-place swaps silently destroying the original array order

### Topic: Priority Queues in Practice (priority-queues-in-practice, beginner)
Using a language's priority queue correctly — comparators, min/max flips, and the decrease-key gap.
- [overview] Using a priority queue as a tool, not building one from scratch
- [concept] Push, pop, and peek — the interface every language's PQ exposes
- [code] Min-heap vs max-heap with a language's default (the negation trick where max-heap isn't built in)
- [concept] Custom comparators: ordering tuples, objects, or (priority, value) pairs correctly
- [pitfall] Ties in the comparator falling through to an unorderable second field
- [code] A comparator-based priority queue ordered by two fields of a custom object
- [concept] Why standard heaps don't support decrease-key, and what that costs Dijkstra-style algorithms
- [compare] Lazy deletion (skip stale entries on pop) vs a true indexed/updatable heap

### Topic: Top-K and Kth-Element Patterns (top-k-and-kth-element-patterns, intermediate)
Fixed-size-K heaps for kth-element and top-K-frequent problems, and when they beat sorting.
- [overview] The top-K family: why a size-K heap beats sorting the whole input
- [concept] Kth largest element — a min-heap of size K, evicting the smallest when it overflows
- [code] Kth largest in a stream using a fixed-size min-heap
- [concept] Top-K frequent elements — count first, then heap on frequency
- [code] Top-K frequent elements with a size-K heap over a frequency map
- [compare] Heap O(n log k) vs full sort O(n log n) vs quickselect O(n) average — picking by constraints
- [pitfall] Building a heap of all n elements when only a size-K heap was needed
- [concept] K closest points/elements — same pattern, a different distance key
- [pitfall] Forgetting to pop before push (or vice versa) and letting the heap grow past size K

### Topic: K-Way Merge (k-way-merge, intermediate)
Merging K sorted sequences (or finding the smallest range across them) with one heap seeded from each source.
- [overview] Merging K sorted sequences without concatenating and re-sorting everything
- [concept] Seeding a heap with the first element of each list, tagged by source
- [diagram] Heap contents and the merged output growing round by round across three sorted lists
- [code] Merging K sorted lists using a heap of (value, list-index, element-index)
- [pitfall] Forgetting to push the next element from the same source after popping — stalling the merge
- [concept] Complexity: O(n log k) total comparisons instead of O(nk) with a linear scan each round
- [concept] Smallest range covering an element from each of K lists — sliding the heap's minimum forward
- [code] Smallest-range-covering-K-lists using a heap plus a running max
- [compare] K-way merge via heap vs divide-and-conquer pairwise merging — same bound, different constants
- [pitfall] Using a heap of size K when K is large and lists are short — a linear merge may actually be faster

### Topic: Two-Heap Median Finder (two-heap-median-finder, intermediate)
Tracking a running median from a stream by balancing a max-heap and a min-heap.
- [overview] Finding a running median from a data stream with two heaps instead of a sorted structure
- [concept] Splitting the stream into a max-heap (lower half) and a min-heap (upper half)
- [diagram] The two-heap split after inserting a stream of numbers one at a time
- [concept] The balance invariant: sizes differ by at most one, lower-half max ≤ upper-half min
- [code] Insert with rebalancing: push to one heap, then transfer the root if sizes drift
- [code] Reading the median in O(1) from the two heap roots
- [pitfall] Inserting into the wrong heap first and skipping the cross-check against the other root
- [compare] Two-heap median vs a sorted-insert structure (BST/skip list) — simpler code, same O(log n) insert
- [concept] Extending the pattern: sliding-window median, and why removal breaks the simple two-heap trick
- [pitfall] Assuming two heaps alone support O(log n) deletion of an arbitrary (non-root) element

### Topic: Heap-Based Greedy Patterns (heap-based-greedy-patterns, intermediate)
Greedy problems where the next best choice changes after every step — task scheduling, string rearrangement, and rope/stone merging.
- [overview] Greedy problems that need "always take the current best" — a heap makes that O(log n) per step
- [concept] Task scheduler: a max-heap on frequency, with cooldown enforced by a waiting queue
- [code] Task scheduler implementation using a frequency max-heap and a cooldown buffer
- [concept] Reorganize string / rearrange-so-no-two-adjacent-match — the same greedy-by-frequency idea
- [pitfall] Greedily placing the most frequent character without checking it against the previous slot
- [concept] Connect ropes / merge stones at minimum cost — always combine the two cheapest first
- [code] Minimum cost to connect ropes using a min-heap (Huffman-style greedy merge)
- [compare] Greedy-with-heap vs greedy-with-sort — the next "best" choice changes after merges vs is fixed upfront
- [pitfall] Assuming a heap-based greedy choice is optimal without an exchange-argument justification

### Topic: Advanced Heap Variants (advanced-heap-variants, advanced)
d-ary heaps, indexed/updatable priority queues for true decrease-key, and why Fibonacci heaps rarely get implemented.
- [overview] Beyond the textbook binary heap: variants built for specific bottlenecks
- [concept] d-ary heaps: fewer levels make sift-up (and decrease-key) cheaper, but each sift-down compares against more children
- [compare] Binary heap vs d-ary heap — raise d when inserts/decrease-key dominate; keep d=2 when extract-min dominates
- [concept] Indexed (updatable) priority queues: tracking each element's heap position for true decrease-key
- [code] Decrease-key with an index map, as Dijkstra and Prim actually need it
- [concept] Binomial and Fibonacci heaps — the conceptual idea behind O(1) amortized decrease-key
- [pitfall] Citing Fibonacci-heap Dijkstra complexity without being able to explain why it's rarely implemented in practice
- [compare] When an indexed/Fibonacci heap earns its complexity vs when a plain heap + lazy deletion is good enough

**Cross-links:** interval-overlap scheduling (e.g., meeting rooms) lives in `intervals`; exchange-argument proofs for greedy choices live in `greedy`; heap-based priority selection inside Dijkstra/Prim lives in `graphs`.

## Group: Tries & String Algorithms (tries-strings)

### Topic: Trie Construction and Operations (trie-construction-and-operations, beginner)
Node design, insert/search/prefix-search, and safe deletion in a prefix tree.
- [overview] Tries: a tree shaped by shared prefixes instead of by comparisons
- [concept] Node design: children as a fixed 26-array vs a hash map, and the space/speed trade-off
- [code] Insert: walking or creating a child per character, then marking end-of-word
- [code] Search and startsWith (prefix search) — the only difference is the end-of-word check
- [diagram] Building a trie from a small word set and watching shared prefixes collapse into one path
- [concept] Time complexity is per-character, not per-word — O(L) regardless of dictionary size
- [pitfall] Marking "isEndOfWord" incorrectly so a prefix is mistaken for a complete word (or vice versa)
- [code] Deleting a word: unmarking end-of-word and pruning now-unused nodes back up the path
- [pitfall] Deleting nodes that are still shared by another word's prefix

### Topic: Trie Applications (trie-applications, intermediate)
Prefix-shaped problems a trie solves cleanly — autocomplete, Word Search II, shortest-root replacement, and binary XOR tries.
- [overview] What tries are actually for: prefix-shaped problems a hash map can't solve as cleanly
- [concept] Autocomplete: collecting all words under a prefix node via DFS
- [code] Autocomplete/word-suggestions implementation from a prefix's subtree
- [concept] Word Search II: pruning a board DFS by walking a trie instead of testing each word separately
- [code] Board DFS plus trie pruning, removing matched leaves to avoid re-finding them
- [pitfall] Running a fresh board search per dictionary word instead of searching all words at once via a shared trie
- [concept] Longest common prefix of a word list via the trie's first branching point
- [code] Replace Words: mapping each word to its shortest dictionary root using prefix search
- [concept] Binary tries over bit representations: maximum XOR pair by walking opposite bits greedily
- [compare] Trie vs hash set for prefix queries — a hash set can't answer "does any word start with X" in O(L)

### Topic: Naive Pattern Matching and KMP (naive-pattern-matching-and-kmp, intermediate)
From O(nm) brute-force substring search to O(n+m) KMP via the failure (LPS) array.
- [overview] Substring search: from O(nm) brute force to O(n+m) with KMP
- [concept] Brute-force matching, and exactly where it wastes work re-scanning the text
- [code] Naive pattern matching with the sliding comparison loop
- [concept] The failure function: for each prefix of the pattern, its longest proper prefix that's also a suffix
- [diagram] Building the LPS array for a pattern with a repeating structure (e.g., "ababaca")
- [code] Computing the LPS array in O(m)
- [concept] The main KMP scan: on mismatch, jump using LPS instead of restarting from the text's next character
- [code] KMP search using the precomputed LPS array
- [pitfall] Off-by-one errors in the LPS array shifting the resume point wrong after a mismatch
- [compare] KMP vs brute force vs a built-in string search — when the O(n+m) guarantee actually matters

### Topic: Rabin-Karp and Rolling Hash (rabin-karp-and-rolling-hash, intermediate)
Polynomial rolling hashes for O(1)-amortized substring comparison, with collision-safe verification.
- [overview] Rabin-Karp: turning substring comparison into a single number comparison
- [concept] Polynomial rolling hash: treating a substring as a base-B number over its characters
- [code] Computing the initial window's hash in O(m)
- [diagram] Sliding the window one character right — which term drops, which term is added
- [concept] Rolling the hash forward in O(1): drop the leading character's contribution, add the new one
- [code] The roll step: recomputing the next window's hash from the previous one
- [pitfall] Hash collisions — two different substrings hashing equal — always verify with a direct comparison
- [concept] Choosing modulus and base to keep collision probability low without overflowing
- [concept] Multiple-pattern search: hashing several patterns once and scanning the text in a single pass
- [compare] Rabin-Karp vs KMP — average-case simplicity vs a guaranteed worst-case linear time
- [pitfall] Forgetting modular arithmetic on subtraction, producing negative hash values

### Topic: Z-Function and Pattern Matching (z-function-and-pattern-matching, advanced)
The Z-array's O(n) construction and its use for substring search and border/period problems.
- [overview] The Z-array: for every position, how far it matches the string's own prefix
- [concept] Z-array definition, and reading off pattern matches where Z equals the pattern length
- [diagram] Z-array values on a sample string, and the Z-box (match window) that speeds computation
- [code] Building the Z-array in O(n) using the current Z-box to skip redundant comparisons
- [concept] Using the Z-array for pattern search: concatenate pattern + separator + text
- [pitfall] Picking a separator character that could actually appear in the input, corrupting the match boundary
- [compare] Z-function vs KMP's LPS array — both O(n), different bookkeeping, same substring-search power
- [concept] Other uses: counting a string's distinct periods and finding all its borders

### Topic: Suffix Arrays and Suffix Trees (Intro) (suffix-arrays-and-suffix-trees-intro, advanced)
Sorted-suffix indexing, the LCP array, and the substring problems they unlock, at an intro level.
- [overview] Suffix arrays: sorting every suffix of a string to answer substring questions fast
- [concept] What a suffix array stores — starting indices of suffixes in sorted order, not the suffixes themselves
- [diagram] The suffix array of a short string alongside its sorted suffixes
- [concept] Naive O(n² log n) construction vs prefix-doubling O(n log n)
- [code] Binary-searching for a pattern inside the suffix array in O(m log n)
- [concept] The LCP (longest common prefix) array and what it adds on top of the suffix array
- [concept] Longest repeated substring as the maximum value in the LCP array
- [compare] Suffix array vs suffix tree — same problems solved, array trades tree pointers for sorted-index simplicity
- [pitfall] Treating from-scratch O(n log n) suffix array construction as interview-expected — most interviews expect recognition, not the build

### Topic: Manacher's Algorithm for Palindromes (manachers-algorithm-for-palindromes, advanced)
Linear-time longest-palindromic-substring detection using mirrored radii around a unification trick.
- [overview] Finding every palindromic substring's length in O(n) instead of O(n²)
- [concept] Expand-around-center at O(n²): the baseline this algorithm improves on
- [pitfall] Handling even-length and odd-length palindromes as separate cases instead of unifying them
- [concept] The unification trick: inserting separators so every palindrome becomes odd-length
- [concept] The mirror property: reusing a palindrome's mirror radius inside a known palindromic span
- [diagram] The radius array and current rightmost palindrome boundary as the scan progresses
- [code] Manacher's algorithm computing the radius array in one linear pass
- [pitfall] Forgetting to cap the mirrored radius at the current right boundary before expanding further
- [compare] Manacher's vs expand-around-center — when the O(n) guarantee is worth the extra bookkeeping

**Cross-links:** general hash table mechanics and collision handling live in `hashing` (this group owns only string rolling-hash mechanics); the maximum-XOR binary trie pattern borrows bit tricks from `bit-manipulation`.

## Group: Graphs (graphs)

### Topic: Graph Representations (graph-representations, beginner)
How to encode a graph as an adjacency list, matrix, or edge list, and which one to reach for under time/space constraints.
- [overview] Three ways to represent the same graph
- [concept] Adjacency lists: the default for sparse graphs
- [concept] Adjacency matrices: O(1) edge lookup at O(V²) space
- [concept] Edge lists: the flattest representation, built for sorting edges
- [diagram] One graph, three representations side by side
- [code] Building a weighted adjacency list from a list of edges
- [compare] List vs matrix vs edge list on space, edge-lookup, and iteration cost
- [concept] Directed vs undirected: one entry per edge, or two
- [concept] Grids and implicit graphs: when there's no adjacency list at all
- [pitfall] Defaulting to a matrix and blowing the memory budget on a sparse graph
- [pitfall] Forgetting to store both directions for an undirected edge

### Topic: Graph Traversal — BFS & DFS (graph-traversal-bfs-dfs, beginner)
The two fundamental ways to visit every reachable node, and the different guarantees each one gives you.
- [overview] Two ways to explore a graph, and what each one guarantees
- [concept] BFS: level-by-level exploration with a queue
- [code] BFS with a visited set and a queue
- [concept] DFS: going deep first, with a stack or recursion
- [code] DFS — recursive and iterative versions
- [diagram] BFS's frontier vs DFS's recursion stack, on the same graph
- [concept] Why BFS finds shortest paths in unweighted graphs and DFS doesn't
- [concept] Multi-source BFS: flooding outward from many starting points at once
- [compare] BFS vs DFS — memory use, path guarantees, and when each wins
- [pitfall] Reaching for DFS to find a "shortest path" in an unweighted graph
- [pitfall] Recursive DFS stack overflow on a long chain or deep graph
- [pitfall] Marking a node visited on dequeue instead of on enqueue in BFS

### Topic: Connected Components & Bipartite Graphs (connected-components-bipartite, beginner)
Using BFS/DFS to partition a graph into connected pieces and to test whether it can be legally 2-colored.
- [overview] Two classic traversal applications: counting islands and 2-coloring a graph
- [concept] Connected components: one traversal launched per unvisited node
- [code] Counting connected components with iterative DFS
- [concept] Bipartite check: can you 2-color it so no edge joins two same-colored nodes?
- [code] BFS-based bipartiteness check with a color array
- [diagram] A bipartite graph vs a non-bipartite graph — where the coloring collides
- [concept] Why bipartiteness is exactly "no odd-length cycle"
- [compare] DFS/BFS components vs Union-Find components — same answer, different bookkeeping
- [compare] "Connected" on a directed graph vs an undirected graph — not the same claim
- [pitfall] Checking bipartiteness once and forgetting to restart from every unvisited component
- [pitfall] Calling a directed graph "connected" because one specific node can reach everything

### Topic: Union-Find (Disjoint Set Union) (union-find, intermediate)
A near-constant-time structure for tracking which nodes belong to the same group as edges are added.
- [overview] A data structure built for one question: are these two in the same group?
- [concept] The naive version: parent pointers and a find that walks to the root
- [code] Basic Union-Find with find and union
- [concept] Union by rank/size: keeping the tree shallow on purpose
- [concept] Path compression: flattening the tree on every find
- [code] Union-Find with both optimizations combined
- [diagram] A tall unbalanced tree vs the flattened tree after path compression
- [concept] Why the combined complexity is "almost O(1)" — the inverse Ackermann function
- [compare] Union-Find vs BFS/DFS for connectivity — online/dynamic vs offline/static
- [concept] Detecting a cycle by checking "same set" before you union two nodes
- [concept] Kruskal's MST as Union-Find's headline application
- [pitfall] Unioning the taller tree under the shorter one — backwards, and it undoes the optimization
- [pitfall] Skipping path compression and getting O(n) find on a skewed chain

### Topic: Cycle Detection in Directed & Undirected Graphs (cycle-detection, intermediate)
Detecting a cycle correctly — which needs different bookkeeping in a directed graph than in an undirected one.
- [overview] Why "does this graph have a cycle" needs a different algorithm per graph type
- [concept] Undirected cycle detection: a visited neighbor that isn't your parent
- [code] DFS cycle check for undirected graphs with parent tracking
- [concept] Directed cycle detection: "visited" isn't enough, you need "on the current path"
- [concept] The three-color (white/gray/black) method for directed graphs
- [code] DFS cycle check for directed graphs using a recursion-stack marker
- [diagram] A back edge vs a cross edge in a directed DFS tree — only one means a cycle
- [concept] Union-Find as a second way to catch a cycle in an undirected graph
- [compare] Parent-tracking DFS vs Union-Find for undirected cycle detection
- [concept] Topological sort's leftover nodes as a directed-cycle detector
- [pitfall] Reusing the undirected "skip the parent" trick on a directed graph
- [pitfall] Treating any revisited node as a cycle instead of checking if it's still on the stack

### Topic: Topological Sort — Kahn's & DFS-Based (topological-sort, intermediate)
Producing a valid dependency order over a DAG, and detecting when no such order exists.
- [overview] Ordering tasks so every dependency comes before its dependents
- [concept] What a topological order actually guarantees — and what it doesn't
- [concept] Kahn's algorithm: peel off zero-in-degree nodes, layer by layer
- [code] Kahn's algorithm with a queue and an in-degree array
- [concept] DFS-based topological sort: post-order, then reverse
- [code] DFS-based topological sort implementation
- [diagram] Kahn's in-degree layers vs DFS finishing times reversed, on the same DAG
- [concept] Why reversing DFS post-order produces a valid topological order
- [compare] Kahn's vs DFS-based — which one also flags a cycle, which gives all valid orders
- [concept] Detecting a cycle for free: leftover nodes in Kahn's, a gray node in DFS
- [concept] Where it actually shows up: build systems, course prerequisites, task scheduling
- [pitfall] Assuming a topological order is unique
- [pitfall] Running topological sort without checking for a cycle first

### Topic: Dijkstra's Algorithm & Single-Source Shortest Paths (dijkstra-shortest-paths, intermediate)
Computing shortest paths from a single source when all edge weights are non-negative.
- [overview] Shortest paths from one source, when every edge cost is non-negative
- [concept] The greedy idea: always finalize the closest unvisited node next
- [code] Dijkstra's algorithm with a min-heap
- [diagram] Dijkstra's frontier expanding outward, finalizing nodes in distance order
- [concept] Why the greedy choice is safe — the non-negative-weight proof sketch
- [concept] Lazy deletion: why the same node can enter the heap more than once
- [code] Reconstructing the actual shortest path, not just its length
- [compare] Binary heap vs plain array — O((V+E) log V) vs O(V²)
- [concept] 0-1 BFS as a deque-based shortcut when weights are only 0 or 1
- [pitfall] Running Dijkstra on a graph with a negative edge and trusting the answer
- [pitfall] Re-relaxing a node that was already popped off the heap with a stale distance

### Topic: Negative Weights & All-Pairs — Bellman-Ford & Floyd-Warshall (bellman-ford-floyd-warshall, advanced)
Handling shortest paths when edges can be negative, and computing every pair's distance at once.
- [overview] Two problems Dijkstra can't solve: negative edges, and every-pair distances
- [concept] Bellman-Ford: relax every edge, V-1 times, guaranteed
- [code] Bellman-Ford with early termination
- [concept] The V-th round trick: how Bellman-Ford flags a negative cycle
- [diagram] Relaxation distances converging over rounds on a graph with a negative edge
- [concept] Floyd-Warshall: routing every pair through every possible intermediate node
- [code] Floyd-Warshall's triple loop and its DP formulation
- [diagram] The "via k" DP — building all-pairs distances one intermediate node at a time
- [compare] Dijkstra vs Bellman-Ford vs Floyd-Warshall — weight limits, single vs all pairs, complexity
- [concept] Why a negative cycle makes "shortest path" undefined in the first place
- [pitfall] Stopping Bellman-Ford at V-1 rounds without the extra check, missing a negative cycle
- [pitfall] Reaching for Floyd-Warshall's O(V³) on a large sparse graph instead of repeated Dijkstra

### Topic: Minimum Spanning Trees — Kruskal & Prim (minimum-spanning-trees, intermediate)
Connecting every node at minimum total edge cost, via two different greedy constructions.
- [overview] Connecting every node as cheaply as possible, with no cycles
- [concept] What makes a spanning tree "minimum" — and why greedy works here (the cut property)
- [concept] Kruskal's algorithm: sort edges, add the cheapest one that doesn't close a cycle
- [code] Kruskal's algorithm using Union-Find to reject cycle-forming edges
- [concept] Prim's algorithm: grow one tree outward, always by the cheapest frontier edge
- [code] Prim's algorithm with a min-heap
- [diagram] Kruskal picking edges globally by weight vs Prim growing a single connected blob
- [compare] Kruskal vs Prim — dense vs sparse graphs, and which data structure each leans on
- [concept] Why an MST is not the same as a shortest-path tree
- [concept] MST uniqueness — when tied edge weights allow more than one valid MST
- [pitfall] Assuming the MST minimizes the path between two specific nodes
- [pitfall] Picking Prim on a sparse graph or Kruskal on a dense one and paying an avoidable log factor

**Cross-links:** `heaps` (priority-queue mechanics behind Dijkstra's and Prim's min-heaps), `sorting-searching` (the edge sort inside Kruskal's algorithm), `dynamic-programming` (Floyd-Warshall's DP recurrence, and DP-on-DAG using topological order).

## Group: Sorting & Searching (sorting-searching)

### Topic: Merge Sort & Divide-and-Conquer Sorting (merge-sort, beginner)
The divide-and-conquer sort that guarantees O(n log n) and stability at the cost of extra memory.
- [overview] Sorting by splitting in half, sorting each half, and merging
- [concept] The merge step: combining two sorted halves in linear time
- [code] Merge sort — recursive divide plus merge
- [diagram] The recursion tree — log n levels, each doing O(n) work
- [concept] Why merge sort is O(n log n) even in the worst case
- [concept] Stability: merge sort preserves the relative order of equal keys
- [concept] Merge sort on linked lists: no random access needed, so it's the natural fit
- [concept] External sorting: merging chunks too large to fit in memory
- [compare] Top-down (recursive) vs bottom-up (iterative) merge sort
- [pitfall] Merging in place naively and overwriting data you haven't read yet
- [pitfall] Forgetting merge sort's O(n) auxiliary space when the problem demands O(1) extra

### Topic: Quicksort & Partitioning Schemes (quicksort-partitioning, intermediate)
The in-place divide-and-conquer sort built around picking a pivot, and the two classic ways to partition around it.
- [overview] Sorting by picking a pivot and partitioning the array around it
- [concept] The Lomuto partition scheme, step by step
- [code] Quicksort with Lomuto partitioning
- [concept] The Hoare partition scheme — why it does fewer swaps
- [code] Quicksort with Hoare partitioning
- [diagram] Lomuto vs Hoare partitioning the same array — where the pointers end up
- [concept] Picking a pivot: first/last element, median-of-three, or random
- [concept] Why a sorted (or reverse-sorted) input triggers the O(n²) worst case
- [concept] Randomized pivots: turning a worst case into an astronomically unlikely one
- [compare] Lomuto vs Hoare — swap count, duplicate handling, index semantics
- [concept] Recursing on the smaller half first to cap recursion depth at O(log n)
- [pitfall] Mixing Lomuto-style logic with a Hoare-style partition index
- [pitfall] Trusting a fixed first-element pivot without guarding against sorted input

### Topic: Comparing the Classic Sorts & the Ω(n log n) Lower Bound (comparing-classic-sorts, intermediate)
Weighing merge sort, quicksort, and heapsort against each other, and why no comparison sort can beat n log n.
- [overview] Merge sort, quicksort, and heapsort all cost O(n log n) — so how do you choose?
- [concept] Stability: why merge sort preserves equal-key order and quicksort/heapsort don't
- [concept] In-place vs extra memory: O(1)/O(log n) space for quicksort/heapsort vs O(n) for merge sort
- [diagram] Best/average/worst-case complexity across the three sorts, side by side
- [compare] Merge sort vs quicksort vs heapsort — stability, space, cache behavior, worst case
- [concept] Why comparison sorting can't beat Ω(n log n) — the decision-tree argument
- [concept] Cache behavior and constant factors: why quicksort usually beats merge sort in practice
- [concept] What production languages actually run — Python/Java's Timsort vs C++'s introsort
- [concept] Heapsort's real niche: in-place and worst-case-safe, rarely the practical default (see `heaps`)
- [pitfall] Picking a sort by Big-O alone and ignoring its stability guarantee
- [pitfall] Assuming "in-place" means zero extra memory anywhere, including the call stack

### Topic: Non-Comparison Sorts — Counting, Radix & Bucket (non-comparison-sorts, intermediate)
Sorting in linear time by exploiting structure in the keys instead of comparing them.
- [overview] Beating O(n log n) by not comparing elements at all
- [concept] Counting sort: tallying exact key frequencies when the key range is small
- [code] Counting sort, including the stable prefix-sum version
- [concept] Why counting sort costs O(n + k) — and why it's useless when k >> n
- [concept] Radix sort: sorting digit by digit using a stable sort as the subroutine
- [code] LSD radix sort implementation
- [diagram] Radix sort's passes over the digits, least-significant to most-significant
- [concept] Bucket sort: scattering into ranges, sorting each bucket, concatenating
- [compare] Counting vs radix vs bucket — what key property each one exploits
- [compare] When a comparison sort still wins over a non-comparison one
- [pitfall] Applying counting sort to a key range far larger than n
- [pitfall] Forgetting that each radix pass must be a stable sort, or the final order breaks

### Topic: Binary Search Fundamentals (binary-search-fundamentals, beginner)
The core loop invariant behind binary search and the boundary-search templates built on top of it.
- [overview] Halving the search space every step, in a sorted array
- [concept] The invariant: what stays true about the search window every iteration
- [code] The plain "does it exist" binary search template
- [diagram] The search window shrinking step by step until it collapses
- [concept] lower_bound and upper_bound: searching for a boundary, not just a match
- [code] lower_bound / upper_bound implementation
- [concept] Why `lo + (hi - lo) / 2` beats `(lo + hi) / 2` — the overflow bug
- [compare] Inclusive `[lo, hi]` vs half-open `[lo, hi)` loop templates
- [concept] Why O(log n) actually matters once n gets into the millions
- [pitfall] Off-by-one errors from mixing `<` and `<=` with the wrong bounds convention
- [pitfall] Running binary search on data that isn't sorted by the key you're searching on

### Topic: Binary Search Variants — First/Last Occurrence & Rotated Arrays (binary-search-variants, intermediate)
Applying the binary search invariant to arrays with duplicates and to rotated sorted arrays.
- [overview] The same invariant, aimed at trickier targets
- [concept] Finding the first occurrence of a target among duplicates
- [concept] Finding the last occurrence — the mirror-image condition
- [code] First-and-last-occurrence binary search (the "search for range" pattern)
- [concept] Searching a rotated sorted array: one half is always properly sorted
- [code] Binary search on a rotated sorted array
- [diagram] A rotated array split at the pivot — spotting which half is sorted
- [concept] Finding the rotation point (the minimum) as its own binary search
- [concept] Handling duplicates in a rotated array, when you can't tell which half is sorted
- [compare] Rotated-array search vs plain binary search — what changes at each step
- [pitfall] Assuming the left half is always the sorted half
- [pitfall] Applying no-duplicate rotated-search logic to data that has duplicates

### Topic: Searching in 2D Matrices (searching-2d-matrices, intermediate)
Extending binary search and elimination search into two dimensions.
- [overview] Extending binary search into two dimensions
- [concept] The fully-sorted matrix: flatten to 1D and binary search by index mapping
- [code] Binary search on a fully sorted matrix via row/col index mapping
- [concept] The row-and-column-sorted matrix: why flattening no longer works
- [code] Staircase search starting from the top-right corner
- [diagram] The staircase search's path — eliminating a row or a column on every step
- [concept] Why staircase search costs O(m + n), not O(log(mn))
- [compare] Fully-sorted-matrix binary search vs staircase search — which structure each assumes
- [concept] Binary search on the answer, applied to a matrix: the k-th smallest element
- [pitfall] Using flattened-array binary search on a matrix that isn't fully sorted
- [pitfall] Starting the staircase search from a corner that can't eliminate cleanly

### Topic: Binary Search on the Answer (binary-search-on-answer, advanced)
Binary searching over a range of possible answers instead of over an array, using a monotonic feasibility check.
- [overview] Binary search without an array — searching a range of possible answers
- [concept] The pattern: a monotonic "is this answer feasible?" predicate
- [concept] Recognizing the signal: "minimize the maximum" / "maximize the minimum" phrasing
- [code] Binary search on the answer: minimum eating speed to finish in time
- [diagram] The feasible/infeasible split across the answer range
- [code] Binary search on the answer: minimum capacity to ship within a deadline
- [concept] Setting the search bounds so the true answer is provably inside [lo, hi]
- [compare] Binary search on the answer vs a pure greedy/simulation sweep
- [concept] Binary search on real numbers: stopping by precision instead of exact convergence
- [pitfall] Applying this pattern when the feasibility predicate isn't actually monotonic
- [pitfall] An off-by-one in the feasibility check that returns a feasible but non-optimal answer

**Cross-links:** `heaps` (heapsort's internals), `arrays-strings` (general in-place array manipulation), `two-pointers-sliding-window` (two-pointer partitioning framed as a window pattern), `greedy` (the feasibility checks inside binary-search-on-the-answer problems are often greedy simulations).

## Group: Recursion & Backtracking (recursion-backtracking)

### Topic: Recursion Fundamentals (recursion-fundamentals, beginner)
How recursive calls execute on the call stack, how to design correct base and recursive cases, and when to convert recursion to an explicit iterative form.
- [overview] Recursion: solving a problem by solving a smaller version of itself
- [diagram] The call stack — how each recursive call pushes and pops a stack frame
- [concept] Base case first: designing the case that stops the recursion before the case that shrinks toward it
- [diagram] Tracing execution with a recursion tree, call by call
- [pitfall] The silent bug: a base case that's never reached, and the stack overflow it eventually causes
- [code] Naive recursive Fibonacci and the exponential blow-up from recomputing the same call
- [pitfall] Overlapping subproblems (like naive Fibonacci) are the tell for memoization, not just cleaner recursion
- [concept] Tail-recursive form, and why most mainstream languages still grow the stack anyway
- [code] Rewriting a recursive function iteratively with an explicit stack
- [pitfall] Treating recursion as free — the O(depth) stack space nobody budgets for
- [compare] Recursion vs. an explicit loop for the same logic: when each actually wins

### Topic: The Backtracking Framework (backtracking-framework, beginner)
The general choose-explore-unexplore template underlying every backtracking problem, and how pruning changes its cost in practice.
- [overview] Backtracking: exhaustively searching a decision tree, undoing each choice that doesn't pan out
- [diagram] The decision tree of choices, with dead branches pruned early
- [concept] The three-step template: choose a candidate, explore deeper, unexplore (undo) before the next candidate
- [code] The generic backtracking skeleton you adapt for permutations, subsets, or board search
- [pitfall] Forgetting the "unexplore" step and corrupting state for every sibling branch
- [concept] Pruning: cutting a branch the instant a partial choice can't lead to a valid answer
- [compare] Brute-force enumeration vs. backtracking with pruning over the same search space
- [concept] Why backtracking's cost is branching-factor^depth, and how one good prune reshapes it
- [pitfall] Pruning too late — checking validity only at a full-depth leaf instead of at each partial state
- [compare] Copying state at each branch vs. mutating shared state and undoing it

### Topic: Generating Permutations (permutations, intermediate)
Generating every ordering of a set via backtracking, handling duplicate elements, and the in-place-swap vs. used-set implementation trade-off.
- [concept] Building each permutation one position at a time, backtracking when a position runs out of choices
- [code] The used-set approach: tracking which elements are already placed in the current path
- [code] The in-place swap approach: swapping an element into position and swapping back after
- [compare] Used-set vs. in-place swapping — extra space vs. mutating the input array
- [concept] Handling duplicate elements: sort first, then skip a duplicate at the same tree depth
- [pitfall] Skipping duplicates at the wrong level and silently dropping valid permutations
- [diagram] The permutation decision tree for a 3-element input, branch by branch
- [concept] Why the count is n!, and what that means for the largest n you can brute-force
- [compare] Generating all permutations vs. finding the next lexicographic permutation — different algorithms entirely
- [pitfall] The k-th permutation problem doesn't need generating all permutations — it has a direct combinatorial shortcut

### Topic: Generating Subsets & the Power Set (subsets-power-set, intermediate)
Generating every subset of a set via the include/exclude recursion tree, handling duplicates, and relating it to the power set's 2^n size.
- [concept] Each element gets an include/exclude choice — the recursion tree has depth n and 2^n leaves
- [code] Backtracking template for subsets: add the element, recurse, remove it
- [diagram] The include/exclude decision tree for a 3-element set, all 8 subsets as leaves
- [concept] Building subsets incrementally with a "start index" instead of paired include/exclude calls
- [concept] Handling duplicate elements: sort first, then skip a repeated value at the same tree level
- [pitfall] Confusing "skip duplicates at the same level" with "skip duplicates anywhere" and losing valid subsets
- [compare] Generating subsets by recursion vs. iterating 0..2^n−1 and reading off the bits
- [concept] Why the answer size is always 2^n, regardless of which generation strategy you pick
- [pitfall] Adding a reference to the mutating working list instead of a copy, so every "subset" ends up empty

### Topic: Generating Combinations & Combination Sum (combinations-combination-sum, intermediate)
Choosing a fixed-size or target-sum group from a set where order doesn't matter, and the pruning that makes the search tractable.
- [concept] Combinations vs. permutations: order doesn't matter, so the search only ever moves forward
- [code] Backtracking template for "choose k of n" using a strictly increasing start index
- [concept] Pruning when the remaining elements can't possibly fill out the needed count
- [code] Combination Sum: reusing an element by not advancing the index on that recursive call
- [concept] Combination Sum II: no reuse allowed, but same-level duplicate-skipping still applies
- [pitfall] Re-deriving the same combination in a different order because the start index wasn't advanced
- [diagram] The pruned decision tree for Combination Sum once a partial sum exceeds the target
- [compare] Combinations (fixed size k) vs. subsets (any size) — same engine, different stopping rule
- [concept] Sorting the input first so duplicate-skipping and sum-based pruning both become possible

### Topic: Word Search & Grid Backtracking (word-search-grid-backtracking, intermediate)
DFS-with-backtracking over a 2D grid to match a path against a target word, including the mark-and-restore pattern on visited cells.
- [concept] Treating the grid as a graph of neighbors, and backtracking one matched character at a time
- [code] Marking a cell visited before recursing and restoring it right after — the grid's "unexplore" step
- [pitfall] Using a separate visited set instead of marking in place, and the extra memory that costs per call
- [concept] Pruning the instant the next character on the path doesn't match the target word
- [diagram] The search tree from one starting cell, dead ends pruned as soon as a letter mismatches
- [concept] Trying every cell as a start point, and why that dominates the overall complexity
- [compare] Searching for one word vs. many words at once, where a shared trie prunes far more
- [pitfall] Forgetting grid-boundary checks and reading past the edge of the board
- [concept] Complexity in terms of rows × cols × 4^(word length), and why long words prune fast in practice

### Topic: N-Queens & Board Backtracking (n-queens, advanced)
Placing N non-attacking queens via backtracking, tracking column and diagonal conflicts in O(1) instead of rescanning the board.
- [concept] Placing one queen per row so the search only ever needs to check earlier rows
- [code] Backtracking template: try each column in the current row, place, recurse, remove
- [concept] Tracking used columns and both diagonal directions with sets instead of rescanning the board
- [diagram] Why a cell's diagonal is identified by row−col in one direction and row+col in the other
- [pitfall] Rescanning the whole board for conflicts on every placement instead of maintaining conflict sets
- [concept] Pruning a row the moment every column in it is already blocked
- [compare] Counting all solutions vs. returning the first valid board — same search, different stopping condition
- [diagram] The pruned search tree for N=4, showing exactly where invalid branches die
- [concept] Why solution count grows much faster than N despite the row-by-row pruning

### Topic: Sudoku Solver & Constraint Satisfaction (sudoku-solver-csp, advanced)
Solving Sudoku as a constraint-satisfaction backtracking search, and the ordering heuristics that keep it fast in practice.
- [concept] Framing Sudoku as a CSP: variables (empty cells), domains (1–9), constraints (row/col/box uniqueness)
- [code] Backtracking template: find an empty cell, try each legal digit, place, recurse, remove
- [concept] Precomputing row/column/box constraint sets so a legality check is O(1), not a rescan
- [pitfall] Always picking the first empty cell instead of the most-constrained one, multiplying the search space
- [concept] The minimum-remaining-values heuristic: filling the cell with the fewest legal digits first
- [diagram] How placing one digit shrinks the candidate sets of every peer cell in its row, column, and box
- [compare] Plain backtracking vs. backtracking with constraint propagation (eliminating candidates as you place)
- [pitfall] Re-validating the whole board on every placement instead of only the row/col/box that changed
- [concept] Generalizing the pattern: any CSP (map coloring, cryptarithmetic) fits the same choose/check/undo shape

**Cross-links:** `dynamic-programming` (the backtracking-vs-DP compare and the memoization fix for overlapping subproblems live there), `bit-manipulation` (bitmask subset-iteration mechanics), `tries-strings` (trie-pruned multi-word grid search), `trees-bst` / `graphs` (general tree/graph traversal mechanics, owned there), `math-number-theory` (k-th-permutation combinatorial shortcut).

## Group: Dynamic Programming (dynamic-programming)

### Topic: DP Fundamentals: Memoization vs. Tabulation (dp-fundamentals, beginner)
Recognizing when a problem has overlapping subproblems and optimal substructure, and the two equivalent ways to exploit that: memoization and tabulation.
- [overview] Dynamic programming: solving each distinct subproblem once and reusing the answer
- [concept] The two ingredients a problem needs: overlapping subproblems and optimal substructure
- [diagram] The recursion tree for naive Fibonacci, with repeated subtrees highlighted
- [compare] Top-down memoization vs. bottom-up tabulation — same subproblems, opposite traversal order
- [code] Adding a memo dictionary to a naive recursive solution — the minimal top-down conversion
- [code] Rewriting the same problem bottom-up with a table filled in dependency order
- [concept] Defining the state: what a DP problem's "state" is, and why choosing it correctly is most of the work
- [concept] Writing the recurrence: expressing a state's answer in terms of smaller states' answers
- [pitfall] A recurrence that's technically correct but has no valid fill order, because of a dependency cycle
- [concept] Space optimization: collapsing a table to the last one or two rows when the recurrence only looks back that far
- [pitfall] Memoizing a function whose "state" isn't really just its arguments — hidden mutable state breaks the cache
- [compare] Backtracking's exhaustive enumeration vs. DP's reuse of overlapping subproblems
- [concept] Reconstructing the actual chosen path or answer, not just the optimal value, by remembering choices

### Topic: 1D DP: Climbing Stairs & House Robber (dp-1d-sequences, beginner)
The simplest DP shape — a 1D table indexed by position — via Climbing Stairs and the House Robber family of skip-or-take problems.
- [concept] The 1D DP shape: dp[i] depends on just a few earlier dp[j] with j < i
- [code] Climbing Stairs: dp[i] = dp[i-1] + dp[i-2], Fibonacci in disguise
- [diagram] Filling the dp array left to right, showing which earlier cells each step reads
- [concept] House Robber: the take-or-skip choice at each house and its recurrence
- [pitfall] Being greedy about "skip every other house" instead of computing the real optimum
- [concept] House Robber II: houses in a circle, solved as two linear runs with different exclusions
- [compare] Top-down memoized recursion vs. the rolling-variable bottom-up version of the same recurrence
- [concept] Space-optimizing to two rolling variables instead of a full array
- [pitfall] Off-by-one base cases (dp[0], dp[1]) that silently corrupt every later cell
- [concept] Generalizing the pattern: "decide at position i from a fixed window of earlier positions"

### Topic: 0/1 & Unbounded Knapsack (knapsack, intermediate)
0/1 and unbounded knapsack: the take-or-leave-it recurrence over a weight-capacity axis, and the reference case for reasoning about DP state design.
- [concept] The state: (item index, remaining capacity) and the take-or-skip recurrence over it
- [diagram] The 2D dp table for 0/1 knapsack — rows as items, columns as capacity
- [code] Bottom-up 0/1 knapsack, filling the table while iterating capacity downward per item
- [pitfall] Iterating capacity forward in the 1D-optimized version and reusing an item twice by accident
- [concept] Unbounded knapsack: why iterating capacity forward is exactly correct once reuse is allowed
- [compare] 0/1 knapsack vs. unbounded knapsack — one iteration-direction change, opposite reuse semantics
- [concept] Space-optimizing the 2D table down to a single 1D array over capacity
- [compare] 0/1 Knapsack (needs DP) vs. Fractional Knapsack (greedy suffices) — what divisibility buys you
- [concept] Subset-sum and partition-equal-subset as knapsack with a boolean "is this capacity reachable" table
- [pitfall] Treating every "pick a subset under a constraint" problem as knapsack when reuse or order rules differ
- [concept] Reconstructing which items were chosen by walking back through the filled table

### Topic: Longest Increasing Subsequence (lis, intermediate)
Longest Increasing Subsequence from the O(n²) DP recurrence to the O(n log n) patience-sorting / binary-search optimization.
- [concept] The O(n²) recurrence: dp[i] as the longest chain ending exactly at index i
- [code] Filling dp[i] by scanning all earlier j and extending the best valid chain
- [pitfall] Confusing dp[i] ("ending at i") with "the LIS length using the first i elements" — a different recurrence
- [diagram] The chain of "ending at index i" pointers that reconstructs the actual subsequence
- [concept] The patience-sorting idea: piles where each pile's top card is the smallest tail of a chain that length
- [diagram] Dealing cards onto patience-sorting piles, where the final pile count equals the LIS length
- [code] Replacing the linear scan with binary search over pile tops for O(n log n)
- [pitfall] Reading the tails array's final length as the actual subsequence instead of just its length
- [compare] The O(n²) DP vs. the O(n log n) patience-sorting version — same answer, different state representation
- [concept] Variants this extends to: longest non-decreasing chain, and Russian-doll envelopes as 2D LIS after sorting

### Topic: Longest Common Subsequence & Edit Distance (lcs-edit-distance, intermediate)
Longest Common Subsequence and Edit Distance as the canonical 2D string DP, aligning two sequences cell by cell.
- [concept] The 2D state: dp[i][j] as the answer using the first i characters of one string and first j of the other
- [diagram] The LCS grid: matching characters step diagonally, mismatches take the best neighbor
- [code] Filling the LCS table bottom-up and reading the answer from the final cell
- [concept] Reconstructing the actual common subsequence by walking back through the filled table
- [concept] Edit Distance's three moves — insert, delete, replace — as three neighboring cells in the same grid
- [diagram] The Edit Distance grid, showing which of the three neighbors each cell's minimum comes from
- [compare] LCS vs. Edit Distance — nearly the same table shape, a different recurrence and a different question
- [pitfall] Off-by-one indexing between the 0-indexed string and the 1-indexed dp table with its empty-prefix row/column
- [concept] Space-optimizing to two rows, since each cell only ever needs the row above and the row so far
- [concept] The same grid underneath: longest palindromic subsequence as LCS of a string with its own reverse
- [pitfall] Assuming LCS returns a contiguous run — it doesn't; that's the different problem of longest common substring

### Topic: Interval DP: Matrix Chain & Burst Balloons (interval-dp, advanced)
DP over subranges of a sequence, choosing a split point or last operation within each interval, via Matrix Chain Multiplication and Burst Balloons.
- [concept] The state: dp[i][j] as the best answer over the subrange from i to j, built from smaller subranges inside it
- [concept] Why interval DP always iterates by increasing interval length, not by row or column alone
- [code] Matrix Chain Multiplication: trying every split point k and taking the cheapest parenthesization
- [diagram] The dp table filled by diagonals, each diagonal representing one interval length
- [concept] Burst Balloons: treating the *last* balloon burst in a range as the split, not the first
- [pitfall] Picking the "first choice made" as the split point when the recurrence actually needs the "last choice made"
- [compare] Matrix Chain's split-point recurrence vs. Burst Balloons' last-action recurrence — same shape, opposite direction of reasoning
- [concept] Complexity: O(n³) from n² intervals times an O(n) split search, and why that's usually the ceiling here
- [concept] Reconstructing the optimal split or order by remembering the best k at each interval
- [pitfall] Off-by-one errors in interval bounds (inclusive vs. exclusive) that silently skip valid splits

### Topic: State-Machine DP: The Buy/Sell Stock Family (state-machine-stock-dp, intermediate)
The Buy/Sell Stock family as DP over explicit holding/not-holding states, extended to cooldowns, fees, and a bounded transaction count.
- [concept] Modeling each day as a small state machine: holding a share or not, and the transitions between them
- [diagram] The two-state transition diagram: hold, sell, buy, rest, and which recurrence updates which
- [code] Buy/Sell Stock with one transaction, as a running-minimum-so-far scan
- [code] Unlimited transactions: summing every profitable up-move in one pass
- [compare] One transaction vs. unlimited transactions — why the unlimited case collapses to a greedy scan
- [concept] Adding a cooldown state after selling, and how it changes which transition feeds "holding"
- [code] Adding a flat transaction fee, and where in the recurrence it gets subtracted
- [concept] At-most-k-transactions: adding a transaction-count dimension to the state
- [diagram] The 2D state grid (day × transactions-used) for the k-transaction version
- [pitfall] Reusing the unlimited-transactions greedy shortcut on a variant where it no longer holds
- [concept] Space-optimizing the whole family to a handful of rolling variables instead of a table

### Topic: Bitmask DP: State as a Subset (bitmask-dp, advanced)
DP where the state is a subset of a small universe encoded as bits, via Held-Karp TSP and worker-task assignment problems.
- [concept] Using an integer's bits as a "which elements are used so far" state, viable when n is roughly ≤ 20
- [concept] The state: (bitmask of visited/used elements, current position) and what it lets you reuse
- [code] Held-Karp: the DP recurrence for Traveling Salesman over (mask, last city)
- [diagram] How a bitmask transitions when one more element gets included, bit by bit
- [concept] Iterating masks in increasing numeric order guarantees every submask is already computed
- [pitfall] Reaching for bitmask DP when n is too large, so the state space explodes past feasibility
- [concept] Assignment-style problems: matching n workers to n tasks via a mask of "tasks already assigned"
- [compare] Bitmask DP's state-as-subset vs. plain subset-enumeration backtracking over the same universe
- [concept] Enumerating submasks of a mask efficiently, and why that shows up inside bitmask-DP transitions
- [pitfall] Forgetting that mask 0 (nothing chosen yet) needs its own explicit base case

### Topic: DP on Trees: Combining Children's Answers (dp-on-trees, advanced)
DP over a tree's recursive structure — combining children's answers at each node — via House Robber III and diameter/max-path-sum problems.
- [concept] DP on trees: computing each node's answer from its children's answers via post-order traversal
- [concept] House Robber III: each node returns a pair (best-if-robbed, best-if-not-robbed) to its parent
- [code] The post-order recursion combining a node's pair from its two children's pairs
- [diagram] The combine step at one node: how a parent's two values are built from its children's four values
- [concept] Diameter of a tree as a DP quantity: each node returns its height while a global max tracks the best path through it
- [pitfall] Conflating "what a node returns to its parent" with "the final answer," missing paths that pass through a node without ending there
- [compare] Returning a single value per node vs. returning a small tuple of states per node
- [concept] Binary Tree Maximum Path Sum as the same "return vs. update global best" pattern, now with negative values in play
- [pitfall] Letting a negative-sum child contribute to the parent's chain instead of clamping it to zero
- [concept] Why this is still an ordinary post-order traversal underneath, just with a richer return value

**Cross-links:** `recursion-backtracking` (the backtracking-vs-DP compare lives here; bitmask DP's subset-enumeration counterpart), `greedy` (fractional-knapsack exchange-argument proof; general greedy-vs-DP framing), `bit-manipulation` (bitmask mechanics used by bitmask DP), `trees-bst` (post-order traversal mechanics under tree DP), `graphs` (DAG longest/shortest-path DP, Floyd-Warshall), `intervals` (a different pattern — greedy/sweep-line over literal ranges, not DP over subranges — despite the similar-sounding name).

## Group: Greedy (greedy)

### Topic: Greedy Fundamentals — What Greedy Assumes and Where It Breaks (greedy-fundamentals, beginner)
What a greedy algorithm actually assumes, and the classic counterexample that shows a plausible-looking greedy strategy can still be wrong.
- [overview] Greedy algorithms: committing to the locally best choice at every step
- [concept] The two ingredients a problem needs: the greedy-choice property and optimal substructure
- [pitfall] The coin-change trap: greedy fails to make 6 optimally with denominations {1, 3, 4}
- [concept] Why a greedy strategy that "looks right" still isn't proven until you show it
- [diagram] A greedy choice sequence versus the full decision tree it prunes away
- [pitfall] Defaulting to "sort, then scan" without checking that the exchange still holds
- [concept] Recognizing greedy-shaped cues in a problem statement: "maximum count", "non-overlapping", "earliest/latest"

### Topic: Activity Selection — Maximizing Non-Overlapping Intervals (activity-selection, beginner)
The canonical greedy problem — picking the maximum number of non-overlapping activities by always taking the one that finishes earliest.
- [overview] Activity selection: choosing the largest possible set of non-overlapping activities
- [concept] Why sorting by finish time — not start time, not duration — is the correct greedy key
- [diagram] Walking the sorted timeline: accept, skip, accept, as the pointer advances
- [code] Earliest-finish-time greedy in a single pass after sorting
- [pitfall] Sorting by start time or by interval length instead of finish time
- [compare] Maximizing count (activity selection) versus minimizing rooms (meeting rooms) — different objectives, different techniques
- [concept] Complexity: O(n log n) from the sort; the scan itself is O(n)
- [pitfall] Getting the overlap boundary wrong — is an activity ending exactly when the next starts a conflict?

### Topic: Proving Greedy Correct — The Exchange Argument (exchange-argument, intermediate)
The general proof technique for showing a greedy choice is safe to make, worked through on interval scheduling.
- [overview] The exchange argument: the standard technique for proving a greedy choice is safe
- [concept] Step one — assume an optimal solution that disagrees with the greedy choice at some point
- [concept] Step two — show swapping in the greedy choice cannot make that solution worse
- [diagram] Exchanging one interval for another inside an optimal schedule without losing count
- [code] Applying the exchange argument to activity selection: earliest finish time is always safe to swap in
- [concept] Optimal substructure: why the remaining subproblem is the same problem, just smaller
- [compare] Exchange argument versus a "stays-ahead" proof — two different templates for proving greedy correct
- [pitfall] A proof sketch that shows "a valid answer" but never shows "an optimal one"
- [concept] When no exchange argument presents itself — treat that as the signal to reach for DP instead

### Topic: Jump Game — Greedy Reachability, One Pass at a Time (jump-game, intermediate)
Greedy reachability tracking for Jump Game I and II, and why maximizing reach at each step is always safe.
- [overview] Jump Game: tracking the furthest reachable index in a single pass
- [concept] Maintaining "furthest reach so far" while scanning once, left to right
- [diagram] The reachable frontier expanding as the scan passes each index
- [code] Jump Game I: one-pass greedy feasibility check
- [code] Jump Game II: greedy level-by-level jump counting
- [compare] Jump Game II's greedy pass versus a DP-over-positions solution — same answer, different cost
- [pitfall] Confusing "maximize reach at each step" with "always take the single longest jump available"
- [concept] Why maximizing reach is always safe: reach is monotone, so keeping more options open never hurts

### Topic: Gas Station — The Single-Pass Circular Greedy (gas-station, intermediate)
The single-pass greedy for the circular gas-station problem, and the reset rule that makes one scan sufficient.
- [overview] Gas Station: finding the one starting point that completes a circular route
- [concept] Feasibility check first: a valid start exists only if total gas >= total cost
- [concept] The reset rule: if the tank runs dry, no station in the failed run could have worked as a start either
- [diagram] Running tank balance around the loop, resetting the candidate start on the first deficit
- [code] Single-pass greedy for the starting index
- [pitfall] Re-testing every candidate start from scratch — an O(n^2) habit this problem doesn't need
- [concept] Why the reset step is itself a compressed exchange argument
- [compare] Gas Station versus Jump Game: both track a running budget, but one resets and the other only grows

### Topic: Greedy vs Dynamic Programming — Telling Them Apart (greedy-vs-dp, intermediate)
How to tell, before you start coding, whether a problem needs greedy's single pass or DP's full search over choices.
- [overview] Greedy and DP both optimize over a sequence of choices — the difference is what happens after a choice
- [concept] The tell: can a local choice be revisited or undone later without extra cost?
- [diagram] Fractional knapsack (greedy by value/weight ratio) next to 0/1 knapsack (needs DP)
- [pitfall] Applying the fractional-knapsack ratio trick to the 0/1 version of the problem
- [compare] Signal checklist: single sortable criterion with no reuse of past choices points to greedy; overlapping subproblems with either/or decisions point to DP
- [concept] Greedy as a special case: when a DP recurrence collapses to "always take the locally best option"
- [pitfall] Trusting a greedy that merely passed the given examples — small tests rarely expose a wrong greedy
- [concept] Defending a greedy choice out loud in an interview: state the exchange argument, don't just assert correctness

### Topic: Huffman Coding — Greedy with a Min-Heap (huffman-coding, advanced)
Building an optimal prefix code by greedily merging the two rarest symbols with a min-heap.
- [overview] Huffman coding: building an optimal prefix code by always merging the two rarest symbols
- [concept] Why prefix-free codes let you decode without any delimiter
- [diagram] Building the Huffman tree bottom-up from a min-heap of symbol frequencies
- [code] Min-heap construction: repeatedly pop the two smallest, merge, push the sum
- [concept] The exchange argument for Huffman: the two rarest symbols can always be forced to the deepest level
- [compare] Huffman coding versus fixed-length codes: where the bit savings actually come from
- [concept] Complexity: O(n log n), driven by n-1 rounds of heap extract/insert
- [pitfall] Assuming a tie in frequencies changes optimality — it only changes which optimal tree you get

**Cross-links:** `intervals` (general merge/insert/overlap-counting mechanics beyond the greedy proof itself), `heaps` (heap operations underlying Huffman coding), `dynamic-programming` (full DP treatment contrasted in greedy-vs-dp, e.g. 0/1 knapsack).

## Group: Intervals & Sweep Line (intervals)

### Topic: Merge Intervals — Collapsing Overlapping Ranges (merge-intervals, beginner)
Collapsing a sorted list of ranges into their disjoint union in one linear pass.
- [overview] Merge Intervals: collapsing a list of ranges into their disjoint union
- [concept] Why sorting by start time first makes a single linear pass sufficient
- [diagram] Walking sorted intervals: extend the current merge, or close it and start a new one
- [code] Single-pass merge after sorting
- [pitfall] Comparing against the previous input interval instead of the last merged interval
- [pitfall] Getting the touching-boundary case wrong — does [1,2] and [2,3] count as overlapping?
- [concept] Complexity: O(n log n) from the sort; the merge pass itself is O(n)
- [compare] Merge Intervals versus Insert Interval: batch merging versus single-insertion merging

### Topic: Insert Interval — Single-Pass Insertion into a Sorted List (insert-interval, beginner)
Inserting a single new interval into an already-merged, sorted list without a full re-merge.
- [overview] Insert Interval: adding one new range into an already-merged, sorted list
- [concept] Three zones in a single pass: intervals fully before, intervals overlapping, intervals fully after
- [diagram] The new interval growing as it absorbs each overlapping neighbor
- [code] A single O(n) pass that builds the result without re-sorting
- [pitfall] Appending and re-running full Merge Intervals instead of exploiting the already-sorted input
- [pitfall] Forgetting to flush the remaining "after" intervals once the merge window closes
- [concept] Why this is O(n) while "append then merge-intervals" is O(n log n)

### Topic: Interval List Intersections — Two-Pointer Overlap Finding (interval-list-intersection, intermediate)
Two-pointer scanning across two independent sorted interval lists to find every overlap.
- [overview] Finding every overlap between two independent sorted interval lists
- [concept] Two-pointer scan: advance whichever list's current interval ends first
- [diagram] Both pointers stepping forward, emitting an intersection at each overlap
- [code] The two-pointer intersection pass
- [pitfall] Merging the two lists together first, losing track of which original interval each piece came from
- [concept] Why discarding the earlier-ending interval is always safe
- [compare] Intersecting two lists versus merging one list — a genuinely different pointer discipline
- [pitfall] Missing that an intersection can be a single point, depending on the problem's definition of overlap

### Topic: Meeting Rooms — Overlap Counting and Minimum Resources (meeting-rooms, intermediate)
Counting how many meetings are simultaneously active to determine feasibility and minimum rooms needed.
- [overview] Meeting Rooms: can one room host everything, and if not, how many are needed?
- [concept] Meeting Rooms I: sort and check whether any adjacent pair overlaps
- [concept] Meeting Rooms II: tracking concurrently active meetings, not just pairwise overlap
- [diagram] Separate sorted start/end arrays swept in lockstep to track concurrency
- [code] Two-pointer start/end sweep for the minimum room count
- [compare] Two-array two-pointer versus a min-heap of end times — two ways to track "what's still active"
- [pitfall] Counting a meeting ending at time t and one starting at time t as overlapping when they shouldn't be
- [compare] "Erase Overlap Intervals" reframes this data as a removal-count problem — greedy proof owned by `greedy`
- [concept] What peak concurrency physically means: the minimum rooms or resources required

### Topic: The Sweep Line Technique — Events, Sorting, and a Running Counter (sweep-line-technique, intermediate)
The general event-sweep pattern — turn ranges into start/end events, sort, and scan with a running counter.
- [overview] Sweep line: turning interval endpoints into events and scanning them in sorted order
- [concept] Encoding a range as a +1-at-start / -1-at-end pair of events
- [diagram] A timeline of events swept left to right with a running counter
- [code] The generic event-sweep template: build events, sort, scan, track running state
- [compare] Sweep line versus a nested-loop scan over every pair of intervals
- [pitfall] Sorting events by time only, with no tie-break rule for a start and end at the same instant
- [concept] Beyond intervals: sweep line applies to any "a range contributes to a running total" problem, like car pooling
- [compare] Sweep line versus a prefix-sum/difference-array approach on a bounded coordinate range

### Topic: The Skyline Problem — Sweep Line with a Max-Heap of Active Heights (skyline-problem, advanced)
Combining a sweep line with a max-heap of active heights to merge overlapping building outlines into one silhouette.
- [overview] Skyline: merging overlapping building outlines into a single silhouette
- [concept] Representing each building as a start-event (add height) and an end-event (remove height)
- [diagram] The sweep line crossing building edges while a max-heap tracks the tallest active building
- [code] Event sweep with a max-heap of active heights, emitting a key point on every change to the max
- [pitfall] A max-heap holding stale, already-ended heights that are never lazily removed
- [pitfall] Missing the tie-break rule for processing simultaneous start and end events
- [concept] Why a key point is emitted only when the current max height actually changes
- [concept] Complexity: O(n log n) from sorting events plus heap operations
- [compare] Skyline versus Meeting Rooms II: both track how much is active, skyline needs the actual max, not just the count

**Cross-links:** `greedy` (exchange-argument proof for why earliest-finish-time greedy is optimal, and the activity-selection framing behind "erase overlap intervals"), `heaps` (heap mechanics used in Meeting Rooms II and Skyline), `arrays-strings` (prefix-sum/difference-array alternative mentioned in the sweep-line technique).

## Group: Bit Manipulation (bit-manipulation)

### Topic: Bitwise Operators and Number Representation (bitwise-fundamentals, beginner)
The AND/OR/XOR/NOT/shift primitives and two's-complement representation everything else in this group builds on.
- [overview] AND, OR, XOR, NOT, and shifts: the primitives everything else in this group builds on
- [concept] Two's complement: why negative numbers are represented — and behave — the way they do
- [diagram] One byte's bit pattern under AND, OR, XOR, and NOT, side by side
- [concept] Left and right shift as multiply/divide by powers of two — and where that stops being true
- [pitfall] Arithmetic right shift versus logical right shift on a negative number
- [pitfall] Shifting by an amount >= the type's bit width — undefined or implementation-specific
- [concept] Precedence traps: bitwise operators binding looser than comparisons in several languages
- [compare] Signed versus unsigned overflow behavior under bitwise operations across common interview languages

### Topic: Bit Manipulation Idioms — Get, Set, Clear, Toggle (bit-idioms, beginner)
The four standard mask-based operations — get, set, clear, and toggle a bit or a range of bits.
- [overview] Four idioms every bit-manipulation question builds on: get, set, clear, and toggle a bit
- [concept] Building a single-bit mask with 1 << i as the basis for all four idioms
- [code] get/set/clear/toggle bit i, each as a one-line operation
- [diagram] A mask being ANDed, ORed, or XORed against a value to change exactly one bit
- [code] Clearing and updating a contiguous range of bits with a constructed mask
- [pitfall] Using OR to "set" a bit when you actually meant to overwrite it regardless of its current value
- [pitfall] Off-by-one in bit indexing: bit 0 as least-significant versus an assumed 1-indexed scheme
- [concept] Why masks generalize past single bits: any subset of positions is just a wider mask

### Topic: XOR Properties and the Single-Number Family (xor-tricks, intermediate)
XOR's self-canceling property and the Single-Number family of problems it solves in O(1) space.
- [overview] XOR's self-canceling property, and the family of problems it unlocks
- [concept] The three properties that matter: a^a=0, a^0=a, and XOR is commutative and associative
- [diagram] XOR-folding an array down to the one element without a pair
- [code] Single Number I: every element appears twice except one
- [compare] Single Number II (every element appears three times except one) needs per-bit counting, not a plain XOR fold
- [compare] Single Number III (two unique elements) — using a distinguishing bit to split the array in two
- [code] Finding a missing number in the range 0..n via XOR instead of a sum-based formula
- [pitfall] Reaching for XOR when duplicates aren't guaranteed to pair up evenly
- [concept] XOR swap without a temp variable — a curiosity worth recognizing, not a habit worth keeping

### Topic: Bit-Counting Tricks — Brian Kernighan's Algorithm and Popcount (bit-counting, intermediate)
Counting and isolating set bits fast with Brian Kernighan's trick, popcount, and power-of-two checks.
- [overview] Counting set bits fast: Brian Kernighan's trick and when it's worth reaching for
- [concept] Why n & (n-1) clears exactly the lowest set bit
- [diagram] Repeated n & (n-1), peeling off one set bit per iteration until n reaches zero
- [code] The Brian Kernighan popcount loop — O(number of set bits), not O(bit width)
- [concept] n & -n isolates the lowest set bit instead of clearing it — a related but different trick
- [code] A one-line power-of-two check using n & (n-1) == 0
- [compare] Brian Kernighan's loop versus a language built-in popcount versus a precomputed lookup table
- [pitfall] Forgetting the n == 0 edge case in a popcount or power-of-two check

### Topic: Bitmasking for Subsets — Representing Sets as Integers (bitmask-subsets, advanced)
Representing and enumerating subsets of a small item set as integer bitmasks.
- [overview] Representing a subset of a small item set as a single integer bitmask
- [concept] Why n items map to 2^n masks — and why that caps this technique to small n
- [diagram] Enumerating every subset of {A, B, C} as the masks 000 through 111
- [code] Iterating all 2^n subsets with a plain loop over the integer range
- [code] Iterating all submasks of a given mask efficiently
- [concept] Checking membership, adding, and removing an element from a subset mask
- [concept] Bridging idea: why a bitmask is a compact, hashable DP state — cross-link `dynamic-programming` for the actual recurrence
- [pitfall] Reaching for a bitmask when n is large enough that 2^n blows the time budget
- [compare] Bitmask subset enumeration versus recursive backtracking over subsets — same outcomes, different constants and reuse

**Cross-links:** `dynamic-programming` (bitmask DP recurrences, e.g. TSP/assignment-style problems), `recursion-backtracking` (recursive subset enumeration as the alternative to bitmask iteration).

## Group: Math & Number Theory (math-number-theory)

### Topic: GCD, LCM, and the Euclidean Algorithm (gcd-lcm-euclidean, beginner)
Computing GCD and LCM fast with the Euclidean algorithm's remainder identity.
- [overview] GCD and LCM: the building blocks under fractions, ratios, and cycle-length problems
- [concept] The Euclidean algorithm's key identity: gcd(a, b) = gcd(b, a mod b)
- [diagram] Tracing gcd(48, 18) down through successive remainders to zero
- [code] Recursive and iterative Euclidean algorithm implementations
- [concept] LCM from GCD: lcm(a, b) = a * b / gcd(a, b), and why the division comes first
- [pitfall] Multiplying a * b before dividing by the GCD and overflowing
- [concept] Complexity: O(log(min(a, b))) — why this stays fast even on huge numbers
- [pitfall] Treating gcd(0, n) as an error case instead of the defined base case, n

### Topic: Primality Testing and the Sieve of Eratosthenes (primes-sieve, beginner)
Testing a single number for primality versus precomputing all primes up to N with the Sieve of Eratosthenes.
- [overview] Testing one number for primality versus finding every prime up to N
- [concept] Trial division up to sqrt(n) — why you never need to check past the square root
- [code] An O(sqrt(n)) single-number primality check
- [concept] The Sieve of Eratosthenes: marking composites instead of testing each number independently
- [diagram] The sieve array, watching multiples of 2, 3, and 5 get struck out
- [code] Building a Sieve of Eratosthenes boolean array up to N
- [concept] Why the sieve's outer loop only needs to run to sqrt(N)
- [compare] Trial division per query versus precomputing a sieve — pick based on how many queries you'll answer
- [pitfall] Starting the inner marking loop at 2*p instead of p*p, and redoing already-marked work

### Topic: Extended Euclidean Algorithm and Bezout's Identity (extended-euclidean, intermediate)
Recovering the Bezout coefficients behind gcd(a,b) = ax + by, and what that unlocks.
- [overview] Extended Euclid: recovering the coefficients behind gcd(a, b) = a*x + b*y
- [concept] Bezout's identity: gcd(a, b) is always expressible as an integer combination of a and b
- [diagram] Unwinding the Euclidean recursion, back-substituting x and y at each level
- [code] Recursive extended Euclidean algorithm returning (gcd, x, y)
- [concept] Why this matters: it's the general-purpose way to solve ax + by = c over the integers
- [compare] Extended Euclid versus Fermat's little theorem — two different routes to a modular inverse
- [pitfall] Sign errors when back-substituting coefficients up through the recursion
- [concept] A solution to ax + by = c exists only when gcd(a, b) divides c

### Topic: Modular Arithmetic, Fast Exponentiation, and Modular Inverse (modular-arithmetic, intermediate)
Keeping arithmetic inside a fixed range with fast exponentiation and modular inverses.
- [overview] Doing arithmetic that never leaves a fixed range, and why interviews lean on it
- [concept] Modular addition, subtraction, and multiplication: reduce after every operation, not just at the end
- [pitfall] Modular subtraction going negative without adding the modulus back
- [concept] Fast exponentiation: computing a^b mod m in O(log b) instead of O(b)
- [diagram] Repeated squaring, halving the exponent at each step
- [code] Iterative fast exponentiation with modular reduction at each step
- [concept] Modular inverse: the number that "undoes" multiplication by a, modulo m
- [code] Modular inverse via Fermat's little theorem when m is prime: a^(m-2) mod m
- [compare] Fermat-based inverse (prime modulus only) versus extended-Euclid-based inverse (any modulus coprime to a)
- [pitfall] Dividing directly under a modulus instead of multiplying by the modular inverse

### Topic: Basic Combinatorics — Factorials, nCr, and Pascal's Triangle (combinatorics-basics, intermediate)
Counting arrangements and selections with factorials, nCr, and Pascal's triangle, including nCr under a modulus.
- [overview] Counting arrangements and selections: factorials, permutations, and combinations
- [concept] Permutations (order matters) versus combinations (order doesn't) — nPr versus nCr
- [concept] Computing nCr via factorials, and why that overflows or loses precision fast
- [code] Computing nCr mod p using precomputed factorials and a modular inverse
- [diagram] Pascal's triangle as nCr built from nCr(n-1, r-1) + nCr(n-1, r)
- [code] Building an nCr table via the Pascal's-triangle recurrence, with no division at all
- [compare] Factorial-formula nCr versus Pascal's-triangle nCr — overflow risk versus precompute cost
- [pitfall] Computing nCr with plain integer division and losing correctness mid-calculation
- [concept] Where this shows up: grid path counting, probability questions, "how many ways" prompts

**Cross-links:** `dynamic-programming` (Pascal's-triangle-style tables and grid path counting are treated as DP topics there).

## Group: Coding Interview Strategy (coding-interview-strategy)

### Topic: Clarifying Questions Before You Code (clarifying-questions, beginner)
The questions worth asking before writing any code, chosen because the answer actually changes your approach.
- [overview] The first two minutes: questions worth asking before you write a line of code
- [concept] Constraint questions that change the algorithm: input size, value range, sortedness, duplicates
- [concept] Ambiguity questions that change the answer: empty input, one element, negative numbers, ties
- [pitfall] Asking a question that doesn't change your approach at all — a wasted signal, not a good one
- [compare] "What if the array is empty?" (changes your code) versus "what language should I use?" (signals nothing)
- [concept] Restating the problem in your own words before proposing an approach
- [pitfall] Silently assuming an input property, like sortedness or no duplicates, instead of confirming it
- [concept] Reading n <= 10^5 versus n <= 10^9 as a direct hint at the time complexity you're expected to hit

### Topic: Thinking Out Loud and Structuring Your Code (thinking-out-loud, beginner)
Narrating your approach and structuring your code so the interviewer can follow and credit your thinking.
- [overview] What to say, and when, so the interviewer can follow — and credit — your thinking
- [concept] The narration loop: state your approach, state its complexity, then start coding
- [pitfall] Going silent for several minutes while you work out the full solution in your head first
- [concept] Naming variables and functions for meaning, not i/j/tmp/flag, even under time pressure
- [concept] Decomposing into small helper functions so partial progress stays visible and gradable
- [pitfall] Narrating so much low-level detail that the real signal drowns in noise
- [compare] Mentioning the brute force first versus jumping straight to the optimal approach silently
- [concept] Flagging your own trade-offs before being asked: "this is O(n^2); I can get it to O(n log n) if needed"

### Topic: Pattern Recognition — Mapping Problem Cues to Technique (pattern-recognition-framework, intermediate)
Mapping a problem's surface cues and constraints to the right technique from across the other DSA groups.
- [overview] Why fast interviewers look "psychic": they're matching cues to a known technique, not inventing one
- [concept] Keyword cues: "contiguous subarray/substring" points to sliding window; "kth largest" points to a heap; "all combinations" points to backtracking
- [concept] More keyword cues: "shortest path" points to BFS or Dijkstra; "connected components" points to Union-Find or DFS; "max/min over choices" points to DP or greedy
- [diagram] A decision tree: input shape — array, tree, graph, string — narrowing which sibling group's toolbox applies
- [concept] Constraint-size cues: n <= 20 hints at bitmask brute force; n <= 10^5 hints at O(n log n); n <= 10^9 hints at O(log n) or O(1)
- [compare] "Sounds like DP" versus "actually greedy suffices" — the tell is whether a choice can be revisited
- [pitfall] Locking onto a technique from a surface word like "optimal" before checking what the constraints actually allow
- [concept] Multi-technique problems: recognizing when a solution chains two patterns, like sort-then-two-pointer or hash-map-then-window
- [pitfall] Force-fitting the one pattern you're most comfortable with onto a problem that doesn't call for it
- [concept] Building your own cue sheet from practice: logging which phrase led to which technique after each problem

### Topic: Talking Through Complexity Trade-offs (complexity-tradeoff-communication, intermediate)
Proactively stating and defending the time/space trade-offs of your solution as you build it.
- [overview] Complexity isn't just a number at the end — it's a conversation you steer
- [concept] Stating both time and space complexity, unprompted, for every approach you propose
- [concept] Naming the trade-off explicitly: framing it as "trading O(n) space for O(1) time," not just stating two numbers
- [compare] Presenting the brute-force complexity as a baseline first, then showing exactly what your optimization buys
- [pitfall] Misstating your own solution's complexity because a hidden sort or hash rebuild went uncounted
- [concept] Amortized complexity: explaining why a resizing array append is O(1) on average, without hand-waving
- [pitfall] Quoting Big-O in the wrong variable, like saying O(n) when the real driver is O(V+E) on a graph
- [concept] Deciding when to proactively offer a further optimization versus waiting for the interviewer's follow-up

### Topic: Testing Your Own Code — Live Edge-Case Discipline (live-testing-discipline, intermediate)
Finding your own bugs live by dry-running edge cases before declaring a solution done.
- [overview] Interviewers grade how you find your own bugs, not just whether your code has any
- [concept] A standing edge-case checklist: empty input, single element, all-duplicates, already-sorted, negative or zero values
- [concept] Dry-running your own code on a small example by hand, out loud, before declaring it done
- [diagram] Tracing variable state line by line through one small example to catch an off-by-one live
- [pitfall] Testing only the happy-path example the interviewer originally gave you
- [concept] Reading your code once for the specific bug classes you personally tend to make
- [compare] Tracing by hand on the whiteboard versus mentally simulating — when the written trace earns its time cost
- [pitfall] Patching the symptom at the input where you found a bug, instead of fixing the root cause

### Topic: Getting Stuck and Taking a Hint Gracefully (handling-being-stuck, advanced)
Recovering from a stall and incorporating a hint without abandoning your technical footing.
- [overview] Being stuck is expected — what separates a recoverable stall from a silent collapse
- [concept] Narrating the stall itself: saying what you've ruled out and why, instead of going quiet
- [concept] Falling back to a brute force out loud as a checkpoint, rather than abandoning the problem
- [pitfall] Insisting on your original approach after a hint clearly points somewhere else
- [concept] Treating a hint as new information to fold in, not as a signal that you've failed
- [compare] A candidate who asks a targeted question when stuck versus one who waits silently for rescue
- [concept] Using your own clarifying-question habit as an unstuck tool: re-reading the constraints for a clue you missed
- [pitfall] Over-apologizing or narrating anxiety instead of just continuing the technical thread
- [concept] Recovering your time budget after a stall: what to cut so you still land a working solution

**Cross-links:** `two-pointers-sliding-window`, `heaps`, `graphs`, `dynamic-programming`, `greedy`, `bit-manipulation` (the pattern-recognition framework maps cues into each of these — and the other remaining groups — without re-teaching their techniques).
