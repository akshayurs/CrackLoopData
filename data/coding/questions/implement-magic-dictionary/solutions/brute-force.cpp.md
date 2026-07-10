The simplest reading of the rule "changing exactly one character" is to just check it directly against every stored word: same length, and exactly one position differs. No trie, no preprocessing beyond keeping the list around.

It is the honest baseline you would state first in an interview before reaching for a trie.

```cpp
#include <string>
#include <vector>
using namespace std;

class MagicDictionary {
public:
    MagicDictionary() {}

    void buildDict(vector<string> dictionary) {
        words = dictionary;
    }

    bool search(string searchWord) {
        for (const string& candidate : words) {
            if (candidate.size() != searchWord.size()) continue;
            int diff = 0;
            for (size_t i = 0; i < searchWord.size(); i++) {
                if (candidate[i] != searchWord[i]) diff++;
            }
            if (diff == 1) return true;
        }
        return false;
    }

private:
    vector<string> words;
};
```

## Why it works

`buildDict` just remembers the words. `search` scans every stored word, skips any whose length doesn't match (a length mismatch can never be a one-letter substitution), and counts differing positions. A candidate qualifies only if exactly one position differs — zero differences means the words are identical, not a genuine change.

## Complexity

- Time: O(N·L) — each search compares against up to N stored words of length up to L.
- Space: O(N·L) — storing all the words.
