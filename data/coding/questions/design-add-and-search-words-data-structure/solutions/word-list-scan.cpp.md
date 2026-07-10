The simplest dictionary "implementation" doesn't build any tree at all — it just remembers every added word in a vector. `addWord` is a single push. `search` compares the query against every stored word of the same length, treating each `.` as an automatic match for whatever letter sits in that position.

This is the honest baseline: correct and easy to write under pressure, but it re-scans everything stored so far on every query, and the comparison itself costs a full pass over the word.

```cpp
#include <string>
#include <vector>
using namespace std;

class WordDictionary {
public:
    WordDictionary() {}

    void addWord(string word) {
        words.push_back(word);
    }

    bool search(string word) {
        for (const auto& w : words) {
            if (w.size() != word.size()) continue;
            bool match = true;
            for (size_t i = 0; i < word.size(); i++) {
                if (word[i] != '.' && word[i] != w[i]) {
                    match = false;
                    break;
                }
            }
            if (match) return true;
        }
        return false;
    }

private:
    vector<string> words;
};
```

## Why it works

`words` records everything added, duplicates included. For a query to match a stored word they must first be the same length, since `.` stands for exactly one letter, never zero or many. The inner loop walks both strings position by position, and a mismatch only counts when the query character is a concrete letter that differs from the stored one — a `.` always passes. The first stored word that survives the whole walk makes `search` return `true` immediately.

## Complexity

- Time: O(1) for `addWord`; O(n * L) for `search`, where n is the number of stored words and L is the word length.
- Space: O(n * L) to store every added word.
