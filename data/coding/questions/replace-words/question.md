In English, a shorter word can act as the *root* of a longer one — "help" is the root of "helper". You are given a `dictionary` of root words and a `sentence` (words separated by single spaces). For every word in the sentence, if some root in the dictionary is a prefix of that word, replace the word with the **shortest** such root. If a word has no matching root, leave it unchanged. Return the resulting sentence.

## Examples

```text
Input:  dictionary = ["cat", "bat", "rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

```text
Input:  dictionary = ["a", "b", "c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
```

```text
Input:  dictionary = ["ap"], sentence = "apple orange ap"
Output: "ap orange ap"        # "orange" has no matching root, so it stays as-is
```

## Constraints

- 1 <= dictionary.length <= 1000
- 1 <= dictionary[i].length <= 100
- dictionary[i] consists of lowercase English letters only.
- 1 <= sentence.length <= 10^6
- sentence has no leading/trailing spaces, and words are separated by exactly one space.
- Each word in sentence consists of lowercase English letters only.

## Follow-up

The brute force compares every word against every root. Can you preprocess the dictionary so each word is resolved by scanning only its own characters?
