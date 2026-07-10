You are given an `m x n` grid of lowercase letters `board` and a list of strings `words`. Return every word from `words` that can be traced on the board.

A word is traceable if it can be built from letters of sequentially adjacent cells, where "adjacent" means horizontally or vertically neighboring. The same cell may not be reused more than once within a single word, but a cell can be reused across different words. Return the matches sorted alphabetically.

## Examples

```text
Input:  board = [["o","a","a","n"],
                  ["e","t","a","e"],
                  ["i","h","k","r"],
                  ["i","f","l","v"]]
        words = ["oath", "pea", "eat", "rain"]
Output: ["eat", "oath"]
```

```text
Input:  board = [["a","b"],
                  ["c","d"]]
        words = ["abcb"]
Output: []        # "abcb" would need to revisit "b"
```

```text
Input:  board = [["a","b","c"],
                  ["a","e","d"],
                  ["a","f","g"]]
        words = ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ege"]
Output: ["abcdefg", "befa", "eaabcdgfa", "gfedcbaaa"]
```

## Constraints

- 1 <= board.length, board[i].length <= 12
- board[i][j] is a lowercase English letter.
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters.
- All strings in `words` are unique.

## Follow-up

The brute-force approach re-scans the whole board once per word. Can you search for all words in a single pass over the board?
