Load every word into an `unordered_set`, then test each word independently with a prefix DP: can the string be cut into two or more pieces that are all words in the set? `dp[j]` tracks whether the prefix of length `j` can be fully covered.

Skipping the split where `i == 0` and `j == n` rules out matching a word to itself as a single unbroken piece.

```cpp
#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<string> findConcatenatedWords(vector<string>& words) {
        unordered_set<string> wordSet(words.begin(), words.end());
        vector<string> result;
        for (const string& word : words) {
            int n = word.size();
            vector<bool> dp(n + 1, false);
            dp[0] = true;
            for (int j = 1; j <= n; j++) {
                for (int i = 0; i < j; i++) {
                    if (!dp[i]) continue;
                    if (i == 0 && j == n) continue;
                    if (wordSet.count(word.substr(i, j - i))) {
                        dp[j] = true;
                        break;
                    }
                }
            }
            if (dp[n]) result.push_back(word);
        }
        sort(result.begin(), result.end());
        return result;
    }
};
```

## Why it works

`dp[i]` true means the prefix of length `i` is fully built from set members. Reaching `dp[j]` requires some boundary `i` with `dp[i]` true where the middle chunk `word.substr(i, j - i)` is also a member. Excluding `i == 0 && j == n` blocks the trivial whole-word match, so `dp[n]` only turns true through a genuine multi-word split.

## Complexity

- Time: O(n · L³) — n words, each running an O(L²) DP whose transitions build and hash O(L)-length substrings.
- Space: O(n · L) — the set stores every word.
