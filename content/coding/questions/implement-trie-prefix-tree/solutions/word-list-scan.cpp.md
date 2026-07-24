The simplest possible trie "implementation" doesn't build a tree at all — it just keeps every inserted word in a vector. `search` checks for an exact match; `startsWith` checks whether any stored word begins with the prefix.

This is the honest baseline: correct, easy to write under pressure, but it re-scans everything stored so far on every query.

```cpp
#include <string>
#include <vector>
using namespace std;

class Trie {
public:
    Trie() {}

    void insert(string word) {
        words.push_back(word);
    }

    bool search(string word) {
        for (const string& w : words) {
            if (w == word) {
                return true;
            }
        }
        return false;
    }

    bool startsWith(string prefix) {
        for (const string& w : words) {
            if (w.compare(0, prefix.size(), prefix) == 0) {
                return true;
            }
        }
        return false;
    }

private:
    vector<string> words;
};
```

## Why it works

`words` is just a record of everything inserted, duplicates and all. `search` asks whether `word` appears verbatim in that record. `startsWith` walks the record and returns as soon as one entry's first `prefix.size()` characters match `prefix` exactly. Nothing here depends on shared structure between words, so correctness is immediate, but so is the cost of re-checking every stored word on every call.

## Complexity

- Time: O(L) for `insert`; O(n * L) for `search` and `startsWith`, where n is the number of inserted words and L is the average word length.
- Space: O(n * L) to store every inserted word.
