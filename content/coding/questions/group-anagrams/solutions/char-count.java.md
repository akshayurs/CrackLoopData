Sorting each string is more work than the problem needs. What actually defines an anagram group is the count of each of the 26 lowercase letters — not their order. So build a fixed 26-length count array for each string and use *that* as the key, skipping the O(k log k) sort entirely.

Serialize the counts into a `String` so it can key a `HashMap`. Every anagram produces the same serialized counts, so the grouping matches the sort approach but each key costs only a linear pass over the string.

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> buckets = new HashMap<>();
        for (String s : strs) {
            int[] counts = new int[26];
            for (char ch : s.toCharArray()) {
                counts[ch - 'a']++;
            }
            StringBuilder key = new StringBuilder();
            for (int c : counts) key.append(c).append('#');
            buckets.computeIfAbsent(key.toString(), k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(buckets.values());
    }
}
```

## Why it works

Two strings are anagrams if and only if their per-letter frequency vectors are equal, so the serialized 26-count string is a perfect canonical key. Building it scans the string once — no comparison sort. The `#` separator keeps multi-digit counts unambiguous. Identical vectors collide into one bucket; any difference in even a single letter's count yields a different key and a separate group.

## Complexity

- Time: O(n · k) — n strings, each scanned once in O(k); building the 26-length key is O(k + 26).
- Space: O(n · k) — the stored strings dominate; each key is a constant 26 entries.
