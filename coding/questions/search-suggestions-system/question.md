You're given an array of strings `products` — a search catalog — and a string `searchWord` that a user types one character at a time. After each character is typed, suggest up to three products from the catalog that start with the text typed so far: pick the three lexicographically smallest matches (fewer if less than three exist, an empty list if none exist), and list them in lexicographical order.

Return a list with one entry per character of `searchWord`, in the order the characters were typed.

## Examples

```text
Input:  products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord = "mouse"
Output: [
  ["mobile", "moneypot", "monitor"],
  ["mobile", "moneypot", "monitor"],
  ["mouse", "mousepad"],
  ["mouse", "mousepad"],
  ["mouse", "mousepad"]
]
```

```text
Input:  products = ["havana"], searchWord = "havana"
Output: [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
```

```text
Input:  products = ["bags", "baggage", "banner", "box", "cloths"], searchWord = "bags"
Output: [["baggage", "bags", "banner"], ["baggage", "bags", "banner"], ["baggage", "bags"], ["bags"]]
```

## Constraints

- 1 <= products.length <= 1000
- 1 <= products[i].length <= 3000
- sum(products[i].length) <= 2 * 10^4
- 1 <= searchWord.length <= 1000
- `products[i]` and `searchWord` consist of lowercase English letters only.
