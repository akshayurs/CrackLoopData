Drop every word into an `unordered_set` so membership checks are O(1), then test each word directly: it is buildable exactly when all of its proper prefixes also live in that set. Track the best answer seen so far, preferring a longer word or, on a length tie, the lexicographically smaller one.

This is the straightforward reading of the definition — no trie, just prefix slicing and a hash lookup for each one.

```cpp
#include <string>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    string longestWord(vector<string>& words) {
        unordered_set<string> wordSet(words.begin(), words.end());
        string best = "";
        for (const string& word : words) {
            bool buildable = true;
            for (size_t i = 1; i < word.size(); i++) {
                if (!wordSet.count(word.substr(0, i))) {
                    buildable = false;
                    break;
                }
            }
            if (buildable && (word.size() > best.size()
                    || (word.size() == best.size() && word < best))) {
                best = word;
            }
        }
        return best;
    }
};
```

## Why it works

A word is buildable only if every shorter prefix that would have been typed on the way to it is itself a word in the array. Checking `word.substr(0, i)` for every `i` from 1 up to (but not including) the full length verifies exactly that chain. Comparing candidates by length first, then lexicographically, reproduces the required tie-break rule.

## Complexity

- Time: O(n · L²) — n words, each with up to L prefixes, each substring and lookup costing O(L).
- Space: O(n · L) — the hash set stores every word.
