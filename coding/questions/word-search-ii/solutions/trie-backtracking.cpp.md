The brute-force approach wastes effort because many words share prefixes — searching for `"eat"` and `"eaten"` separately walks the same first three letters twice. Merge every word into a single trie first, then make **one** DFS pass over the board, walking the trie in step with the board instead of walking a fixed word string.

At each board cell, follow the trie edge matching that cell's letter. Whenever the trie node reached marks the end of a word, record it and clear the marker so the same word is never added twice.

```cpp
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct TrieNode {
    TrieNode* children[26] = {};
    string word;
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode root;
        for (const string& w : words) {
            TrieNode* node = &root;
            for (char ch : w) {
                int idx = ch - 'a';
                if (!node->children[idx]) node->children[idx] = new TrieNode();
                node = node->children[idx];
            }
            node->word = w;
        }
        rows = board.size();
        cols = board[0].size();
        this->board = &board;
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                dfs(r, c, &root);
        sort(found.begin(), found.end());
        return found;
    }

private:
    vector<vector<char>>* board;
    int rows, cols;
    vector<string> found;

    void dfs(int r, int c, TrieNode* node) {
        char ch = (*board)[r][c];
        if (ch == '*') return;
        TrieNode* next = node->children[ch - 'a'];
        if (!next) return;
        if (!next->word.empty()) {
            found.push_back(next->word);
            next->word.clear();
        }
        (*board)[r][c] = '*';
        int dr[] = {1, -1, 0, 0}, dc[] = {0, 0, 1, -1};
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i], nc = c + dc[i];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) dfs(nr, nc, next);
        }
        (*board)[r][c] = ch;
    }
};
```

## Why it works

The trie lets every board path be walked once and checked against all words that share its prefix simultaneously, instead of once per word. Marking a cell `'*'` during the current path prevents reusing it within one word, and restoring it afterward lets other paths use it. Clearing the `word` field guarantees a word is reported at most once even if multiple paths could spell it.

## Complexity

- Time: O(m · n · 4^L) — one DFS pass over the board, where each cell's search branches up to 4 ways per remaining trie depth (bounded by max word length L); building the trie is O(sum of word lengths).
- Space: O(sum of word lengths) — the trie, plus O(L) recursion depth.
