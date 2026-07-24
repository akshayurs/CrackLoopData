Reach for the string-algorithms toolkit when a problem sounds like any of these:

- **"Find the first occurrence of a substring"** — `strStr()`-style search. Naive is fine to mention, but KMP is the O(n + m) upgrade worth naming.
- **"Does the string repeat a pattern?"** — repeated substring pattern, repeated DNA sequences. Rolling hash or KMP's failure function both apply.
- **"Find the shortest palindrome / longest happy prefix"** — these are disguised failure-function problems: build pattern = `s + '#' + reverse(s)` (or similar) and read the answer off the last failure-function value.
- **"Compress / decompress / reformat this string under exact rules"** — String Compression, Zigzag Conversion, Text Justification, Integer to English Words. No fancy algorithm — careful index bookkeeping and edge cases (single char runs, last line justification, leading zeros).
- **"Group strings that are shifts/rotations/anagrams of each other"** — Group Shifted Strings: normalize each string to a canonical key (e.g., pairwise character differences mod 26) and bucket by key.
- **"Compare two dotted/segmented strings"** — Compare Version Numbers: split on the separator, compare segment by segment, watch numeric vs lexicographic comparison.

Signal words: *"substring"*, *"occurrence"*, *"repeated pattern"*, *"prefix that is also a suffix"*, *"in-place"*, *"reformat"*, *"palindrome"*. If the brute force is an O(n·m) nested scan over text and pattern, that is the cue to ask whether KMP or rolling hash removes the inner loop. If the problem is about *shape* of output (spacing, line breaks, casing) rather than search, it is simulation, not a matching algorithm — do not over-engineer it.
