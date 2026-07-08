A string problem is rarely "just loop over the characters." The interesting ones ask you to **find a pattern inside text** (does `needle` occur in `haystack`? where?), or to **transform text in place** under tight constraints (reverse, compress, justify, reformat). Both halves lean on the same toolkit: character counts, sliding windows, and — for real matching algorithms — precomputed tables that let you skip work instead of re-scanning.

Naive substring search compares the pattern at every starting offset, giving O(n·m). The classic upgrade is to **precompute information about the pattern itself** so a mismatch tells you how far you can safely jump, instead of restarting from scratch.

**KMP (Knuth-Morris-Pratt)** builds a *failure function* — for each prefix of the pattern, the length of the longest proper prefix that is also a suffix. On a mismatch, you fall back using that table instead of resetting the pattern pointer to zero, giving O(n + m) matching.

**Rabin-Karp** takes a different route: hash every window of the text with a *rolling hash* (O(1) to slide one character) and only do a real character comparison when hashes collide. Good for multiple-pattern search and duplicate-substring problems.

A typical KMP-shaped skeleton:

```
build failure[] for pattern       // failure[i] = longest prefix-suffix of pattern[0..i]
i = 0, j = 0                      // i walks text, j walks pattern
while i < len(text):
    if text[i] == pattern[j]:
        i += 1; j += 1
        if j == len(pattern): record match at i - j; j = failure[j - 1]
    elif j > 0:
        j = failure[j - 1]        // skip using the table, do not restart at i
    else:
        i += 1
```

Manipulation problems (reverse words, compression, zigzag, justify) are usually simulation: build the output with careful indices or a buffer, respecting the exact rules given.
