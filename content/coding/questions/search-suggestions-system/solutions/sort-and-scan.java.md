Sort the catalog once so matches for any prefix already come out in the right order. Then, for every prefix of `searchWord` (length 1, 2, 3, ...), walk the sorted list and collect the first three entries that start with it.

This redoes a linear scan for every prefix, so it re-examines products you already ruled out on the previous, shorter prefix — simple, but wasteful once the query gets long.

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<String>> searchSuggestions(String[] products, String searchWord) {
        Arrays.sort(products);
        List<List<String>> result = new ArrayList<>();
        StringBuilder prefix = new StringBuilder();
        for (char ch : searchWord.toCharArray()) {
            prefix.append(ch);
            List<String> matches = new ArrayList<>();
            for (String p : products) {
                if (p.startsWith(prefix.toString())) {
                    matches.add(p);
                    if (matches.size() == 3) break;
                }
            }
            result.add(matches);
        }
        return result;
    }
}
```

## Why it works

Sorting the catalog once guarantees that any subset of matches, collected in array order, is already lexicographically sorted — so taking the first three matches is always the three smallest. Checking `startsWith` against the growing prefix correctly narrows the candidate set at each step, and stopping once 3 are found caps the suggestion list as required.

## Complexity

- Time: O(n log n + m * n * L) — one sort, then for each of the `m` prefix lengths a scan of `n` products with an O(L) prefix check.
- Space: O(n) — the output lists (sorting is done in place).
