Same literal approach in C++: tokenize the sentence on spaces and, for each word, scan the whole dictionary for the shortest root that is a prefix of it.

`string::compare` on a bounded range gives the prefix check without allocating a substring, but the dictionary is still rescanned for every word.

```cpp
#include <string>
#include <vector>
#include <sstream>
using namespace std;

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        istringstream iss(sentence);
        string word;
        vector<string> result;
        while (iss >> word) {
            string best;
            for (const string& root : dictionary) {
                if (word.compare(0, root.size(), root) == 0 &&
                    (best.empty() || root.size() < best.size())) {
                    best = root;
                }
            }
            result.push_back(best.empty() ? word : best);
        }
        string out;
        for (size_t i = 0; i < result.size(); i++) {
            if (i) out += " ";
            out += result[i];
        }
        return out;
    }
};
```

## Why it works

`word.compare(0, root.size(), root)` compares the leading `root.size()` characters of `word` against `root`, returning 0 only when `root` is genuinely a prefix (a longer root can never match a shorter word). `best` keeps the shortest such root across the whole dictionary scan, and a word with no match is emitted unchanged.

## Complexity

- Time: O(w * r * L) — w words, r roots, up to L characters compared per `compare` call.
- Space: O(w) — the output buffer, ignoring the input.
