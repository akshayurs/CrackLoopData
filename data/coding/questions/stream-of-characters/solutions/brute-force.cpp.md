Keep every letter the stream has produced in a growing buffer. On each `query`, walk the dictionary and test whether the buffer's tail matches that word exactly.

This is easy to write correctly first, then optimize once it's clear where the time goes.

```cpp
#include <string>
#include <vector>

class StreamChecker {
public:
    StreamChecker(std::vector<std::string> words) : words(std::move(words)) {}

    bool query(char letter) {
        stream.push_back(letter);
        int len = stream.size();
        for (const std::string& word : words) {
            int n = word.size();
            if (n <= len && stream.compare(len - n, n, word) == 0) {
                return true;
            }
        }
        return false;
    }

private:
    std::vector<std::string> words;
    std::string stream;
};
```

## Why it works

`stream` holds the full history in order, so its last `n` characters are exactly the last `n` letters seen — `compare` at that offset answers "does the stream end with this word?". Checking every word on every call is correct because there is no shortcut yet for skipping non-matching prefixes.

## Complexity

- Time: O(Q * W * L) — Q queries, each scanning W words of average length L to compare a suffix.
- Space: O(Q + W * L) — the buffer grows with the stream; the dictionary is stored as given.
