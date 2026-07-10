The same literal approach in JavaScript: split the sentence into words, and for each one scan every root in the dictionary, keeping the shortest one that is a prefix of the word.

No preprocessing happens, so the cost of the dictionary scan is paid once per word — but the code is a direct translation of the rule in the problem statement.

```javascript
function replaceWords(dictionary, sentence) {
  const result = [];
  for (const word of sentence.split(" ")) {
    let best = null;
    for (const root of dictionary) {
      if (word.startsWith(root) && (best === null || root.length < best.length)) {
        best = root;
      }
    }
    result.push(best !== null ? best : word);
  }
  return result.join(" ");
}
```

## Why it works

`best` tracks the shortest root confirmed to prefix the current word, using `startsWith` for the prefix check. Every root is tried for every word, so no valid match is ever skipped, and the length comparison keeps only the shortest candidate. Words with no matching root are pushed through unchanged.

## Complexity

- Time: O(w * r * L) — w words, r roots, up to L characters compared per `startsWith` call.
- Space: O(w) — the output array, ignoring the input.
