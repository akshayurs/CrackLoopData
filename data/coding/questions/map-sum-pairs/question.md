Design a `MapSum` structure that stores string keys mapped to integer values and can quickly total the values of every key sharing a given prefix. Implement two operations: `insert(key, val)`, which stores `val` under `key` (overwriting any previous value already stored under that exact key), and `sum(prefix)`, which returns the sum of the values of all keys currently in the structure that start with `prefix`.

## Examples

```text
Input:
insert("apple", 3)
sum("ap")
insert("app", 2)
sum("ap")

Output: 3, 5
# after insert("apple", 3): only "apple" exists, so sum("ap") = 3
# after insert("app", 2): "apple" and "app" both start with "ap", so sum("ap") = 3 + 2 = 5
```

```text
Input:
insert("apple", 3)
sum("ap")
insert("apple", 2)
sum("ap")

Output: 3, 2
# re-inserting "apple" overwrites its old value (3 -> 2) instead of adding a second entry
```

```text
Input:
insert("bat", 5)
sum("bath")
sum("bat")

Output: 0, 5
# no stored key starts with "bath", so that sum is 0; "bat" itself matches "bat"
```

## Constraints

- 1 <= key.length, prefix.length <= 50
- 1 <= val <= 1000
- key and prefix consist only of lowercase English letters.
- At most 50 calls in total to `insert` and `sum`.
- The sum of all returned values fits comfortably in a 32-bit signed integer.

## Follow-up

`insert` and brute-force `sum` are easy; can you make `sum` run in time proportional to `prefix.length` instead of scanning every stored key?
