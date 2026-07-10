You are given an array of strings `strs`. Group together the strings that are **anagrams** of one another and return the groups.

Two strings are anagrams when one can be rearranged into the other — they contain exactly the same letters with the same counts. The groups may be returned in any order, and the strings within each group may be in any order.

## Examples

```text
Input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

```text
Input:  strs = [""]
Output: [[""]]        # a single empty string forms its own group
```

```text
Input:  strs = ["a"]
Output: [["a"]]
```

## Constraints

- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

## Follow-up

The order of the groups and the order within a group don't matter. Can you avoid sorting each string?
