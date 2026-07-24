Anagrams share one property that survives rearrangement: sort their letters and they become identical. So the sorted form of a string is a fingerprint that every member of a group agrees on — `"eat"`, `"tea"`, and `"ate"` all sort to `"aet"`.

Use that fingerprint as a `HashMap` key. Walk the array once, sort each string's characters to get its key, and add the original string to the bucket for that key. The bucket values are the answer.

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> buckets = new HashMap<>();
        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            buckets.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(buckets.values());
    }
}
```

## Why it works

Two strings are anagrams exactly when their multisets of characters match, and sorting canonicalizes that multiset into a single comparable string. Strings with the same sorted key land in the same bucket; strings with different letters never collide. Because we add the original (unsorted) string, each group preserves the input words.

## Complexity

- Time: O(n · k log k) — for n strings of max length k, each sort costs O(k log k).
- Space: O(n · k) — every character is stored once across the buckets.
