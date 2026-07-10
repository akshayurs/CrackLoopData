Load every word into a `HashSet`, then test each word independently with a prefix DP: can the string be cut into two or more pieces, all of which are also words in the set? `dp[j]` records whether the prefix of length `j` can be fully covered.

Skipping the split where `i == 0` and `j == n` prevents the word from being "concatenated" out of just itself.

```java
import java.util.*;

class Solution {
    public List<String> findConcatenatedWords(String[] words) {
        Set<String> wordSet = new HashSet<>(Arrays.asList(words));
        List<String> result = new ArrayList<>();
        for (String word : words) {
            int n = word.length();
            boolean[] dp = new boolean[n + 1];
            dp[0] = true;
            for (int j = 1; j <= n; j++) {
                for (int i = 0; i < j; i++) {
                    if (!dp[i]) continue;
                    if (i == 0 && j == n) continue;
                    if (wordSet.contains(word.substring(i, j))) {
                        dp[j] = true;
                        break;
                    }
                }
            }
            if (dp[n]) result.add(word);
        }
        Collections.sort(result);
        return result;
    }
}
```

## Why it works

`dp[i]` true means the prefix of length `i` is fully assembled from set members. To reach `dp[j]`, some earlier boundary `i` must have `dp[i]` true and the middle chunk `word.substring(i, j)` must also be a member. Excluding the `i == 0, j == n` case rules out matching the whole word to itself, so `dp[n]` can only fire through a genuine multi-word split.

## Complexity

- Time: O(n · L³) — n words, each running an O(L²) DP whose transitions build and hash O(L)-length substrings.
- Space: O(n · L) — the set stores every word.
